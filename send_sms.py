'''
This acts like a client
'''

from twilio.rest import Client
# My common methods
from commonMethods  import *

# myAccSid    = "BBBBBBBB"
# myAccToken  = "AAAAAAAA"
# fromNumber  = "yyy"
# smulkutk    = "xxx"
# toNumber    = smulkutk

account_sid = myAccSid
auth_token  = myAccToken

client = Client(account_sid, auth_token)

message = client.messages.create(
    to  = toNumber,
    from_= fromNumber,
    body = "Hello from BytePython! Can you get Samosa tomorrow? Reply : YES(Y) OR NO(N)")

print(message.sid)

'''
 Resources :
    Twilio Messaging API : https://www.twilio.com/docs/api/messaging

'''