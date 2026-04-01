import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

st.title("AI Chatbot")

user_input = st.text_input("You:")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}]
    )
    
    bot_reply = response.choices[0].message.content
    st.write("Bot:", bot_reply)
