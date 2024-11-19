!pip install streamlit_chat
from streamlit_chat import message

import streamlit as st
import numpy as np



if prompt := st.chat_input("What is up?"):
  st.chat_message("user").markdown(prompt) 
  st.session_state.messages.append({"role": "user", "content": prompt}) 
