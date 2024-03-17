import os
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversation.base import ConversationChain
from typing import Any


def demo_chatbot() -> Bedrock:
    llm = Bedrock(
        credentials_profile_name="default",
        model_id="meta.llama2-70b-chat-v1",
        model_kwargs={
            "temperature": 0.5,
            "top_p": 0.9,
            "max_gen_len": 512
        }
    )

    return llm

# Create the ConversationBufferMemory
def demo_memory(llm: Bedrock) -> ConversationBufferMemory:
    memory = ConversationBufferMemory(
        llm=llm,
        max_token_limit=512
    )

    return memory

# Create the ConversationChain
def demo_chain(llm: Bedrock, memory: ConversationBufferMemory) -> ConversationChain:
    llm_conversation = ConversationChain(
        llm=llm,
        memory=memory
    )

    return llm_conversation


# Test the backend
"""llm = demo_chatbot()
memory = demo_memory(llm=llm)
chain = demo_chain(llm=llm, memory=memory)

answer = chain.predict(input="Hey how are you doing?")
print(answer)

print("\n\n")
print("-" * 50)
print("\n\n")

answer2 = chain.predict(input="What was the first question I asked you?")
print(answer2)"""
