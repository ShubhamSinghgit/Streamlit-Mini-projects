import streamlit as st 

st.set_page_config(
    page_title="Multipage app",
    page_icon="😉", 
)

st.title("Homepage")
st.sidebar.success("Select a page")

if "my_input" not in st.session_state:
    st.session_state["my_input"]="" 

my_input = st.text_input("Enter text here", st.session_state["my_input"])

submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("Your Input entered was :", my_input)