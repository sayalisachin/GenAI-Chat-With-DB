import json

import openai
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.sql import text
from st_pages import Page, show_pages

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
        - You can use the sample Chinook DB to ask questions
        - Connect with a your own database and enter your API key.
        

    2. **Language Model Settings**: 
        - This Model uses OpenAI

    3. **Chat with the Bot**: 
        - Switch to the `Chatbot` tab.
        - Type your questions and get real-time responses.

    4. **Reset Chat**: 
        - Use `Clear Chat History` in the sidebar for a fresh start.

    **Dive in and enjoy the experience! 🚀📊**
        Team : Vance
        (Sayali Sachin Chorge)
                
    """)
    
