
import streamlit as st
import numpy as np
from streamlit_chat import message


if prompt := st.chat_input("What is up?"):
  st.chat_message("user").markdown(prompt) 
  st.session_state.messages.append({"role": "user", "content": prompt}) 
  response = f"Echo: {prompt}"
  with st.chat_message("assistant"):
    st.markdown(response)
  st.session_state.messages.append({"role": "assistant", "content": response})





if "messages" not in st.session_state: ##메모리 초기화
 st.session_state.messages = [] 

for msg in st.session_state.messages: ##메세지 구분
 with st.chat_message(msg["role"]):
 st.markdown(msg["content"])
