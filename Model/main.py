import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import joblib
import sklearn
import pickle

st.write("hello")
pickled_model = pickle.load(open('Model/model12.pkl', 'rb'))


bizimlist = []

age = st.slider('How old are you?', 0, 90, 25)
st.write("I'm ", age, 'years old.')
bizimlist.append(age)

job = st.selectbox(
    'Select your job?',
    ('blue-collar', 'services', 'admin.','entrepreneur','self-employed','technician','management','student','retired'
     ,'housemaid','unemployed'))

if job == 'blue-collar':
    bizimlist.append(0)
elif job == 'services':
    bizimlist.append(1)
elif job == 'admin.':
    bizimlist.append(2)
elif job == 'entrepreneur':
    bizimlist.append(3)
elif job == 'self-employed':
    bizimlist.append(4)
elif job == 'technician':
    bizimlist.append(5)
elif job == 'management':
    bizimlist.append(6)
elif job == 'student':
    bizimlist.append(7)
elif job == 'retired':
    bizimlist.append(8)
elif job == 'housemaid':
    bizimlist.append(9)
elif job == 'unemployed':
    bizimlist.append(10)


marital = st.selectbox(
    'What is your marital status?',
    ('married', 'single', 'divorced'))

if marital == 'married':
    bizimlist.append(0)
elif marital == 'single':
    bizimlist.append(1)
elif marital == 'divorced':
    bizimlist.append(2)




default = st.radio(
    "Select Has Credit in Default?",
    ('No', 'Yes'))
if default == 'Yes':
    default = 1
else:
    default=0

bizimlist.append(default)



loan = st.radio(
    "Select Has loan?",
    ('No', 'Yes'))
if loan == 'Yes':
    loan = 1
else:
    loan = 0
st.write(loan)
bizimlist.append(loan)


contact = st.selectbox(
    'Select Contact Communication Type?',
    ('cellular', 'telephone'))
if contact == 'telephone':
    contact = 1
else:
    contact = 0
bizimlist.append(contact)


month = st.selectbox(
    'Select Last Contact Month',
    ('may', 'jun','nov','sep','jul','aug','mar','oct','apr'
     'dec'))
if month == 'may':
    bizimlist.append(0)
elif month == 'jun':
    bizimlist.append(1)
elif month == 'nov':
    bizimlist.append(2)
elif month == 'sep':
    bizimlist.append(3)
elif month == 'jul':
    bizimlist.append(4)
elif month == 'aug':
    bizimlist.append(5)
elif month == 'mar':
    bizimlist.append(6)
elif month == 'oct':
    bizimlist.append(7)
elif month == 'apr':
    bizimlist.append(8)
elif month == 'dec':
    bizimlist.append(9)

day_of_week = st.selectbox(
    'Select Last Contact Day of the Week',
    ('mon', 'tue','wed','thu','fri'))
if day_of_week == 'mon':
    bizimlist.append(0)
elif day_of_week == 'tue':
    bizimlist.append(1)
elif day_of_week == 'wed':
    bizimlist.append(2)
elif day_of_week == 'thu':
    bizimlist.append(3)
elif day_of_week == 'fri':
    bizimlist.append(4)

duration = st.number_input('Insert a duration', step=1.0,format="%d")
st.write('The current number is', round(duration))
duration = int(duration)
bizimlist.append(duration)

campaign = st.number_input('Number of contacts performed during this campaign',step=1.0,format="%d")
st.write('The current number is ', round(campaign))
campaign =int(campaign)
bizimlist.append(campaign)

pdays = st.number_input('Enter Number of Days Passed After Last Contact(pdays)',step=1.0,format="%d")
st.write('The current number is ', round(pdays))
pdays =int(pdays)
bizimlist.append(pdays)

previous = st.number_input('Enter Number of Contacts Performed Before this Campaign(previous)',step=1.0,format="%d")
st.write('The current number is ', round(previous))
previous =int(previous)
bizimlist.append(previous)


poutcome = st.selectbox(
    'Outcome of the previous marketing campaign',
    ('nonexistent', 'failure','success'))
if poutcome == 'nonexistent':
    bizimlist.append(0)
elif poutcome == 'failure':
    bizimlist.append(1)
elif poutcome == 'success':
    bizimlist.append(2)



emp = st.number_input('Insert a emp.var.rate')
st.write('The current number is ', emp)
bizimlist.append(emp)

consprice = st.number_input('Insert a cons.price.idx')
st.write('The current number is ', consprice)
bizimlist.append(consprice)


consconf = st.number_input('Insert a cons.conf.idx')
st.write('The current number is ', consconf)
bizimlist.append(consconf)


euribor3m = st.number_input('Insert a euribor3m')
st.write('The current number is ', euribor3m)
bizimlist.append(euribor3m)

nr = st.number_input('Insert a nr.employed')
st.write('The current number is ', nr)
bizimlist.append(nr)



list_of_lists = [bizimlist]
df = pd.DataFrame(list_of_lists, columns=['age','job','marital','default',
                                      'loan','contact','month','day_of_week',
                                      'duration','campaign','pdays','previous',
                                      'poutcome','emp.var.rate','cons.price.idx',
                                      'cons.conf.idx','euribor3m','nr.employed'])



if st.button('Predict'):
    prediction = pickled_model.predict(df)[0]
    if prediction == 0:
        st.markdown('<span style="color:red;">no</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span style="color:green;">yes</span>', unsafe_allow_html=True)



