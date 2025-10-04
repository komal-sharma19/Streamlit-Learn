import streamlit as st

st.title("Hello Programming App")
st.subheader("Made with streamlit")
st.text("Welcome to my first interative app")
st.write("Choose your favourite programming language from the dropdown")

lang = st.selectbox("Your favourite language", ["Python", "Java", "C++", "JavaScript", "Go", "Ruby", "Swift"])
st.write(f"Your choosen language is {lang}")

st.success("Your choice was recorded successfully!")