from cocktail_llm import run_llm
import streamlit as st
from streamlit_chat import message

st.header("經典調酒推薦機器人")


if st.button("清空對話"):
    st.session_state.clear()
    st.rerun()

prompt = st.chat_input("今天想找甚麼樣的調酒？")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if prompt:

    st.session_state["messages"].append({"role": "user", "content": prompt})
    chat_history = st.session_state["messages"][-6:]
    with st.spinner("機器人思考中"):
            generated_response = run_llm(query=prompt, chat_history=chat_history)

    st.session_state["messages"].append({"role": "assistant", "content": generated_response})


    
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        message(msg["content"], is_user=True)
    else:
        message(msg["content"])