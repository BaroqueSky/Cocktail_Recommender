import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from typing import Any, Dict, List

from langchain import hub
from langchain.chains import create_history_aware_retriever

load_dotenv()

def run_llm(query: str, chat_history: List[Dict[str, Any]] = []):
    chat_histroy = []
    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, streaming=True)
    vectorstore = PineconeVectorStore(
        index_name=os.environ["INDEX_NAME"], embedding=embeddings )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    
    rephrase_prompt = hub.pull("langchain-ai/chat-langchain-rephrase")
    history_aware = create_history_aware_retriever(llm, retriever, rephrase_prompt)

    template = """你是一位親切的經典調酒推薦員。根據使用者的喜好以及以下提供的內容
    （經典調酒的描述），只推薦一款合適的經典調酒。
    如果使用者的喜好不明確或過於寬泛，請直接表明你不能了解，並且要求使用者提供更進一步的說明。

    內容：
    {context}

    使用者喜好：
    {question}

    你的推薦：
    """




    custom_rag_prompt = PromptTemplate.from_template(template)

    rag_chain = (
        {
            "context": {
                "input": lambda x: x["question"],
                "chat_history": lambda x: x["chat_history"],
            } | history_aware,
            "question": lambda x: x["question"],
        }
        | custom_rag_prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain.invoke({"question": query, "chat_history": chat_history})



if __name__ == "__main__":
    res = run_llm(query="請推薦一款威士忌基底的酒給我")
    print(res)