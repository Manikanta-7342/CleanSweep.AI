from twilio.rest import Client
# def sms(lan,lat):
#     sid='AC0b246b4a64109de691920c953996cded'
#     auth='39d2f1d67835d7f25733773c96ef402c'
#
#     cl= Client(sid,auth)
#     cl.messages.create(body='Chutya sumne irale',PersistentAction=geo:{lan},{lat},from_='+13853967299',to='+919731332758')
#
# def whatsapp1(lan,lat):
#     account_sid = 'AC0b246b4a64109de691920c953996cded'
#     auth_token = '39d2f1d67835d7f25733773c96ef402c'
#     client = Client(account_sid, auth_token)
#
#     message = client.messages.create(
#                                   body='Hello there!',
#                                   persistent_action=[f'geo:{lan},{lat}|375 Beale St'],
#                                   from_='whatsapp:+1415523-8886',
#                                   to='whatsapp:+919731332758'
#                               )
#
#     print(message.sid)

# import requests
# url = "https://www.fast2sms.com/dev/bulk"
# payload = "sender_id=FSTSMS&message=test&language=english&route=p&numbers=9731332758"
# headers = {
# 'authorization': "N49diu0Yx2Ue1mXslqr3kH5ZvRKOcBfQTFzg7LJEjM6GCotWDy8mjrSLwXx5YyzbkvNsVKJW0eO7GAMB",
# 'Content-Type': "application/x-www-form-urlencoded",
# 'Cache-Control': "no-cache",
# }
# response = requests.request("POST", url, data=payload, headers=headers)
# print(response.text)
#
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse, Gather

# app = Flask(__name__)
#
#
# @app.route("/voice", methods=['GET', 'POST'])
# def voice():
#     """Respond to incoming phone calls with a menu of options"""
#     # Start our TwiML response
#     resp = VoiceResponse()
#
#     # Start our <Gather> verb
#     gather = Gather(num_digits=1)
#     gather.say('For sales, press 1. For support, press 2.')
#     resp.append(gather)
#
#     # If the user doesn't select an option, redirect them into a loop
#     resp.redirect('/voice')
#
#     return str(resp)
#
# if __name__ == "__main__":
#     app.run(debug=True)

# account_sid = 'AC0b246b4a64109de691920c953996cded'
# auth_token = '39d2f1d67835d7f25733773c96ef402c'
# client = Client(account_sid, auth_token)
#
# call = client.calls.create(
#                             twiml="<Response><Gather action=\"/gather_results\" digits=\"1\"><Say>Garbage Detected... Garbage Detected... Garbage detected</Say></Gather></Response>",
#                               from_='+13853967299',
#                               to='+919731332758'
#                           )
#
# print(call.sid)
client = vonage.Client(
    application_id="8184ce33",
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

voice = vonage.Voice(client)

response = voice.create_call({
    'to': [{'type': 'phone', 'number': "919731332758"}],
    'from': {'type': 'phone', 'number': "919731332758"},
    'ncco': [{'action': 'talk', 'text': 'This is a text to speech call from Nexmo'}]
})

print(response)