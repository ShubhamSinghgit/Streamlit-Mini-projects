import streamlit as st 

st.set_page_config(
    page_title="Projects",
    page_icon="📚", 
)

st.title("Projects")

st.write("Your input was", st.session_state["my_input"])

