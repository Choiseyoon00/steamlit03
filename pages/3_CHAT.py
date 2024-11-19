
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

while True:
  # 사용자 입력
  user_msg = input("user: ")
  if user_msg == 'STOP':
    break

  new_message = client.beta.threads.messages.create(
    thread_id = thread.id,
    role="user",
    content=user_msg
  )

  run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
    poll_interval_ms=2000
  )
  if run.status in ['expired','failed','cancelled','incomplete']:
    print("Error:", run.status)
    break

  thread_messages = client.beta.threads.messages.list(thread.id, limit=1)
  for msg in thread_messages.data:
    print(f"{msg.role}: {msg.content[0].text.value}")



if prompt := st.chat_input("What is up?"):
  st.chat_message("user").markdown(prompt) 
  st.session_state.messages.append({"role": "user", "content": prompt}) 

with st.chat_message("assistant"):
    st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})







if "messages" not in st.session_state: ##메모리 초기화
 st.session_state.messages = [] 
