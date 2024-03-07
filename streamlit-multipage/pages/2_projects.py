import streamlit as st 

st.set_page_config(
    page_title="Projects",
    page_icon="📚", 
)

st.title("Projects")

# Check if the input exists in the session state
if "my_input" not in st.session_state:
    st.error("No input provided. Please go back to the homepage and enter your text.")
else:
    # Displays the input
    st.write("Your input was:", st.session_state["my_input"])

