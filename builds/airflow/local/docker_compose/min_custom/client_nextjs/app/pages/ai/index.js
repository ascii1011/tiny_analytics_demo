import Link from 'next/link';
import styles from '../../styles/Home.module.css';
import axios from 'axios';


function AIfeature(props) {
  const base = "";
  const triggerDag = async (dagId, runId, executionDate, conf) => {
    try {
    const response = await axios.post(`http://min_custom_airflow_1/api/v1/dags/${dagId}/dag_runs`, {
        run_id: runId,
        conf: conf,
        execution_date: executionDate
    });
    console.log(response.data);
    } catch (error) {
    console.error(error);
    }
  };

  const handleClick = () => {
    triggerDag('example_02_custom', 'run_1', '2022-01-01T00:00:00', { key: 'value' });
  };

  return (
    <div className={styles.container}>
      <main className={styles.main}>
        <h1 className={styles.title}>
          AI builder
        </h1>

          <button onClick={handleClick}>Trigger DAG</button>
        </main>
    </div>
  )
}
    

export default AIfeature;

