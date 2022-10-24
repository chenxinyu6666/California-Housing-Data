from curses import def_shell_mode
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('housing.csv')

plt.style.use('seaborn')


st.title('California Housing Data(1990) by Xinyu Chen')
House_price_filter = st.slider('Median House Price', 0, 500001, 20000)
df = df[df.median_house_value >= House_price_filter]

ocean_proximity_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  
     df.ocean_proximity.unique())  

df = df[df.ocean_proximity.isin(ocean_proximity_filter)]

income_level = st.sidebar.radio('Choose income level',['Low','Medium','High'],key = 'visibility',disabled =False,horizontal = False )
if income_level == 'Low':
    df = df[df.median_income <=2.5]
if income_level == 'High':
    df = df[df.median_income >4.5]
if income_level == 'Medium':
    df = df[(df.median_income>2.5)&(df.median_income<4.5)]

st.map(df)


st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(20, 5))
df.median_house_value.hist(bins=30)
st.pyplot(fig)


