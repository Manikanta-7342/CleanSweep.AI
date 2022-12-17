from twilio.rest import Client
from twilio.rest import Client
import datetime


def sms(t1,lat,lon):
  sid = 'AC0b246b4a64109de691920c953996cded'
  auth = 'f614d44a7a6552064bd1bce30f6aa879'
  # geolocator = Nominatim(user_agent="geoapiExercises")
  # location = geolocator.reverse(str(lat) + "," +str(lon))
  # address = location.raw['address']
  google_maps_link = f"https://www.google.com/maps/search/?api=1&query={float(lat)},{float(lon)}"
  # address = list(address.values())
  # address = ",".join(address)
  case = "Attention Required!!"
  cl = Client(sid, auth)
  cl.messages.create(body=f"{case}\nScrap detected Time: {t1}\nLocation: {google_maps_link}", from_ = '+13853967299', to = '+919731332758')

def whatsapp1(lat, lon):
  account_sid = 'AC0b246b4a64109de691920c953996cded'
  auth_token = 'f614d44a7a6552064bd1bce30f6aa879'
  client = Client(account_sid, auth_token)

  message = client.messages.create(
    body='Hello there!',
    persistent_action=[f'geo:{lat},{lon}|375 Beale St'],
    from_='whatsapp:+1415523-8886',
    to='whatsapp:+919731332758'
  )

  print(message.sid)

ct = datetime.datetime.now()
lat=12.9719
lon=77.5937
sms(ct, lat, lon)
whatsapp1(lat,lon)