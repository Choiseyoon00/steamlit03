
import streamlit as st
import numpy as np
from streamlit_chat import message
from openai import OpenAI

client = st.session_state.get('openai_client', None)

def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text 

user_input = get_text()
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output["generated_text"])


if "messages" not in st.session_state:
 st.session_state.messages = [] 
