# CleanSweep.AI
A-EYE on SCATTERED GARBAGE! An AI & ML solution to solve some of the basic but most important problems in day to day life.  

You can view the project here: https://manikanta-7342-cleansweep-streamlit-ankx0y.streamlit.app/

Youtube Link: https://youtu.be/u2iq5j9OaN0

Problem Statement:- Scattered scrap detection is a significant problem in many countries around the world. It can lead to a number of negative consequences, including environmental degradation, public health issues, and decreased quality of life for residents.
Garbage can accumulate in public spaces, such as streets, parks, and beaches, due to individuals littering or improperly disposing of waste.
In some areas, waste collection systems may be inadequate or inefficient, leading to a build-up of garbage in certain areas.

Objective:- The goal is design an object classification model which segregates garbage and scattered scrap from the given input data from various sources like dashcams, CCTVs installed in roads etc.
The video is processed and the density of garbage is then calculated and the processed through a machine learning algorithm.
If garbage is detected is greater than a certain threshold, then the concerned authorities are intimated with help of an escalation algorithm.

Solution:- The solution to solve the above problem is implementing a Garbage Detection Model using the Single Shot Detector Algorithm whcih is trained on the TACO Dataset. 

System Workflow:-
![Flowchart](https://user-images.githubusercontent.com/80829447/208266806-8d21746e-7aa9-4147-8169-4d3ae4e526b1.png)

Steps to run this project:  
STEP 1: Download the models and the weights from the drive link provided below.  
STEP 2: Clone the GitHub repository.  
STEP 3: Run the code provided below in the terminal of the project folder.

Install the requirements:
```
pip install -r requirements.txt
```

Run the app:
```
streamlit run app.py
```

Collaborators:  
Mani Kanta: https://github.com/Manikanta-7342  
Akhil: https://github.com/Akhil5347  
Shreyas: https://github.com/ShreyasKuntnal

