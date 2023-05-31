# Extract Component that access Microsft Azure DevOPS

## 🚀 Goal

A example of Extract Component that access Microsft Azure DevOPS via a [ASA](https://anonymous.4open.science/r/AzureDevOps-1F18/README.md).

## ⚙️ Requirements

1. Docker Compose
2. Python

## Install

Performs the following command:
```
cd ./src
pip install -r requirements.txt
```

## 🔧 Run

First, execute the infrastruture with database, Kafka and Debezium in [The Band Infrastruture](https://github.com/paulossjunior/base-infrastructure-the-band)

Second, and, Last, execute the following commands: 

```bash
cd ./src

docker-compose up
```

## 🛠️ Stack

1. [Apache Beam](https://beam.apache.org/)
2. [Python](https://www.python.org/)


