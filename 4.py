import streamlit as st
import pandas as pd

st.title("Crop Dashboard")

file  = st.file_uploader("Upload your csv file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())

if file:
    label = df["label"].unique()
    selected_label = st.selectbox("Filter by label", label)
    filtered_data = df[df["label"] == selected_label]
    st.dataframe(filtered_data)