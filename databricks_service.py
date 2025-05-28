# logger
# inspired by https://github.com/databricks/databricks-sdk-py/issues/164 and https://github.com/alexott/databricks-playground/blob/main/azure-mi-in-py-sdk/azure-mi-in-py-sdk.py
from azure.identity import ManagedIdentityCredential
from databricks.sdk import WorkspaceClient
from databricks.sdk.credentials_provider import CredentialsStrategy
import os

class AzureIdentityCredentialsStrategy(CredentialsStrategy):
    def auth_type(self):
        return 'azure-mi'
    
    def __init__(self, client_id):
        self.client_id = client_id

    def __call__(self, cfg):
        mi_credential = ManagedIdentityCredential(client_id=self.client_id)
        
        def inner():
            token = mi_credential.get_token("2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default")
            return {'Authorization': f"Bearer {token.token}"}
        
        return inner

def get_workspace_client():
    if not hasattr(get_workspace_client, "_workspace_client"):
        host = os.getenv("DATABRICKS_HOST")
        client_id = os.getenv("AZURE_CLIENT_ID")
       
        workspace_client = WorkspaceClient(
            host=host, 
            credentials_strategy=AzureIdentityCredentialsStrategy(client_id=client_id))
        get_workspace_client._workspace_client = workspace_client
    
    return get_workspace_client._workspace_client

def get_catalog():
    return list(get_workspace_client().catalogs.list())[0].as_dict()