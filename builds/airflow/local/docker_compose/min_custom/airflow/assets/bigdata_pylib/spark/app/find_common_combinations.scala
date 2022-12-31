//find_common_combinations.scala

import org.apache.spark.sql.{DataFrame,SparkSession}
import spark.implicits._
import org.apache.spark.sql.functions
import org.apache.spark.sql.Row
import org.apache.spark.sql.types.{StructField,StructType,IntegerType,LongType}

object App {
    def main(file1: String, file2: String): Unit = {
        val spark = SparkSession.builder()
            .master("local[1]")
            .appName("FindCommonCombinations")
            .getOrCreate();

        val df1 = load_data_from_file(file1, "col")
        val df2 = load_data_from_file(file2, "col")

        // find intersection 
        val df_inter = df1.select("col").intersect(df2.select("col"))

        // break down counts per string per df
        val df_test1 = df1.groupBy("col").count.join(df_inter, "col")
        val df_test2 = df2.groupBy("col").count.join(df_inter, "col")
            .withColumnRenamed("count", "count2")
        
        // merge and calc combos
        val merged_df = df_test1.join(df_test2, Seq("col"), "full")
            .groupBy("col")
            .agg(sum("count") * sum("count2") as "sum")
            .drop("col")

        // agg combo sums
        println(merged_df.agg(sum("sum")).first.get(0))

    }


    def load_data_from_file(filename: String, col_id: String): DataFrame = {
        val rdd = sc.textFile(filename).collect()

        // for better performance vs available resources
        val distRdd = sc.parallelize(rdd)

        val df = distRdd.toDF(col_id)

        df
    }

}
