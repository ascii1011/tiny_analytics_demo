

from pyspark import SparkContext
logFilepath = "file:////opt/scripts/wordcount.txt"  
sc = SparkContext("spark://192.168.231.132:7077", "first app")
logData = sc.textFile(logFilepath).cache()
numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))