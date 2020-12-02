
import fbchat
from fbchat import Client, log
from fbchat.models import *
from google.api_core.exceptions import InvalidArgument
import dialogflow_v2beta1
from getpass import getpass
import os
import re

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'package.json'

DIALOGFLOW_PROJECT_ID = 'karanassistant-ushv'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

fbchat._util.USER_AGENTS = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')


def getRply(msg):
    session_client = dialogflow_v2beta1.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

    text_input = dialogflow_v2beta1.types.TextInput(text=msg, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow_v2beta1.types.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    return response.query_result.fulfillment_text

class KaranSAssistant(Client):

    def onMessage(self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        # Mark message as read
        self.markAsRead(author_id)

        # Print info on console
        log.info("Message {} from {} in {}".format(message_object, thread_id, thread_type))

        msgText = message_object.text

        if type(msgText) != str:
            msgText = "..."

        # print("\n\n\n\n" + msgText + " \n\n\n\n\n")

        reply = getRply(msgText)

        if "he will reach out" in reply:
            f = open("newSentence.txt", "a")
            f.write(msgText + "\n")
            f.close()

        # Send message
        if author_id != self.uid:
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

        # Mark message as delivered
        self.markAsDelivered(author_id, thread_id)


# Create an object of our class, enter your email and password for facebook.
client = KaranSAssistant("Username", getpass())

# Listen for new message
client.listen()
