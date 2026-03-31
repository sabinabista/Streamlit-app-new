import streamlit as st
from prompt import combined_chain
from prompt import parallel_chain

st.title("Email Assistant")
email_topic = st.text_input("Email Topic")
recipient = st.text_input("recipient")
name = st.text_input("Name")


def generate_email():

    print(name)

    email = parallel_chain.invoke(
        {
            "email_topic": email_topic,
            "recipient": recipient,
            "name": name,
            "question": email_topic,
        }
    )
    st.markdown(email["combined_chain"]["final_email"])
    st.markdown(email["subject_line"]["subject_line"])


st.button("Generate Email", on_click=generate_email)
