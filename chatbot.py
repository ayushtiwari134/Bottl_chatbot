from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio import *


app = Flask(__name__)
count=0
from twilio.rest import Client

account_sid = 'AC68dece1aeedd5877f9b238a3cdfca6d0'
auth_token = '034927186136026d394e4cb36cdacbef'
client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   body='',
#   to='whatsapp:+917439042931'
# )

# print(message.sid)

@app.route("/sms", methods=['POST'])
def reply():
    
    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    print(incoming_msg)
    message=response.message()
    responded = False
    words = incoming_msg.split('@')
    if "hello" in incoming_msg:
        reply = "Welcome to BMTC ticket bot"
        reply = "Hello! I am your ticket-bot and I will assist you in purchasing bus tickets, bus passes and tracking live location of busses. Type your queries or choose one of the options below for me to assist you"
        message.body(reply)
        responded = True
        
        
    if len(words) == 2 and "Bus tickets" in incoming_msg:
        reminder_string = "Would you like to enter your bus stop or bus number"
        message.body(reminder_string)
        responded = True

        if len(words)==2 and "Bus stop" in incoming_msg:
            reminder_string = "Please enter the source stop name choose one of the following options or type your query"
            message.body(reminder_string)
            responded = True
            
            if len(words)==3 and "Type stop name" in incoming_msg:
                reminder_string = "Please type your stop name"
                message.body(reminder_string)
                responded = True


        elif len(words)==2 and "Bus Number" in incoming_msg:
            reminder_string="Please enter your bus number"
            message.body(reminder_string)
            responded= True 
        
if __name__ == "__main__":
    app.run(debug=True)