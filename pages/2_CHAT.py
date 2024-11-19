!pip install streamlit-chat 

import streamlit as st
import numpy as np
from streamlit_chat import message


prompt = st.chat_input("Say something")
if prompt:
    with st.chat_message("user"):
