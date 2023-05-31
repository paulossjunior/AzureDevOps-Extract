import logging
from azuredevopsX import factories
logging.basicConfig(level=logging.INFO)
from .util import Util
import uuid

class Extract():
    """Abstract Class with the main function used to extract data application and save in a MongoDB"""

    def __init__(self):
        self.util = Util()
        self.instance = None
        
    def config (self, entity, personal_access_token, organization_url, organization_uuid,configuration_uuid) :

        

        self.personal_access_token = personal_access_token
        self.organization_url = organization_url
        self.organization_uuid = organization_uuid
        self.configuration_uuid = configuration_uuid
        
        extract = {
            
            'project': factories.ProjectFactory(personal_access_token=self.personal_access_token,
                                                        organization_url=self.organization_url),
            
            'interaction': factories.InteractionFactory(personal_access_token=self.personal_access_token,
                                                        organization_url=self.organization_url),
            
            'team': factories.TeamFactory(personal_access_token=self.personal_access_token,
                                                        organization_url=self.organization_url), 
            
            'teammember': factories.TeamMemberFactory(personal_access_token=self.personal_access_token,
                                                        organization_url=self.organization_url),
            
            'workitem': factories.WorkItemFactory(personal_access_token=self.personal_access_token,
                                                        organization_url=self.organization_url), 
            
            'backlog': factories.WorkItemFactory(personal_access_token=self.personal_access_token,
                                                        organization_url=self.organization_url), 
            'workitemtype': factories.WorkItemFactory(personal_access_token=self.personal_access_token,
                                                        organization_url=self.organization_url)
            }
        self.entity = entity
        self.instance = extract[self.entity]
        

    def do(self):
        """Main function to retrieve and save data in a MongoDB's collection
        
        Args:
            dict data: credentials (secret, url etc) to connect a application
        
        """
        try:
            logging.info("Start Retrieve Information")
            
            data_extracted = self.instance.get_all(today=False)  
                        
            logging.info("End Returning")

            data_transformed = []
            for data in data_extracted:
                
                data_dict = self.util.object_to_dict(data)
                data_dict['entity'] = self.entity
                data_dict['internal_uuid'] = str(uuid.uuid4())
                data_transformed.append (data_dict)

            return data_transformed
            
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)    


   