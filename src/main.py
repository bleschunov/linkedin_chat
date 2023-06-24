import streamlit as st
from streamlit_chat import message

from api import get_messages, get_profile_url, send_message
from message import Message
from spreadsheet import insert_row

query_params = st.experimental_get_query_params()
member_id = query_params["member_id"][0]


def print_messages():
    for msg in st.session_state.msg_list:
        message(msg.text, msg.is_me)


if "msg_list" not in st.session_state:
    st.session_state.msg_list = get_messages(member_id)


query = st.text_input('Ваш запрос', '')
if len(st.session_state.msg_list) == 0:
    st.session_state.msg_list.append(Message('Привет! Какой у вас запрос?', False))
    print_messages()
    exit()

st.session_state.msg_list.append(Message(query, True))
send_message(query, member_id)
insert_row(get_profile_url(member_id))
print_messages()

# if len(st.session_state.msg_list) > 1:
#     answer = agent.run(query)
#     st.session_state.msg_list.append(Message(answer, False))
#     message(answer)