from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from user_data_processor import *


def get_raw_df(spark, schema, alias_value):
    """
            :param spark: spark session for the streaming app
            :param alias_value: The alias value for the clean data frame
            :return: raw spark dataframe from the kafka consumer
    """
    """
         Creating a consumer for the kafka prodcuer running inside a docker container 
         exposed at localhost:9093.
         Setting spark.streaming.receiver.maxRate
         as could not use default timestamp value available in streams
         as it was difficult to aggregate them.
         Setting scheduler mode as 'FAIR' to run multiple aggregations in a fair mechanism
    """
    return spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:9092") \
        .option("subscribe", "data-stream-analysis") \
        .option("startingOffsets", "earliest") \
        .option("spark.streaming.backpressure.enabled", True) \
        .option("spark.streaming.receiver.maxRate", "2") \
        .option("spark.scheduler.mode", "FAIR") \
        .load() \
        .selectExpr("CAST(value AS STRING)") \
        .select(from_json(col("value"), schema)) \
        .select("jsontostructs(value).*") \
        .alias(alias_value)


def get_spark_streaming_session():
    """
        :return: Returns a spark streaming object
    """
    spark = SparkSession \
        .builder \
        .master("local[2]") \
        .appName("Spark-Data-Processor") \
        .getOrCreate()

    sc = spark.sparkContext
    sc.setLogLevel("ERROR")
    return spark


def process_user_data(spark, user_schema, alias_value):
    """
        :param user_schema: schema which needs to applied on to the incoming data stream
        :param alias_value: The alias value for the clean data frame
        :return: None
    """
    df_clean = get_raw_df(spark, user_schema, alias_value)
    UserDataProcessor.get_gender_by_counts(df_clean).start()
    UserDataProcessor.get_country_by_counts(df_clean).start()


def start():
    spark = get_spark_streaming_session()
    process_user_data(spark, USER_SCHEMA, USER_ALIAS)
    spark.streams.awaitAnyTermination()


if __name__ == "__main__":
    """
    Entry point of the spark streaming application
    """
    start()
