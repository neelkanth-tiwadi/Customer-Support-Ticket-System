import streamlit as st

st.title("Customer Support Ticket System")

ticket = st.text_area("Enter your ticket")

if st.button("Submit"):
    st.write("Ticket received")
    st.write(ticket)