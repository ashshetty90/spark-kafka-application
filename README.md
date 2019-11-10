# Spark Kafka Streaming Application


![FLOW_DIAGRAM](https://github.com/ashshetty90/spark-kafka-application/blob/master/images/flow-diagram.jpg "FLOW_DIAGRAM")
# Overview:
This project is a dockerised pub sub based application written in python to publish data using Kafka and consume/aggregate data using the Spark processing framework.

# Requirement:

1) A dockerised kafka application that produces user behaviour data and pushes into its producer.
2) A dockerised pyspark based application that could read real time data from a kafka producer and perform aggregations on the raw data and perform aggregations real time.

# Architecture:
The Architecture involves the following tech stack.
- Kafka v1.4.7
- Spark v2.4.4
- Python v3.7.2
- Docker

# What can be done better

1) Push the data into a persistant storage like InfluxDB/MySQl/PostGres.
2) Stream real time aggregations from persistant storage systems into dashboards built in Grafana.


# How to run this application
```sh
### Clone the repository [https://github.com/ashshetty90/spark-kafka-application.git]

Running the Kafka Producer 
### After cloning the repository, run the below command in the root directory of the project. Make sure docker is installed on your machine.
$ docker-compose up -d
### The above command will run the kafka producer and the spark consumer inside a docker container.

```

# Screenshots
### Sample Outputs
![KAFKA PRODUCER](https://github.com/ashshetty90/spark-kafka-application/blob/master/images/kafka-producer.png "KAFKA PRODUCER")

![SPARK CONSUMER](https://github.com/ashshetty90/spark-kafka-application/blob/master/images/output.png "SPARK CONSUMER")

