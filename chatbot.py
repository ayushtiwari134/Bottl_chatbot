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
# def send_whatsapp():
#     try:
#         # Get recipient phone number from the request data
#         recipient_phone_number = request.json.get('recipient_phone_number')
    
#         # Send a WhatsApp message
#         message = send_message(recipient_phone_number, 'Hello from Twilio!')
#     except Exception as e:
#         return jsonify({'status': 'error', 'error_message': str(e)})

def reply():
    
    incoming_msg = request.form.get('Body').lower()
    mobile_no = request.form.get('From')
    print(incoming_msg)
    responded = False
    words = incoming_msg.split('@')
    if "hello" in incoming_msg:
        reply = "Welcome to BMTC ticket bot"
        reply = "Hello! I am your ticket-bot and I will assist you in purchasing bus tickets, bus passes and tracking live location of busses. Type your queries or choose one of the options below for me to assist you. Please enter 'bus tickets' to continue"
        send_message(mobile_no,reply)
        responded = True
        return('hello success')
        
    elif "bus tickets" in incoming_msg:
        reminder_string = "Would you like to enter your bus stop or bus number"
        send_message(mobile_no,reminder_string)
        responded = True
        return('bus tickets success')

    elif  "bus stop" in incoming_msg:
        reminder_string = "Please enter the source stop name choose one of the following options or type your query"
        send_message(mobile_no,reminder_string)
        responded = True
        return('bus stop success')
            
    elif  "type stop name" in incoming_msg:
        reminder_string = "Please type your stop name"
        send_message(mobile_no,reminder_string)
        stop_name = request.form.get('Body').lower()
        responded = True
        return('stop name success')

    elif  "bus number" in incoming_msg:
        reminder_string="Please enter your bus number"
        send_message(mobile_no,reminder_string)
        bus_number = request.form.get('Body').lower()
        responded= True
        return('bus number success')

    else:
        reminder_string="Please enter a valid option"
        send_message(mobile_no,reminder_string)
        responded= True
        return('invalid option')

def send_message(mobile_no,message):
    
    message = client.messages.create(
            from_='whatsapp:' + twilio_whatsapp_number,
            body=message,
            to='whatsapp:' + mobile_no
        )
    
if __name__ == "__main__":
    app.run(debug=True)