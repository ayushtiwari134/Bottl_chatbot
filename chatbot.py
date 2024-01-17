from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio import *
import requests

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def reply():
    
    incoming_msg = request.form.get('Body').lower()
    mobile_no = request.form.get('From')
    response = MessagingResponse()
    print(incoming_msg)
    message=response.message()
    responded = False
    words = incoming_msg.split('@')
    if "hello" in incoming_msg:
        reply = "Welcome to BMTC ticket bot"
        reply = "Hello! I am your ticket-bot and I will assist you in purchasing bus tickets, bus passes and tracking live location of busses. Type your queries or choose one of the options below for me to assist you"
        send_message(mobile_no,reply)
        responded = True
        return (reply)
        
    if len(words) == 2 and "Bus tickets" in incoming_msg:
        reminder_string = "Would you like to enter your bus stop or bus number"
        send_message(mobile_no,reminder_string)
        responded = True

        if len(words)==2 and "Bus stop" in incoming_msg:
            reminder_string = "Please enter the source stop name choose one of the following options or type your query"
            send_message(mobile_no,reminder_string)
            responded = True
            
            if len(words)==3 and "Type stop name" in incoming_msg:
                reminder_string = "Please type your stop name"
                send_message(mobile_no,reminder_string)
                responded = True


        elif len(words)==2 and "Bus Number" in incoming_msg:
            reminder_string="Please enter your bus number"
            send_message(mobile_no,reminder_string)
            responded= True 

def send_message(mobile_no,message):
    url= "https://api.twilio.com/2010-04-01/Accounts/AC68dece1aeedd5877f9b238a3cdfca6d0/Messages.json"

    payload = {
        "To": mobile_no,
        "From": "+14155238886",
        "Body": message,
    }

    headers = {
        'Authorization' : 'Authorization: Basic QUM2OGRlY2UxYWVlZGQ1ODc3ZjliMjM4YTNjZGZjYTZkMDowMzQ5MjcxODYxMzYwMjZkMzk0ZTRjYjM2Y2RhY2JlZg=='
    }
    response = requests.request("POST", url, headers=headers, data = payload)

    
if __name__ == "__main__":
    app.run(debug=True)