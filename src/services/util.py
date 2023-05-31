import json
import datetime
class Util:
    
    def __json_default(self,value):
        """ Convert a specific object to dict 
        
        Args:
            object value: a object to convert to dict
        """
        if isinstance(value, datetime.date):
            return dict(year=value.year, month=value.month, day=value.day)
        else:
            return value.__dict__

    def object_to_json(self, entity):
        return json.dumps(entity,ensure_ascii=False,default = lambda o: self.__json_default(o), sort_keys=True, indent=4).encode('utf-8')

    def object_to_dict(self, entity):
        """ Convert an object to dict 
        
        Args:
            object entity: a entity to convert to dict
        """
        json_entity = self.object_to_json(entity)
        return json.loads(json_entity)
