'''
This acts like a client
'''

from twilio.rest import Client

myAccSid    = "BBBBBBBB"
myAccToken  = "AAAAAAAA"
fromNumber  = "yyy"
smulkutk    = "xxx"
toNumber    = smulkutk

account_sid = myAccSid
auth_token  = myAccToken

client = Client(account_sid, auth_token)

message = client.messages.create(
    to  =toNumber,
    from_=fromNumber,
    body="Hello from BytePython!")

print(message.sid)
