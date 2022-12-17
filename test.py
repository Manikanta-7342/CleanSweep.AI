import sys
from PIL import Image
import tensorflow as tf
import numpy as np
import cv2,geocoder
import os,smtplib
import time
import datetime
from twilio.rest import Client
import yagmail
from geopy.geocoders import Nominatim

tf.compat.v1.disable_eager_execution()


def sms(t1,lat,lon):
  sid = 'AC0b246b4a64109de691920c953996cded'
  auth = 'f614d44a7a6552064bd1bce30f6aa879'
  geolocator = Nominatim(user_agent="geoapiExercises")
  location = geolocator.reverse(str(lat) + "," +str(lon))
  address = location.raw['address']
  google_maps_link = f"https://www.google.com/maps/search/?api=1&query={float(lat)},{float(lon)}"
  address = list(address.values())
  address = ",".join(address)
  case = "Attention Required!!"
  cl = Client(sid, auth)
  cl.messages.create(body=f"{case}\nScrap detected Time: {t1}\nLocation: {google_maps_link}\nAddress: {address}", from_ = '+13853967299', to = '+919731332758')

def call(lat,lon):
  account_sid = 'AC0b246b4a64109de691920c953996cded'
  auth_token = 'f614d44a7a6552064bd1bce30f6aa879'
  client = Client(account_sid, auth_token)
  call = client.calls.create(twiml="<Response><Gather action=\"/gather_results\" digits=\"1\"><Say>Attention Required!! Garbage Detected... Garbage Detected... Garbage detected</Say></Gather></Response>",
    from_='+13853967299',
    to='+919731332758'
  )
  print(call.sid)

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

def email_generate(t1, t2, lattitude, longitude):
  geolocator = Nominatim(user_agent="geoapiExercises")
  #tval = t2 - t1
  Longitude = longitude
  Lattitude = lattitude
  location = geolocator.reverse(str(lattitude) + "," + str(Longitude))
  address = location.raw['address']
  google_maps_link = f"https://www.google.com/maps/search/?api=1&query={float(Lattitude)},{float(Longitude)}"
  from_address = "maniadishu7342@gmail.com"
  to_address = "nishank.satish@gmail.com"

  subject = "Test Email"
  case = "Attention Required!!"
  address = list(address.values())
  address = ",".join(address)
  html = f"<h1>{case}</h1> <h2> Address: </h2><h3>{address}</h3><h3><a href={google_maps_link}>Location on GoogleMaps</a></h3><h2>Scrap detected Time:</h2><h3>{t1}</h3>"
  # Connect to your Gmail account and send the email
  yag = yagmail.SMTP(from_address,"uuxfkicknbrtkxgx")
  contents=[html,yagmail.inline("./kill.jpg")]
  yag.send(to=to_address, subject=subject, contents=contents)
  print("Done")


def load_graph(model_file):
  graph = tf.Graph()
  graph_def = tf.compat.v1.GraphDef()

  with open(model_file, "rb") as f:
    graph_def.ParseFromString(f.read())
  with graph.as_default():
    tf.import_graph_def(graph_def)

  return graph

def read_tensor_from_image_file(file_name, input_height=299, input_width=299,
				input_mean=0, input_std=255):
  input_name = "file_reader"
  output_name = "normalized"
  file_reader = tf.io.read_file(file_name, input_name)
  if file_name.endswith(".png"):
    image_reader = tf.image.decode_png(file_reader, channels = 3,
                                       name='png_reader')
  elif file_name.endswith(".gif"):
    image_reader = tf.squeeze(tf.image.decode_gif(file_reader,
                                                  name='gif_reader'))
  elif file_name.endswith(".bmp"):
    image_reader = tf.image.decode_bmp(file_reader, name='bmp_reader')
  else:
    image_reader = tf.image.decode_jpeg(file_reader, channels = 3,
                                        name='jpeg_reader')
  float_caster = tf.cast(image_reader, tf.float32)
  dims_expander = tf.expand_dims(float_caster, 0);
  resized = tf.compat.v1.image.resize_bilinear(dims_expander, [input_height, input_width])
  normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
  sess = tf.compat.v1.Session()
  result = sess.run(normalized)

  return result


def load_labels(label_file):
  label = []
  proto_as_ascii_lines = tf.compat.v1.gfile.GFile(label_file).readlines()
  for l in proto_as_ascii_lines:
    label.append(l.rstrip())
  return label


file_name = "C:\\Users\\manik\\Downloads\\simple.png"
model_file = "files/retrained_graph.pb"
label_file = "files/retrained_labels.txt"
input_height = 224
input_width = 224
input_mean = 128
input_std = 128
input_layer = "input"
output_layer = "final_result"

graph = load_graph(model_file)
#"D:\\JIT\\garbage_detector_kaggle\\videos\\1 - Made with Clipchamp.mp4"
video_reader = cv2.VideoCapture("D:\\JIT\\garbage_detector_kaggle\\videos\\1 - Made with Clipchamp.mp4")
li=[]

try:
  c=2
  while True:
    ret, image_1 = video_reader.read()
    cv2.imwrite("kill1" + ".jpg", image_1)
    if c>1:
      cv2.imwrite("kill"+".jpg", image_1)
      c-=1
    file_name="kill1.jpg"
    for k in range(10):
     video_reader.grab()
    t = read_tensor_from_image_file(file_name,
                                    input_height=input_height,
                                    input_width=input_width,
                                    input_mean=input_mean,
                                    input_std=input_std)

    input_name = "import/" + input_layer
    output_name = "import/" + output_layer
    input_operation = graph.get_operation_by_name(input_name)
    output_operation = graph.get_operation_by_name(output_name)

    with tf.compat.v1.Session(graph=graph) as sess:
      start = time.time()
      results = sess.run(output_operation.outputs[0],
                        {input_operation.outputs[0]: t})
      end=time.time()
    results = np.squeeze(results)

    top_k = results.argsort()[-5:][::-1]
    labels = load_labels(label_file)
    #print(labels)
    print('\nEvaluation time (1-image): {:.3f}s\n'.format(end-start))
    template = "{} (score={:0.5f})"
    for i in top_k:
      print(template.format(labels[i], results[i]))
      if labels[i]=="not clean":
        li.append(results[i])
except:
  pass
#print(li)
print("Percentage that is not clean "+str(sum(li)*100/len(li)))
density = sum(li)/len(li)
g= geocoder.ip('me')
lat, lon = g.latlng
k=[lat,lon]
print(lat, lon)
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.reverse(str(lat) + "," + str(lon))
address = location.raw['address']
address = list(address.values())
address = ",".join(address)
with open('emer.txt', 'w') as file:
  file.write(address)
for i in top_k:
   #print(template.format(labels[i], results[i]))
   if labels[i] == "not clean":
     ct = datetime.datetime.now()
     #sms(ct, lat, lon)
     #whatsapp1(lat, lon)
     #call(lat,lon)
     #email_generate(ct, 21, lat, lon)
     if density<0.96 :
        sms(ct,lat,lon)
     elif density<0.98:
        whatsapp1(lat,lon)
     else:
        email_generate(ct, 21,lat,lon)


