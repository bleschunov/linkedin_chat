import streamlit as st
from linkedin_api import Linkedin
from message import Message

email = st.secrets.LD_USERNAME
password = st.secrets.LD_PASSWORD
me = st.secrets.ME

api = Linkedin(email, password, refresh_cookies=True)


def get_messages(conv_id: str) -> list[Message]:
    messages = []
    conv = api.get_conversation(conv_id)

    for elem in conv["elements"]:
        content = elem["eventContent"]["com.linkedin.voyager.messaging.event.MessageEvent"]["attributedBody"]["text"]
        _from = elem["from"]["com.linkedin.voyager.messaging.MessagingMember"]["miniProfile"]["objectUrn"]
        messages.append(Message(content, me == _from))

    return messages


print(get_messages("2-NTJkNWI0YzItMjBjMC00MjIzLTg0M2YtOGQ5NDBlZjU4YzAzXzAxMw=="))