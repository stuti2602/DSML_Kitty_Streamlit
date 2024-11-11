import streamlit as st
st.title("My First Streamlit App")

# Add a text input

name = st.text_input("Enter your name: ")

# Add a button

if st.button("say Hello"):
    st.write(f"Hello {name}")
