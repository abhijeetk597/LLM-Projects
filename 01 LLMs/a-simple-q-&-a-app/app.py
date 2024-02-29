import streamlit as st
from langchain_openai import OpenAI

# function to instantiate the model and return response
def load_answer(question):
    llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0)

    # invoke method to query the input
    answer = llm.invoke(question)
    return answer

# App UI
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

# Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

user_input = get_text()
response = load_answer(user_input)

submit = st.button("Generate")

if submit:
    st.subheader("Answer:")
    st.write(response)