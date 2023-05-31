import apache_beam as beam
from .extract import Extract
import json
import uuid 
from .util import Util

class FnExtract(beam.DoFn):
   
   """ Abstract Function"""
   def __init__(self,function_name) -> None:

      super().__init__()
      self.application_entity = Extract()
      self.util = Util()
      self.function_name = function_name
      
      
   def process(self, element):
      
      data = json.loads(element[1])
         
      self.application_entity.config (
         entity = self.function_name,
         personal_access_token = data['secret'],
         organization_url = data['url'],
         organization_uuid = data['configuration_uuid'],
         configuration_uuid = data['organization_uuid']
      )
      
      result = self.application_entity.do()      
      return result
            
class FnTuple(beam.DoFn):

   def __init__(self) -> None:

      super().__init__()
      self.util = Util()
      
   def process(self, element):
      
      index = str(uuid.uuid4())
      element = json.dumps (element)
      
      return [(index,element)]
      