### airflow/api/common/experimental/tapd_trigger.py ###

"""
Custom trigger dag feature:
 - allows for pass through of url params to be stored as instance specific xcom key/value pairs
 - returns json of the xcom key/values
 - triggers relative dagruns

modeled from '/trigger'

By:               Christopher R Harty
Created:          Oct 2022
Compatible with:  Apache Airflow 2.4.2
"""

"""Triggering DAG runs APIs."""
from __future__ import annotations

import json
from datetime import datetime

from airflow.exceptions import DagRunAlreadyExists, DagNotFound, AirflowException
from airflow.models import DagBag, DagModel, DagRun, XCom
from airflow.utils import timezone
from airflow.utils.state import DagRunState
from airflow.utils.types import DagRunType



from airflow.settings import Session
from airflow.utils import timezone
from airflow.utils.state import State

from airflow.configuration import conf


__all__ = ['tapd_enhanced_trigger_dag']


def _customize_xcom(dag_id, run_id, execution_date, params):

    # tapd_
    prefix_text = conf.get('tapd', 'enhanced_trigger_xcom_key_prefix')

    # tapd_args
    custom_task_id = conf.get('tapd', 'enhanced_trigger_xcom_task_id')

    resp = {
        'run_id': run_id,
        "generated_xcom": {}
    }

    session = Session()
    for _key in params.keys():
        if _key.startwith(prefix_text):
            try:
                _args = {
                    "key": _key.replace(prefix_text, ""),
                    "value": json.dumps(params(_key)).encode('UTF-8'),
                    "execution_date": execution_date,
                    "task_id": custom_task_id,
                    "dag_id": dag_id,
                }
                session.add(XCom( **_args ))
                
                resp[_key] = _args.update({"value": params(_key)})

            except Exception as e:
                print('err: {}'.format(str(e)))

    session.commit()

    
    # retrive whaat was just stored
    session = Session()

    xcomlist = (
        session.query(XCom)
        .filter_by(dag_id=dag_id, task_id=task_id, execution_date=execution_date)
        .all()
    )

    attributes = []
    for xcom in xcomlist:
        if not xcom.key.startswith('_'):
            attributes.append((xcom.key, xcom.value))

                
    _xcoms = []
    try:
        _xcoms = session.query(XCom).filter(
            XCom.dag_id == dag_id,
            XCom.task_id == custom_task_id,
            XCom.execution_date = execution_date).all()

    except Exception as e:
        print('_xcoms err: {}'.format(str(e)))
        raise AirflowException(e)

    session.commit()
    

    for x in _xcoms:
        if not x.key.startswith('_'):
            resp["generated_xcom"][x.key] = str(x.value)

    return resp

def _tapd_enhanced_trigger_dag(
    dag_id: str,
    url_params: dict,
    dag_bag: DagBag,
    run_id: str | None = None,
    conf: dict | str | None = None,
    execution_date: datetime | None = None,
    replace_microseconds: bool = True,
) -> list[DagRun | None]:
    """Triggers DAG run.

    :param dag_id: DAG ID
    :param dag_bag: DAG Bag model
    :param run_id: ID of the dag_run
    :param conf: configuration
    :param execution_date: date of execution
    :param replace_microseconds: whether microseconds should be zeroed
    :return: list of triggered dags
    """
    dag = dag_bag.get_dag(dag_id)  # prefetch dag if it is stored serialized

    if dag is None or dag_id not in dag_bag.dags:
        raise DagNotFound(f"Dag id {dag_id} not found")

    execution_date = execution_date if execution_date else timezone.utcnow()

    if not timezone.is_localized(execution_date):
        raise ValueError("The execution_date should be localized")

    if replace_microseconds:
        execution_date = execution_date.replace(microsecond=0)

    if dag.default_args and 'start_date' in dag.default_args:
        min_dag_start_date = dag.default_args["start_date"]
        if min_dag_start_date and execution_date < min_dag_start_date:
            raise ValueError(
                f"The execution_date [{execution_date.isoformat()}] should be >= start_date "
                f"[{min_dag_start_date.isoformat()}] from DAG's default_args"
            )
    logical_date = timezone.coerce_datetime(execution_date)

    data_interval = dag.timetable.infer_manual_data_interval(run_after=logical_date)
    run_id = run_id or dag.timetable.generate_run_id(
        run_type=DagRunType.MANUAL, logical_date=logical_date, data_interval=data_interval
    )
    dag_run = DagRun.find_duplicate(dag_id=dag_id, execution_date=execution_date, run_id=run_id)

    if dag_run:
        raise DagRunAlreadyExists(
            f"A Dag Run already exists for dag id {dag_id} at {execution_date} with run id {run_id}"
        )

    run_conf = None
    if conf:
        run_conf = conf if isinstance(conf, dict) else json.loads(conf)

        
    ### custom translation
    # only one set of xcom pairs will be created for the parent dag instance
    resp = _params_to_xcom(dag_id, run_id, execution_date, url_params)

        
    dag_runs = []
    dags_to_run = [dag] + dag.subdags
    for _dag in dags_to_run:
        dag_run = _dag.create_dagrun(
            run_id=run_id,
            execution_date=execution_date,
            state=DagRunState.QUEUED,
            conf=run_conf,
            external_trigger=True,
            dag_hash=dag_bag.dags_hash.get(dag_id),
            data_interval=data_interval,
        )
        dag_runs.append(dag_run)

    return dag_runs, resp


def tapd_enhanced_trigger_dag(
    dag_id: str,
    url_params: dict,
    run_id: str | None = None,
    conf: dict | str | None = None,
    execution_date: datetime | None = None,
    replace_microseconds: bool = True,
) -> DagRun | None:
    """Triggers execution of DAG specified by dag_id

    :param dag_id: DAG ID
    :param url_params: key/values in url
    :param run_id: ID of the dag_run
    :param conf: configuration
    :param execution_date: date of execution
    :param replace_microseconds: whether microseconds should be zeroed
    :return: first dag run triggered - even if more than one Dag Runs were triggered or None
    """
    dag_model = DagModel.get_current(dag_id)
    if dag_model is None:
        raise DagNotFound(f"Dag id {dag_id} not found in DagModel")

    dagbag = DagBag(dag_folder=dag_model.fileloc, read_dags_from_db=True)
    triggers, resp = _tapd_enhanced_trigger_dag(
        dag_id=dag_id,
        url_params=url_params,
        dag_bag=dagbag,
        run_id=run_id,
        conf=conf,
        execution_date=execution_date,
        replace_microseconds=replace_microseconds,
    )

    return (triggers[0] if triggers else None, resp)


