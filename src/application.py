import apache_beam as beam
from beam_nuggets.io import kafkaio
from decouple import config
from services.transform import Transform
import logging

logging.basicConfig(level=logging.INFO)


consumer_config = {"topic": config('TOPIC'),
                   "bootstrap_servers": config('SERVERS'),
                   "group_id": config('GROUP_ID'),}

print (consumer_config)

with beam.Pipeline(runner='DirectRunner') as pipeline:


    credential = (pipeline|  "Reading messages from Kafka"  >> kafkaio.KafkaConsume(
                                        consumer_config=consumer_config))

    credential | "Extract Data and Send To Kafka" >> Transform()

    


    