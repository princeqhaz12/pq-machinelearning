import streamlit as st
import pandas as pd

st.title('🎈 Machine Learning App')

st.info('This is app')

with st.expander('Data'):
st.write('**Raw Data**')
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_size.csv')
df

st.write('**X**')
X = df.drop('species', axis=1)

st.write('**y**')
X = df.species
y
