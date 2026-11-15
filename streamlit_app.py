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

with st.expander("Data visualization"):
    st.scatter_chart(data=df, x="culmen_length_mm", y="body_mass_g", color="species")
with st.sidebar:
    st.header('Input features')
    island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
    gender = st.selectbox('Gender', ('male', 'female'))
    culmen_length_mm = st.slider('culmen Length (mm)', 32.1, 59.6, 43.9)
    culmen_depth_mm = st.slider('culmen Depth (mm)', 13.1, 21.5, 17.2)
    flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
    body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)

    data = {'island': island, 
            'culmen_length_mm': culmen_length_mm,
            'culmen_depth_mm': culmen_depth_mm,
            'flipper_length_mm': flipper_length_mm,
           'body_mass_g': body_mass_g,
            'gender': gender}
    input_df = pd.DataFrame(data, index=[0])
    input_peguins = pd.concat([input_df, X], axis=0)

input_df
    
