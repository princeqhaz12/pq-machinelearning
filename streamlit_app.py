import streamlit as st
import pandas as pd
# Page title
st.title("🐧 Machine Learning App")
# Info box
st.info("This is a simple Machine Learning App.")
# Everything related to the data is inside this expander
with st.expander("Data"):
    # Load data
    df = pd.read_csv(
        "https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_size.csv"
    )
    # Raw data
    st.subheader("Raw Data")
    st.dataframe(df)
    # Dataset shape
    st.subheader("Dataset Shape")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")
    # Features
    st.subheader("Features (X)")
    X = df.drop("species", axis=1)
    st.dataframe(X)
    # Target
    st.subheader("Target (y)")
    y = df["species"]
    st.dataframe(y)
    # Summary statistics
    st.subheader("Summary Statistics")
    st.dataframe(df.describe())
    # Missing values
    st.subheader("Missing Values")
    st.dataframe(df.isnull().sum().to_frame("Missing Count"))
# Content outside the expander
st.success("Application loaded successfully!")

with st.expander('Data visualization'):
    st.scatter_chart(data=df, x='bill_length_mm', y ='body_mass_g', color='species')
