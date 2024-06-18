import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest,AnalyzeResult

ENDPOINT = os.environ["DOCUMENT_INTELLIGENCE_ENDPOINT"]
KEY = os.environ["DOCUMENT_INTELLIGENCE_SUBSCRIPTION_KEY"]

document_url = "https://learn.microsoft.com/en-us/azure/synapse-analytics/machine-learning/media/tutorial-form-recognizer/receipt.png"

document_analysis_client = DocumentIntelligenceClient(
    endpoint=ENDPOINT,
    credential=AzureKeyCredential(
        key=KEY
    )
)

poller = document_analysis_client.begin_analyze_document(
    model_id="prebuilt-receipt",
    analyze_request=AnalyzeDocumentRequest(
        url_source=document_url
    )
)

result: AnalyzeResult = poller.result()

print(result.documents[0].doc_type)
print(result.documents[0].fields.get("MerchantName").value_string)
print(result.documents[0].fields.get("TransactionDate").value_date)
print(result.documents[0].fields.get("Total").get("valueCurrency"))