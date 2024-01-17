from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio import *
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from twilio.rest import Client

# Twilio API credentials
account_sid = 'AC68dece1aeedd5877f9b238a3cdfca6d0'
auth_token = '034927186136026d394e4cb36cdacbef' # Include the country code, e.g., +14155552671
twilio_whatsapp_number = '+14155238886'
# Create a Twilio client
client = Client(account_sid, auth_token)

# Send a message


@app.route("/sms", methods=['POST'])

def sms():
    
# Get incoming message and sender's phone number
    incoming_msg = request.form.get('Body', '').lower()
    sender_phone_number = request.form.get('From', '')
    response = MessagingResponse()
    print(incoming_msg)
    responded = False
    # words = incoming_msg.split('@')
    if "hello" in incoming_msg:
        reply = "Welcome to BMTC ticket bot \nHello! I am your ticket-bot and I will assist you in purchasing bus tickets, bus passes and tracking live location of busses. Type your queries or choose one of the options below for me to assist you.\nPlease enter 'bus tickets' to continue"
        response.message(reply)
        # send_message(response,reply)
        responded = True
        return('hello success')
        
    elif "bus tickets" in incoming_msg:
        reminder_string = "Would you like to enter your bus stop or bus number"
        response.message(reminder_string)
        responded = True
        return('bus tickets success')

    elif  "bus stop" in incoming_msg:
        reminder_string = "Please enter the source stop name choose one of the following options or type your query"
        response.message(reminder_string)
        responded = True
        return('bus stop success')
            
    elif  "type stop name" in incoming_msg:
        reminder_string = "Please type your stop name"
        response.message(reminder_string)
        stop_name = request.form.get('Body').lower()
        responded = True
        return('stop name success')

    elif  "bus number" in incoming_msg:
        reminder_string="Please enter your bus number"
        response.message(reminder_string)
        bus_number = request.form.get('Body').lower()
        responded= True
        return('bus number success')

    else:
        reminder_string="Please enter a valid option"
        response.message(reminder_string)
        responded= True
        return('invalid option')

# def send_message(response,reply):
#     response.message("hi")
    
if __name__ == "__main__":
    app.run(debug=True)