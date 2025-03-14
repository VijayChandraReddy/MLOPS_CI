import streamlit as st

st.title('Power Calculator')
st.write('Enter a number to calculate square, cube, and fifth power')

n = st.number_input('Enter a number', value=1, step=1)

square = n ** 2
cube = n ** 3
fifth = n ** 5  # Fixed typo "fivth"

st.write(f"The square of {n} is {square}")
st.write(f"The cube of {n} is {cube}")
st.write(f"The fifth power of {n} is {fifth}")  # Fixed typo "fivth_power"
