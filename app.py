import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Simple Data Dashboard')
uploaded_file = st.file_uploader("Choose a file", type='csv')

if uploaded_file is not None:
    # Read the uploaded file directly
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader('Filter Data')
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)
    
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns, key='x_axis')
    y_column = st.selectbox("Select y-axis column", columns, key='y_axis')

    if st.button("Generate plot"):
        fig, ax = plt.subplots()
        filtered_df.plot(x=x_column, y=y_column, ax=ax)
        st.pyplot(fig)

else:
    st.write("Waiting for file upload...")


