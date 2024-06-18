######################################
# Create Resource Group
######################################

# Import required modules.
import os

# Define Variables and retrieve subscription ID from environment variable
RESOURCE_GROUP_NAME = "rg-sample-eus-001"
LOCATION = "eastus"
SUBSCRIPTION_ID = os.environ["AZURE_SUBSCRIPTION_ID"]

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Acquire a credential object using DevaultAzureCredential.
credential = DefaultAzureCredential()

# Obtain the management object for resources.
resource_client = ResourceManagementClient(
    credential=credential, 
    subscription_id=SUBSCRIPTION_ID
)

# Provision the resource group.
rg_result = resource_client.resource_groups.create_or_update(
    resource_group_name=RESOURCE_GROUP_NAME, 
    parameters={
        "location": LOCATION
    }
)