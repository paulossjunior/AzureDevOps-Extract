from apache_beam.transforms import PTransform
import apache_beam as beam
from .fn import FnExtract, FnTuple
from beam_nuggets.io import kafkaio
from decouple import config


class Transform(PTransform):
    def __init__(self):
        self.application = "msazuredevops"
        self.entities = ['project','interaction','team', 'teammember','workitem', 'backlog', 'workitemtype']
        self.producer_config = {'bootstrap.servers': config('SERVERS')}
        
    def expand(self, pcoll):
        result = None
        for entity in self.entities:
            result = (
                pcoll
                | "Retrieve {}".format(entity) >>beam.ParDo(FnExtract(function_name=entity))
                | "Transform in Tuple {}".format(entity) >>beam.ParDo(FnTuple())
                | "Sending  {} to Kafka".format(entity) >> kafkaio.KafkaProduce(topic="application.{}.{}".format(self.application,entity),servers=config('SERVERS'))
                
            )
        return result


