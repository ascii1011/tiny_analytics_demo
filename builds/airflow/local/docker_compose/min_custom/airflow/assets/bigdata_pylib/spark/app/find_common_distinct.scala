//find_common.scala

import org.apache.spark.sql.{DataFrame,SparkSession}
import spark.implicits._
import org.apache.spark.sql.functions
import org.apache.spark.sql.Row
import org.apache.spark.sql.types.{StructField,StructType,IntegerType,LongType}

object App {
    def main(file1: String, file2: String): Unit = {
        val spark = SparkSession.builder()
            .master("local[1]")
            .appName("FindCommonDistinct")
            .getOrCreate();

        val df1 = load_data_from_file(file1, "col")
        val df2 = load_data_from_file(file2, "col")

        // intersection 
        val df_inter = df1.select("col").intersect(df2.select("col"))
        println(df_inter.count)
    }


    def load_data_from_file(filename: String, col_id: String): DataFrame = {
        // read in first file
        val rdd = sc.textFile(filename).collect()

        // for better performance vs available resources
        val distRdd = sc.parallelize(rdd)

        val df = distRdd.toDF(col_id)

        df
    }

}
