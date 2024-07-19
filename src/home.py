import streamlit as st
from st_pages import Page, show_pages
import streamlit.components.v1 as components
import json
import openai
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.exc import ProgrammingError
import pandas as pd



# Add a robot emoji icon and set the tab name
st.set_page_config(page_title="Data Bot", page_icon="🤖")

st.subheader("Data Bot - AI-Powered Database Chatbot")

with st.sidebar:
    show_pages([
        Page("home.py", "Home"),
        Page("main.py", "ChatBot"),
        
    ])
    
    
    
   
   
    

with st.expander("How to Use the Chatbot Assistant", expanded=False):
    st.markdown("""
    **Welcome to the Chatbot Assistant!** Here's a quick guide:

    1. **Database Connection**: 
        - Visit the `Database Connection` tab.
        - Connect with a sample database or use yours.
        - Fill in the details and hit `connect`.

    2. **Language Model Settings**: 
        - Go to `Language Model Settings` tab.
        - Select a model or customize one.
        - Press `save` when done.

    3. **Chat with the Bot**: 
        - Switch to the `Chatbot` tab.
        - Type your questions and get real-time responses.

    4. **Reset Chat**: 
        - Use `Clear Chat History` in the sidebar for a fresh start.

    5. **About & Contact**: 
        - Know more about this bot in the `About & Contact` tab.

    Dive in and enjoy the experience! 🚀📊
    """)
    
