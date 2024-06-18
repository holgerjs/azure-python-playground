##################################################
# Script to create an Azure Cognitive Services Account of type "Document Intelligence"
##################################################

# Import required modules.
import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient

# Define Variables
SUBSCRIPTION_ID = os.environ["AZURE_SUBSCRIPTION_ID"]
RESOURCE_GROUP_NAME = "rg-sample-eus-001"
COGNITIVESERVICES_ACCOUNT_NAME = "cogsvc-ai-document-intelligence-eus-001"
COGNITIVESERVICES_ACCOUNT_KIND = "FormRecognizer"
LOCATION = "eastus"

# Acquire a credential object using DevaultAzureCredential.
credential = DefaultAzureCredential()

# Create client
cognitiveservices_client = CognitiveServicesManagementClient(
    credential=credential,
    subscription_id=SUBSCRIPTION_ID
)

# Create Account
cognitiveservices_account = cognitiveservices_client.accounts.begin_create(
    resource_group_name=RESOURCE_GROUP_NAME, 
    account_name=COGNITIVESERVICES_ACCOUNT_NAME,
    account={
        "location": LOCATION,
        "sku": {
            "name": "F0",
            "tier": "Free"
        },
        "identity": {
            "type": "SystemAssigned"
        },
        "kind": COGNITIVESERVICES_ACCOUNT_KIND,
        "properties": {
            "customSubDomainName": COGNITIVESERVICES_ACCOUNT_NAME,
            "publicNetworkAccess": "Enabled"
        }
    }
)

print(cognitiveservices_account.result())