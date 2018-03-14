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

def sendMsgTwoHosts(twoHosts,msgBody):
    client = Client(account_sid, auth_token)

    # TODO : later, have cell_numbers in names.txt and get cell-num of boths hosts, and send msg to both hosts (default include Shreyans)
    # host_1 = twoHosts[0].split(' ')
    # host_2 = twoHosts[1].split(' ')

    message = client.messages.create(to  = toNumber,
                                    from_= fromNumber,
                                    body = msgBody)

    print(message.sid)

#sendMsgTwoHosts(['Shreyans', 'Shrek'], "Hello from BytePython!")
'''
 Resources :
    Twilio Messaging API : https://www.twilio.com/docs/api/messaging

'''