import streamlit as st

def set_page_configuration():
    st.set_page_config(
        page_title="Multipage app",
        page_icon="😉",
    )

def display_homepage():
    st.title("Homepage")
    st.sidebar.success("Select a page")

def handle_text_input():
    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

    my_input = st.text_input("Enter text here", st.session_state["my_input"])
    return my_input

def handle_submit_button(my_input):
    submit = st.button("Submit")
    if submit:
        st.session_state["my_input"] = my_input
        st.write("Your Input entered was :", my_input)

def main():
    set_page_configuration()
    display_homepage()
    my_input = handle_text_input()
    handle_submit_button(my_input)

if __name__ == "__main__":
    main()
