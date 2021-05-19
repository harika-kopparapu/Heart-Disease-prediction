import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

pickle_in = open("Model","rb")
Classifier = pickle.load(pickle_in)

try:
  def Predict_authentication(Age,Sex,CPT,RBP,SC,FBS,RER,MHRA,EIA,OP,SLOP,MV,THAL):
    prediction = Classifier.predict([[Age,Sex,CPT,RBP,SC,FBS,RER,MHRA,EIA,OP,SLOP,MV,THAL]])
    print(prediction)
    return prediction
  def main():
    st.title("Heart Disease UCI")
    html_temp = """
    <div style="background-color:#2E4A62;padding:3px;border-radius:25px;">
    <h2 style="color:white;text-align:center;font-weight:bold;">Put Your Heart, Mind, And Soul Into Even Your Smallest Acts. This Is The Secret Of Success.<h2>
    </div>
    <style>
    body {
    background-color:#8fe2f2;
    background-size: cover;
    }
    </style>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.slider('Point Your Age:', 0, 100, 0)
    Sex = st.radio("Select Gender:[Male:'1',Female:'0']",("0", "1"))
    FBS = st.radio("Select Fasting Blood Sugar:[True :'1',False:'0']",("0","1"))
    CPT = st.sidebar.selectbox("Select the Chest Pain Type",("1","2","3","4"))
    RBP = st.text_input("Enter the Resting Blood Pressure","")
    SC = st.text_input("Enter the Serum Cholestoral in mg/dl","")  
    RER = st.sidebar.selectbox("Select the Resting Electrocardiographic Results",("0", "1" ,"2"))
    MHRA = st.text_input("Enter the Maximum Heart Rate Achieved","")
    EIA = st.text_input("Enter the Exercise Induced Angina","")
    OP = st.text_input("Enter the oldpeak = ST depression induced by exercise relative to rest","")
    SLOP = st.sidebar.selectbox("Select the slope of the peak exercise ST segment",("1", "2" ,"3"))
    MV = st.sidebar.selectbox("Select the number of major vessels (0-3) colored by flourosopy",("0", "1" ,"2","3"))

    THAL = st.sidebar.selectbox("Select the THAL: [Normal:'3',Fixed defect:'6' , Reversable defect:'7']",("3", "6", "7"))

    result=""
    if st.button('Predict'):
                    result = Predict_authentication(Age,Sex,CPT,RBP,SC,FBS,RER,MHRA,EIA,OP,SLOP,MV,THAL)    
    if (result==0):
                    st.success("There is no Presence Of Heart Disease In The Patient")
                    st.markdown("![Alt Text](https://i.pinimg.com/originals/c0/a4/ce/c0a4ce21e959bba78e7cc0d3ed02f781.gif)")
                    st.balloons()
    elif (result==1):
                    st.success("The Presence Of Heart Disease In The Patient")
                    st.markdown("![Alt Text](https://us.123rf.com/450wm/kahovsky/kahovsky1712/kahovsky171200010/91317474-sad-unhealthy-sick-heart-with-nameplate-help-vector-modern-style-cartoon-character-illustration-icon.jpg?ver=6)") 
   

  if __name__=='__main__':
      main()

except:
    st.error("Enter All Values Please")
    st.info('Referesh The APP')

if st.button('About Me'):
                      st.info('KOPPARAPU RANGA HARIKA')
                      st.error('18MIS7160')
                      """Gmail:"""
                      st.code('''harika.18MIS7160@vitap.ac.in''')