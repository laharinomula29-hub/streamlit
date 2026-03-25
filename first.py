import streamlit as st

st.title("Student Registration Form")

col1,col2=st.columns(2)

with col1:
    first_name=st.text_input("First Name")
with col2:
    last_name=st.text_input("Last Name")
email = st.text_input("Email")
password = st.text_input("password",type="password")
confirm_password = st.text_input("confirm password",type="password")
address = st.text_area("Address")

if st.button("Submit"):
    st.write("Registration Successful!")
    st.write("First Name:", first_name)
    st.write("Last Name:", last_name)
    st.write("Email:", email)
    st.write("password:", password)
    st.write("confirm_password:", confirm_password)
    st.write("Address:", address)