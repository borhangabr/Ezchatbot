import streamlit as st
from streamlit_chat import message
from langchain.chat_models import ChatOpenAI
from langchain.schema import(SystemMessage,HumanMessage,AIMessage)
from dotenv import load_dotenv

def main():
    load_dotenv()

    st.set_page_config(
        page_title="your own CHATBOT ",
        page_icon="🤖"
    )

    chat=ChatOpenAI(temperature=0)

    if "messages" not in st.session_state:
        st.session_state.messages=[SystemMessage(content="your name is reyna and you should reply in a rude way")]

    st.header("Welcome to Reyna ChatBot 🤖☢️")

    with st.sidebar:
        user_input=st.text_input("Your message: ",key="user_input")

        if user_input:
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner("Hmmmmmmm...."):
                response=chat(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))

    messages=st.session_state.get('messages',[])
    cnt=0
    for msg in messages[1:]:
        if cnt % 2 ==0:
            message(msg.content,is_user=True,key=str(cnt)+"user")
        else:
            message(msg.content,is_user=False,key=str(cnt)+'AI')
        cnt+=1

if __name__ =='__main__':
    main()
