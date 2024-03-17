import streamlit as st
import backend


llm = backend.demo_chatbot()
memory = backend.demo_memory(llm=llm)
chain = backend.demo_chain(
    llm=llm,
    memory=memory
)

st.title("Welcome to MARCO - Might Accidentially Return Correct Outputs")

if "llm" not in st.session_state:
    st.session_state.llm = llm

if "memory" not in st.session_state:
    st.session_state.memory = memory

if "chain" not in st.session_state:
    st.session_state.chain = chain

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

input_text = st.chat_input("Chat with MARCO")
if input_text:
    with st.chat_message("user"):
        st.markdown(input_text)
    
    st.session_state.chat_history.append({
        "role": "user",
        "text": input_text
    })

    chat_response = st.session_state.chain.predict(input=input_text)
    print(chat_response)
    print("Type:")
    print(type(chat_response))

    with st.chat_message("assistant"):
        st.markdown(chat_response)
    
    st.session_state.chat_history.append({
        "role": "assistant",
        "text": chat_response
    })
