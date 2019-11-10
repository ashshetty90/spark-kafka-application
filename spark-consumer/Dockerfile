FROM bde2020/spark-submit:2.4.4-hadoop2.7

LABEL maintainer="Ashish Shetty ashshetty90@gmail.com>"

COPY / .

ENV SPARK_MASTER_NAME spark-master
ENV SPARK_MASTER_PORT 7077
ENV SPARK_SUBMIT_ARGS "--driver-memory 4G --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0 --py-files /driver.py"
ENV SPARK_APPLICATION_PYTHON_LOCATION /driver.py
ENV SPARK_APPLICATION_ARGS ""

COPY submit.sh /
CMD ["/bin/bash", "/submit.sh"]