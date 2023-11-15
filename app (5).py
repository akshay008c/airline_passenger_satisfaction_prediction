import pickle
import numpy as np
import streamlit as st

def set_bg_hack_url():    
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://rare-gallery.com/uploads/posts/546256-airplane-planes.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()



model=pickle.load(open('/content/classifier.pkl','rb'))
scaler=pickle.load(open('/content/scalar.pkl','rb'))
st.title('Airline customer satsfaction prediction')
opt={'Select option':3,'Male':1,'Female':0}
a=st.selectbox('Gender:',list(opt.keys()))
if a=='Select option':
  st.write('Please select a option')

opt1={'Select option':3,'Disloyal Customer':1,'Loyal Customer':0}
b=st.selectbox('customer_type',list(opt1.keys()))
if b=='Select option':
  st.write('Please select a option')


c=st.number_input('Age')

opt2={'Select option':3,'Personal Travel':1,'Business travel':0}
d=st.selectbox('type_of_travel',list(opt2.keys()))
if d=='Select option':
  st.write('Please select a option')

opt3={'Select option':4,'Eco Plus':2,'Eco':1,'Business travel':0}
e=st.selectbox('customer_class',list(opt3.keys()))
if e=='Select option':
  st.write('Please select a option')

f=st.number_input('Flight distance')
g=st.number_input('Inflight wifi service')
h=st.number_input('Departure arrival time covenient')
i=st.number_input('Ease of online booking')
j=st.number_input('Gate location')
k=st.number_input('Food and driks')
l=st.number_input('Online boardinf')
m=st.number_input('Seat confort')
n=st.number_input('In flight entertainment')
o=st.number_input('On board service')
p=st.number_input('Leg room service')
q=st.number_input('Bagage handeling')
r=st.number_input('Checking service')
s=st.number_input('Inflight service')
t=st.number_input('Cleanliness')
u=st.number_input('Departure delay in minutes')
v=st.number_input('Arraival Delay in minutes')
a=opt[a]
b=opt1[b]
d=opt2[d]
e=opt3[e]




w = scaler.transform([[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v]])

if st.button('Predict'):
    pred = model.predict(w)
    if pred == 0:
        st.write('Not satisfied')
    else:
        st.write('Satisfied')
    st.write('Prediction:', pred[0])  # Accessing the first element of the prediction array
