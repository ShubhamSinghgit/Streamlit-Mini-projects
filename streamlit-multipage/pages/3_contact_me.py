import streamlit as st
import sqlite3

# SQLite connection 
conn = sqlite3.connect('contact_messages.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS messages
             (name TEXT, email TEXT, message TEXT)''')
conn.commit()

st.set_page_config(
    page_title="Contact",
    page_icon="📞", 
)

st.title("Contact Me")

# Contact Form
st.header("Contact Form")
name = st.text_input("Name", max_chars=50)
email = st.text_input("Email", max_chars=50)
message = st.text_area("Message", max_chars=500)
submit_button = st.button("Submit")

if submit_button:
    # Storing the message in the database
    c.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    st.success("Thank you for your message! I will get back to you as soon as possible.")

# Social Media Links
st.header("Social Media")
st.write("Connect with me on social media:")
st.write("- [Twitter](https://twitter.com/__shubhamtwt)")
st.write("- [LinkedIn](https://www.linkedin.com/in/shubham-singh-435220222/)")
st.write("- [GitHub](https://github.com/ShubhamSinghgit)")

# Contact Email
st.header("Email")
st.write("Feel free to reach out via email:")
st.write("[shubham.singh.200205@gmail.com](mailto:shubham.singh.200205@gmail.com)")

# Closing SQLite connection
conn.close()
