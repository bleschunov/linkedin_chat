import streamlit as st
from linkedin_api import Linkedin
from message import Message

email = st.secrets.LD_USERNAME
password = st.secrets.LD_PASSWORD
me = st.secrets.ME

api = Linkedin(email, password, refresh_cookies=True)


def get_messages(member_id: str) -> list[Message]:
    def get_conversation(member_id):
        conv_details = api.get_conversation_details(member_id)
        conv_id = conv_details["dashEntityUrn"].split(":")[-1]
        return api.get_conversation(conv_id)

    messages = []
    conv = get_conversation(member_id)

    for elem in conv["elements"]:
        content = elem["eventContent"]["com.linkedin.voyager.messaging.event.MessageEvent"]["attributedBody"]["text"]
        _from = elem["from"]["com.linkedin.voyager.messaging.MessagingMember"]["miniProfile"]["objectUrn"]
        messages.append(Message(content, me == _from))

    return messages
