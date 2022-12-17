from twilio.rest import Client
account_sid = 'AC0b246b4a64109de691920c953996cded'
auth_token = 'f614d44a7a6552064bd1bce30f6aa879'
client = Client(account_sid, auth_token)

call = client.calls.create(
                            twiml="<Response><Gather action=\"/gather_results\" digits=\"1\"><Say>Garbage Detected... Garbage Detected... Garbage detected</Say></Gather></Response>",
                              from_='+13853967299',
                              to='+919731332758'
                          )

print(call.sid)