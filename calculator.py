import streamlit as st
st.header("Basic Calculator")

# take a square root of number
def square(number):
    return number * number

# how to take number from user:
number = st.number_input("Insert a number")
st.write("The current number is ", number)

# how to call this function - on demand function call button
if st.button("Calculate square"):
    result = square(number)
    st.subheader(f"Result: {result}")

    st.subheader("result")


