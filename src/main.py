import streamlit as st
from streamlit_chat import message

from api import get_messages
from message import Message


def print_messages():
    for msg in st.session_state.msg_list:
        message(msg.text, msg.is_me)


if "msg_list" not in st.session_state:
    query_params = st.experimental_get_query_params()
    conv_id = query_params["conv_id"][0]
    st.session_state.msg_list = get_messages(conv_id)


query = st.text_input('Ваш запрос', '')
if len(st.session_state.msg_list) == 0:
    st.session_state.msg_list.append(Message('Привет! Какой у вас запрос?', False))
    print_messages()
    exit()

st.session_state.msg_list.append(Message(query, True))
print_messages()

# if len(st.session_state.msg_list) > 1:
#     answer = agent.run(query)
#     st.session_state.msg_list.append(Message(answer, False))
#     message(answer)