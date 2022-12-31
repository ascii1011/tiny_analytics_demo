
from pyspark.sql import SQLContext, SparkSession

def main():
    print('pyspark_app_test:')
    spark = SparkSession.builder.appName("MyApp").getOrCreate()
    print('context')
    sc = spark.sparkContext

    print('log level')
    sc.setLogLevel("ERROR")

    print('--end--')

if __name__ == "__main__":
    main()

