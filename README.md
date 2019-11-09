# Spark Kafka Streaming Application


![FLOW_DIAGRAM](https://github.com/ashshetty90/spark-kafka-application/blob/master/images/flow-diagram.jpg "FLOW_DIAGRAM")
# Overview:
This project is a pub sub based application written in python to publish data using Kafka and consume/aggregate data using the Spark processing framework.

# Requirement:

1) A dockerised kafka application that produces user behaviour data and pushes into its producer.
2) A python spark based command line application that could read real time data from a kafka producer and perform aggregations on the raw data and perform aggregations real time.

# Architecture:
The Architecture involves the following tech stack.
- Kafka v1.4.7
- Spark v2.4.4
- Python v3.7.2
- Docker

# What can be done better

1) Dockerise the Spark application.
2) Push the data into a persistant storage like InfluxDB/MySQl/PostGres.
3) Stream real time aggregations from persistant storage systems into dashboards built in Grafana.


# How to run this application
```sh
### Clone the repository [https://github.com/ashshetty90/spark-kafka-application.git]

1) Running the Kafka Producer 
### After cloning the repository, run the below command in the root directory of the project. Make sure docker is installed on your machine.
$ docker-compose up -d
### The above command will run the kafka producer inside a docker container and will expose it at `localhost:9093`


2) Running the Spark Streaming Consumer Application
### Please note that this set-up is valid only for Mac OS machines

### Firstly, make sure you have installed home brew on your local machine . If not please use the below command to install it:
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Python3 needs xcode as well so installing it
$ xcode-select --install
### Some basic checks
$ brew doctor
### Now lets move to installing the latest python on the machine :
$ brew install python3
### Running the below command will return you the latest python3 version
$ python3 --version 

### Moving on to installing spark in the local machine 

You would need java8 installed on your machine, I have installed openjdk8 using:

$ brew cask install homebrew/cask-versions/adoptopenjdk8

Install apache-spark
$ brew install apache-spark

### In case you have more than one version of python installed in your machine, make sure you enforce python3 as the default python version for your py-spark applications by adding :

export PYSPARK_PYTHON=/usr/local/bin/python3  in the .bash_profile or /usr/local/Cellar/apache-spark/2.4.4/libexec/conf/spark-env.sh.template (Or spark-env.sh whichever is available)

### Install dependecies from Pipfile
$ pipenv install


### Running the application

$ /usr/local/Cellar/apache-spark/2.4.4/bin/spark-submit --driver-memory 4G --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0   --py-files <complete path to the driver.py file>/driver.py <complete path to the driver.py file>/driver.py

For Ex:
$ /usr/local/Cellar/apache-spark/2.4.4/bin/spark-submit --driver-memory 4G --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0   --py-files /User/Workspace/app/driver.py /User/Workspace/app/driver.py

```

# Screenshots
### Sample Outputs
![KAFKA PRODUCER](https://github.com/ashshetty90/spark-kafka-application/blob/master/images/kafka-producer.png "KAFKA PRODUCER")

![SPARK CONSUMER](https://github.com/ashshetty90/spark-kafka-application/blob/master/images/output.png "SPARK CONSUMER")

