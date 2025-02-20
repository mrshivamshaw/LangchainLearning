import streamlit as st
import requests

def responseFromOpenAI(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",json={"input":{"topic":input_text}})
    return response.json()['output']['content']
def responseFromOllama(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",json={"input":{"topic":input_text}})
    return response.json()['output']

st.title("Learning Langserve")
input_text1=st.text_input("Enter the topic for essay")
input_text2=st.text_input("Enter the topic for poem")

if input_text1:
    st.write(responseFromOpenAI(input_text1))
if input_text2:
    st.write(responseFromOllama(input_text2))