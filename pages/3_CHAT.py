
import streamlit as st
import numpy as np
from streamlit_chat import message
from openai import OpenAI

client = st.session_state.get('openai_client', None)


message("My message") 
message("Hello bot!", is_user=True)  # align's the message to the right



if "messages" not in st.session_state:
 st.session_state.messages = [] 
