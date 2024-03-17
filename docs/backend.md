# Steps to create the Backend for the Chatbot

These are the required steps in order to build the backend for the langchain/streamlit chatbot utilizing AWS Bedrock.

## 1. Import Modules

```python
import os
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversation.base import ConversationChain
```

## 2. Write a function to invoke the model

```python
def demo_chatbot():
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
```
