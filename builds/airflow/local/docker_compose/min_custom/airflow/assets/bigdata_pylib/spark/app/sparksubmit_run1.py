
"""
```
> spark-submit --master 'local[*]' run1.py 2019-01-01 
```
"""
import logging
from pyspark.sql import SQLContext, SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T
import click
import datetime as dt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.argument("exec_date", required=True, type=click.DateTime(formats=["%Y-%m-%d"]))
def main(exec_date: dt.datetime):
    logger.info(f"Exec_date: {exec_date}")
    spark = SparkSession.builder.appName("MyApp").getOrCreate()
    sc = spark.sparkContext
    sc.setLogLevel("ERROR")
    schema = T.StructType(
        [
            T.StructField("id", T.LongType(), True),
            T.StructField("name", T.StringType(), True),
            T.StructField(
                "transactions",
                T.ArrayType(
                    T.StructType(
                        [
                            T.StructField("transaction-id", T.LongType(), True),
                            T.StructField("amount", T.LongType(), True),
                        ]
                    )
                ),
            ),
        ]
    )

    data_path = (
        "/Users/vascella/Codes/dask-playground/dask-tutorial/data/accounts.*.json.gz"
    )
    logging.info(f"Reading {data_path}")
    df = spark.read.json(data_path, schema=schema)
    df.printSchema()


if __name__ == "__main__":
    main()

