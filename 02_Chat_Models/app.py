import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

# UI
st.set_page_config(page_title="LLM-LangChain Chat Model Demo", page_icon=":robot:")
st.header("Hey, I'm your Chat GPT")

if "sessionMessage" not in st.session_state:
    st.session_state.sessionMessage = [
        SystemMessage(content="You are a sarcastic AI Assistant")
    ]

def load_answer(question):
    st.session_state.sessionMessage.append(HumanMessage(content=question))
    assistant_answer = chat.invoke(st.session_state.sessionMessage)
    st.session_state.sessionMessage.append(AIMessage(content=assistant_answer.content))
    return assistant_answer.content

def get_text():
    input_text = st.text_input("You: ")
    return input_text


chat = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")

user_input = get_text()
submit = st.button("Generate")

if submit:

    response = load_answer(user_input)
    st.subheader("Answer:")

    st.write(response)
