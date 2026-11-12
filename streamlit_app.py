import streamlit as st
import pandas as pd

st.title('🎈 Machine Learning App')

st.write('This is app')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_size.csv')
df
