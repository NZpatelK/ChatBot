from google.oauth2 import service_account
from google.api_core.exceptions import InvalidArgument
import dialogflow_v2beta1
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'package.json'

DIALOGFLOW_PROJECT_ID = 'karanassistant-ushv'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

text_to_be_analyzed = "Hello!"

session_client = dialogflow_v2beta1.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

text_input = dialogflow_v2beta1.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
query_input = dialogflow_v2beta1.types.QueryInput(text=text_input)

try:
    response = session_client.detect_intent(session=session, query_input=query_input)
except InvalidArgument:
    raise

print("Query text:", response.query_result.query_text)
print("Detected intent:", response.query_result.intent.display_name)
print("Detected intent confidence:", response.query_result.intent_detection_confidence)
print("Fulfillment text:", response.query_result.fulfillment_text)
