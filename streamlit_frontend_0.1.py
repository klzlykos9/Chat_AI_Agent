
import streamlit as st

with st.chat_message('user'):
    st.text('Hi')


with st.chat_message('assistant'):
    st.text('how can i help you')

with st.chat_message('user'):
    st.text('my name is klz')


# st.session_state -> dict -> 

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []



# message_history = []

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input= st.chat_input("Type here")

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role':'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    st.session_state['message_history'].append({'role':'assistant', 'content': user_input})
    with st.chat_message('assistant'):
        st.text(user_input)