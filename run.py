# /usr/bin/env python

'''
This acts like a server
'''
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
# My common methods
from commonMethods  import *

# This can be any service/product/customer care/emergency services number
# twilioNumber    = "yyy"
# customerNumber  = "xxx"

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages and create a conversation"""
    txMsgBody       = ""

    rxFromNumber    = request.values.get('From')
    rxMsgBody       = request.values.get('Body')
    rxMsgBody       = rxMsgBody.capitalize()

    if any( [rxMsgBody == "Yes", rxMsgBody == "Y"] ):
        txMsgBody += "Great! "
    elif any( [rxMsgBody == "No", rxMsgBody == "N"] ):
        txMsgBody += "Okay. I'll check with next in line"
    else:
        txMsgBody += "Do you mind getting with Shrek? "

    # Start our response
    resp = MessagingResponse()

    # Add a message
    txMsgBody += greetingString('end')
    resp.message(txMsgBody)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)