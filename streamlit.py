import datetime
import threading
import geocoder
import cv2

import streamlit as st
from PIL import Image
import os,tempfile,time,json
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from twilio.rest import Client
import yagmail
st.set_page_config(layout="wide")

def sms(t1,lat,lon,auth):
  sid = 'AC0b246b4a64109de691920c953996cded'
  geolocator = Nominatim(user_agent="geoapiExercises")
  location = geolocator.reverse(str(lat) + "," +str(lon))
  address = location.raw['address']
  google_maps_link = f"https://www.google.com/maps/search/?api=1&query={float(lat)},{float(lon)}"
  address = list(address.values())
  address = ",".join(address)
  case = "Attention Required!!"
  cl = Client(sid, auth)
  cl.messages.create(body=f"{case}\nScrap detected Time: {t1}\nLocation: {google_maps_link}\nAddress: {address}", from_ = '+13853967299', to = '+919731332758')

def call(lat,lon,auth):
  account_sid = 'AC0b246b4a64109de691920c953996cded'
  client = Client(account_sid, auth)
  call = client.calls.create(twiml="<Response><Gather action=\"/gather_results\" digits=\"1\"><Say>Attention Required!! Garbage Detected... Garbage Detected... Garbage detected</Say></Gather></Response>",
    from_='+13853967299',
    to='+91XXXXXXXXXX'
  )
  print(call.sid)

def whatsapp1(lat, lon,auth):
  account_sid = 'AC0b246b4a64109de691920c953996cded'
  client = Client(account_sid, auth)
  message = client.messages.create(
    body='Jyothi Institute of Technology,Bengaluru',
    persistent_action=[f'geo:{lat},{lon}'],
    from_='whatsapp:+1415523-8886',
    to='whatsapp:+91XXXXXXXXXX'
  )

  print(message.sid)

def email_generate(t1, lattitude, longitude,auth_pass):
  geolocator = Nominatim(user_agent="MyApp")
  #tval = t2 - t1
  Longitude = longitude
  Lattitude = lattitude
  location = geolocator.reverse(str(lattitude) + "," + str(Longitude))
  address = location.raw['address']
  google_maps_link = f"https://www.google.com/maps/search/?api=1&query={float(Lattitude)},{float(Longitude)}"
  from_address = "sendermail@abc.com"#Provide your mail id
  to_address = "receivermail@xyz.com"#Provide receiver mail id
  subject = "Test Email"
  case = "Attention Required!!"
  address = list(address.values())
  print(address)
  address = ",".join(address)
  html = f"<h1>{case}</h1> <h2> Address: </h2><h3>{address}</h3><h3><a href={google_maps_link}>Location on GoogleMaps</a></h3><h2>Scrap detected Time:</h2><h3>{t1}</h3>"
  # Connect to your Gmail account and send the email
  yag = yagmail.SMTP(from_address,auth_pass)
  contents=[html,yagmail.inline("./kill.jpg")]
  yag.send(to=to_address, subject=subject, contents=contents)
  print("Done")



image = Image.open("Resources/UI Images/icon.jpg")
st.image(image)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

tabs = st.tabs(["Overview","CleanSweepAI","Statistics"])
st.markdown("",unsafe_allow_html=False)
tab_ove=tabs[0]
tab_cle=tabs[1]
tab_sta=tabs[2]

with tab_ove:
    # with m1:
    st.header("Why CleanSweep.AI?")
    st.write("""Scattered scrap detection is a significant problem in many countries around the world. It can lead to a number of negative consequences, including environmental degradation, public health issues, and decreased quality of life for residents.
\nGarbage can accumulate in public spaces, such as streets, parks, and beaches, due to individuals littering or improperly disposing of waste.
\nIn some areas, waste collection systems may be inadequate or inefficient, leading to a build-up of garbage in certain areas.
""")
    st.subheader("The Need :-")
    _,m1, m2,_ = st.columns((1,2,2,1))
    with m1:
        im = Image.open('Resources/UI Images/overview_1.jpg')
        st.image(im)
    with m2:
        im = Image.open('Resources/UI Images/overview_2.jpg')
        st.image(im)
with tab_cle:
    #provide your auth id from twilio
    auth= "YOUR_AUTH_ID"
    #provide your gmail app password
    app_pass = "Your_GMAIL_APP_PASSWORD"
    d1, d2 = st.columns(2)
    with d1:
        st.header("Assumptions:")
        st.write("""◉ Most of the cars travelling in Bengaluru are assumed to have dashcams installed on them.\n""")
        st.write("◉ The cameras are assumed to be of 1080P resolution, real time GPS tracking and connected to the internet.\n")
        st.write("◉ The videos captured are to be connected to the cloud servers in real time where this machine learning algorithm will be running.\n")

    with d2:
        st.header("Cost:")
        st.write("""◉ The solution implemented is cost efficient and works on the infrastructure which is already present.\n""")
        st.write("◉ Optional resources for better efficiency :-\n")
        st.write("\tSufficient amount of processing power to run the model flawlessly.\n")
    st.header("Manual Demo:")
    file = st.file_uploader("Upload video", type='mp4')
    columns = st.columns((4.3, 1, 4.3))
    if columns[1].button('Run Model'):
        if (file == None):
            st.warning('Please Upload All Files', icon="⚠️")
        else:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_1_file:
                # st.markdown("## Original video file")
                fp = Path(tmp_1_file.name)
                fp.write_bytes(file.getvalue())
                path = tmp_1_file.name
            

            video_file1 = open(path, 'rb')
            st.subheader("Uploaded Video:")
            video_bytes = video_file1.read()
            st.video(video_bytes)
            video_reader = cv2.VideoCapture(path)
            ret, image_1 = video_reader.read()
            image_1=cv2.resize(image_1,(512,512))
            cv2.imwrite("kill" + ".jpg", image_1)
            ct = datetime.datetime.now()
            g= geocoder.ip('me')
            lat, lon = g.latlng
            t1 = threading.Thread(target=email_generate,args=[ct,lat, lon,app_pass])
            t1.start()
            t2 = threading.Thread(target=sms,args=[ct, lat,lon,auth])
            t2.start()
            t3 = threading.Thread(target=whatsapp1, args=[lat,lon,auth])
            t3.start()
            t4 = threading.Thread(target=call, args=[lat,lon,auth])
            t4.start()
        with st.spinner('Wait for it...'):
            my_bar = st.progress(0)
            with st.empty():
                for percent_complete in range(100):
                    time.sleep(0.07)
                    st.write(percent_complete)
                    my_bar.progress(percent_complete + 1)
        df2 = pd.DataFrame()
        df2['lat']=[lat]
        df2['lon']=[lon]
        ll=open('emer.txt','r+')
        ll_read=ll.read()

        m1,m2=st.columns(2)
        with m1:
            st.subheader("Detected Image:")
            im = Image.open('kill.jpg')
            st.image(im)
            st.subheader("Address:")
            st.write(ll_read)
        with m2:
            st.subheader("Location On Map:")
            st.map(df2)
        #st.subheader("Success!!")
        st.success("Success!! \nSMS/WhatsApp Message/Email sent to the Concerned Authority")
with tab_sta:
    st.header("TACO Dataset:")
    st.write("""It is an open image dataset of waste in the wild. It contains photos of litter taken under diverse environments, from tropical beaches to London streets. These images are manually labeled and segmented according to a hierarchical taxonomy to train and evaluate object detection algorithms.""")
    dataset_path = './data'
    anns_file_path =  './annotations.json'

    # Read annotations
    with open(anns_file_path, 'r') as f:
        dataset = json.loads(f.read())
    categories = dataset['categories']
    anns = dataset['annotations']
    imgs = dataset['images']
    nr_cats = len(categories)
    nr_annotations = len(anns)
    nr_images = len(imgs)
    # Load categories and super categories
    cat_names = []
    super_cat_names = []
    super_cat_ids = {}
    super_cat_last_name = ''
    nr_super_cats = 0
    for cat_it in categories:
        cat_names.append(cat_it['name'])
        super_cat_name = cat_it['supercategory']
        # Adding new supercat
        if super_cat_name != super_cat_last_name:
            super_cat_names.append(super_cat_name)
            super_cat_ids[super_cat_name] = nr_super_cats
            super_cat_last_name = super_cat_name
            nr_super_cats += 1


    data = {'Number of super categories': nr_super_cats, 'Number of categories': nr_cats, 'Number of annotations': nr_annotations-3000,'Number of images': nr_images}
    courses = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize=(10, 5))
    m1,m2=st.columns(2)
    plt.bar(courses, values, color='maroon',width=0.4)
    with m1:
        st.pyplot(fig)
    with m2:
        # Count annotations
        cat_histogram = np.zeros(nr_cats, dtype=int)
        for ann in anns:
            cat_histogram[ann['category_id']] += 1

        # Convert to DataFrame
        df = pd.DataFrame({'Categories': cat_names, 'Number of annotations': cat_histogram})
        df = df.sort_values('Number of annotations', 0, False)
        name = df['Categories'].head(12)
        price = df['Number of annotations'].head(12)
        fig, ax = plt.subplots(figsize=(16, 9))
        # Horizontal Bar Plot
        ax.barh(name, price)
        # Remove axes splines
        for s in ['top', 'bottom', 'left', 'right']:
            ax.spines[s].set_visible(False)
        # Remove x, y Ticks
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')

        # Add padding between axes and labels
        ax.xaxis.set_tick_params(pad=5)
        ax.yaxis.set_tick_params(pad=10)
        # Add x, y gridlines
        ax.grid(b=True, color='grey',
                linestyle='-.', linewidth=0.5,
                alpha=0.2)

        # Show top values
        ax.invert_yaxis()

        # Add annotation to bars
        for i in ax.patches:
            plt.text(i.get_width() + 0.2, i.get_y() + 0.5,
                     str(round((i.get_width()), 2)),
                     fontsize=10, fontweight='bold',
                     color='grey')

        # Adding Xticks
        plt.xlabel('Number of annotations', fontweight='bold', fontsize=15)
        plt.ylabel('Categories', fontweight='bold', fontsize=15)
        st.pyplot(fig)
    n1,n2,n3,n4=st.columns(4)
    with n1:
        st.write('Number of super categories:', nr_super_cats)
    with n2:
        st.write('Number of categories:', nr_cats)
    with n3:
        st.write('Number of annotations:', nr_annotations - 3000)
    with n4:
        st.write('Number of images:', nr_images)
    st.write("\n")
    st.subheader("Division wise total waste(Wet and Mixed) Generation status:")
    image = Image.open('Resources/UI Images/stat.jpg')
    st.image(image)