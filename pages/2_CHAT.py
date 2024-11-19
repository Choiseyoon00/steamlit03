
import streamlit as st
import numpy as np
from streamlit_chat import message


assistant = client.beta.assistants.create(
    instructions = "you are a chatbot",
    model = "gpt-4-turbo",
    tools = tools
)
thread = client.beta.threads.create(
  messages=[
    {
        "role":"user",
        # "content": "다음 이차방정식의 해를 구해줘: 15x^2 - 2x+1.2=0"
    }
  ]
)


if prompt := st.chat_input("What is up?"):
  st.chat_message("user").markdown(prompt) 
  st.session_state.messages.append({"role": "user", "content": prompt}) 


 response = f"Echo: {prompt}"

 with st.chat_message("assistant"):
 st.markdown(response)

 st.session_state.messages.append({"role": "assistant", "content": response})







if "messages" not in st.session_state: ##메모리 초기화
 st.session_state.messages = [] 
