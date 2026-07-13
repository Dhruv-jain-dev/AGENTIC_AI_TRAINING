from Session12E import DBHelper
from Session12B import User
import streamlit as st
st.title("User Registeration")
name=st.text_input("Enter full name:")
phone=st.text_input("Enter phone number:")
email=st.text_input("Enter email:")
password=st.text_input("Enter password:",type='password')

if st.button('Register'):

    user = User(name, phone, email, password)
    document_to_save = user.to_dictionary()

    db_helper = DBHelper()
    db_helper.select_collection()
    db_helper.save(document_to_save)