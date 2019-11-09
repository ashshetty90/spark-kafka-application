from pyspark.sql.types import StringType, StructType, StructField

USER_SCHEMA = StructType([StructField("id", StringType(), True),
                          StructField("first_name", StringType(), True),
                          StructField("last_name", StringType(), True),
                          StructField("email", StringType(), True),
                          StructField("gender", StringType(), True),
                          StructField("ip_address", StringType(), True),
                          StructField("date", StringType(), True),
                          StructField("country", StringType(), True)])

USER_ALIAS = "clean_user_data"


class UserDataProcessor:
    @staticmethod
    def get_country_by_counts(df_raw):
        """
                :param df_raw: The raw data frame from the kafka stream
                :return: The aggregated data frame for the counts by country for each streaming micro batch
            """
        return df_raw.groupBy("clean_user_data.country").count() \
            .alias("country_count").orderBy("country_count.count", ascending=False) \
            .writeStream \
            .format("console") \
            .outputMode("complete")

    @staticmethod
    def get_gender_by_counts(df_raw):
        """
        :param df_raw: The raw data frame from the kafka stream
        :return:  The aggregated data frame for the counts by gender for each streaming micro batch
        """
        return df_raw.groupBy("clean_user_data.gender").count() \
            .alias("gender_count").orderBy("gender_count.count", ascending=False) \
            .writeStream \
            .format("console") \
            .outputMode("complete")
