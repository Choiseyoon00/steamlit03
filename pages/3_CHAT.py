
import streamlit as st
import numpy as np
from streamlit_chat import message
from openai import OpenAI

client = st.session_state.get('openai_client', None)

assistant = client.beta.assistants.create(
  name="chatbot",
  instructions="you are a chatbot.",
  model="gpt-4o-mini"
)

thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "you are a chatbot."
    }
  ]
)

prompt = st.chat_input("Say something")
if prompt:
    with st.chat_message("user"):










 if "messages" not in st.session_state: ##메모리 초기화
   with st.session_state.messages = [] 
