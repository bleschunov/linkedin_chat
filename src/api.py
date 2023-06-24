import streamlit as st
from linkedin_api import Linkedin
from message import Message

email = st.secrets.LD_USERNAME
password = st.secrets.LD_PASSWORD
me = st.secrets.ME

api = Linkedin(email, password, refresh_cookies=False)


def get_messages(member_id: str) -> list[Message]:
    def get_conversation(member_id):
        conv_details = api.get_conversation_details(member_id)
        conv_id = conv_details["dashEntityUrn"].split(":")[-1]
        return api.get_conversation(conv_id)

    messages = []
    conv = get_conversation(member_id)

    for elem in conv["elements"]:
        content = elem["eventContent"]["com.linkedin.voyager.messaging.event.MessageEvent"]["attributedBody"]["text"]
        _from_obj = elem["from"]["com.linkedin.voyager.messaging.MessagingMember"]["miniProfile"]
        _from = _from_obj["objectUrn"]
        avatar_obj = _from_obj["picture"]["com.linkedin.common.VectorImage"]
        avatar = avatar_obj["rootUrl"] + avatar_obj["artifacts"][0]["fileIdentifyingUrlPathSegment"]
        messages.append(Message(content, me == _from, avatar))

    return messages


def get_profile_url(member_id: str) -> str:
    profile = api.get_profile(member_id)
    return f"https://linkedin.com/in/{profile['public_id']}"


def send_message(message, member_id: str) -> None:
    api.send_message(message, recipients=[member_id])
