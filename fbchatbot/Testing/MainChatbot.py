import fbchat
from fbchat import Client, log
from fbchat.models import *
import re

fbchat._util.USER_AGENTS = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')

class KaranAssistant(Client):


    def onMessage(self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        # Mark message as read
        self.markAsRead(author_id)

        # Print info on consoleka
        log.info("Message {} from {} in {}".format(message_object, thread_id, thread_type))


        # Message Text
        msgText = message_object.text

        reply = 'hello world'

        # Send message
        if author_id != self.uid:
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

        # Mark message as delivered
        self.markAsDelivered(author_id, thread_id)

name = input("Name: ")
password = input("pass: ")

# Create an object of our class, enter your email and password for facebook.
client = KaranAssistant(name, password)

# Listen for new message
client.listen()

