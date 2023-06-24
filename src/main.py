import streamlit as st
from streamlit_chat import message

from api import get_messages, get_profile_url, send_message
from message import Message
from spreadsheet import insert_row

query_params = st.experimental_get_query_params()
member_id = query_params["member_id"][0]


def print_messages():
    for msg in st.session_state.msg_list:
        message(msg.text, msg.is_me, logo=msg.avatar)


st.session_state.msg_list = get_messages(member_id)

print_messages()

query = st.text_input('', '')

send_message(query, member_id)
insert_row(get_profile_url(member_id))

# if len(st.session_state.msg_list) > 1:
#     answer = agent.run(query)
#     st.session_state.msg_list.append(Message(answer, False))
#     message(answer)