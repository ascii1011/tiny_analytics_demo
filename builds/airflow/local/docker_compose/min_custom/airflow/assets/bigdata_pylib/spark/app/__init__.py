

"""

idea sources: 
 - https://anant.us/blog/modern-business/airflow-and-spark-running-spark-jobs-in-apache-airflow/
 - https://anant.us/blog/modern-business/airflow-and-cassandra-writing-to-cassandra-from-airflow/
 - https://sparkbyexamples.com/spark/spark-sparkcontext/
 - https://www.programcreek.com/scala/org.apache.spark.SparkContext
 - https://www.projectpro.io/recipes/use-sparksubmitoperator-airflow-dag
 - 

"""


def spark_submit_op(debug=False):
    """
    # Running Spark application on standalone cluster
    ./bin/spark-submit \
    --class org.apache.spark.examples.SparkPi \
    --master spark://192.168.231.132:7077 \
    --deploy-mode cluster \
    --executor-memory 5G \
    --executor-cores 8 \
    /spark-home/examples/jars/spark-examples_versionxx.jar 80
    """
    pass

def py_spark_op(debug=False):
    """
    from pyspark import SparkContext
    logFilepath = "file:////home/hduser/wordcount.txt"  
    sc = SparkContext("local", "first app")
    logData = sc.textFile(logFilepath).cache()
    numAs = logData.filter(lambda s: 'a' in s).count()
    numBs = logData.filter(lambda s: 'b' in s).count()
    print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
    """
    pass