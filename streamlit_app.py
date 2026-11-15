import streamlit as st
import pandas as pd

st.title('🎈 Machine Learning App')

st.info('This is app')

with st.expander('Data'):

    df = pd.read_csv(
  'https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_size.csv'
)
    
st.write('**Raw data**')
st.dataframe(df)    
st.dataframe(X)
st.dataframe(y)
    
st.write('**X**')
X = df.drop('species', axis=1)
st.write('**y**')
y = df['species']






    
