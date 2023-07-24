import streamlit as st
from langchain.llms import OpenAI

#function to return response
def load_answer(question):
    llm=OpenAI(model_name='text-davinci-003',temperature=0)
    answer=llm(question)
    return answer

#App UI 

st.set_page_config(page_title='Lang Chain Demo',page_icon=':robot:')
st.header('Lang Chain Demo')

#get the user input
def get_input():
    input_text=st.text_input('You :',key='input')
    return input_text

user_input=get_input()
response=load_answer(user_input)

submit=st.button('generate')
if submit:
    st.subheader('answer')
    st.write(response)
