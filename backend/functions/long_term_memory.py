import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain import OpenAI
import pinecone
from langchain.chains import RetrievalQA
from decouple import config
import openai
import json

openai.api_key = config("OPEN_AI_KEY")
pinecone.init(api_key="c8ea84aa-f559-4d1a-9a01-f54c2244fc28", environment="gcp-starter")

def long_term_message_and_response(recent_chat):
    print('Hello VectorStore!')
    loader = TextLoader('stored_data_long_term.json')
    document = loader.load()

    text_splitter = CharacterTextSplitter(separator="role", is_separator_regex=False, chunk_size=50, chunk_overlap=0)
    #Change this such that the text splitter splits at every 10th iteration of the word role, irrespective of chunk size.

    texts = text_splitter.split_documents(documents=document)

    print("TEXTS =", texts)
    print("length of texts = ", len(texts))
    
    embeddings = OpenAIEmbeddings(openai_api_key=openai.api_key)
    docsearch = Pinecone.from_documents(texts, embeddings, index_name="medium-blogs-embedding-index")

    qa = RetrievalQA.from_chain_type(llm=OpenAI( openai_api_key=openai.api_key), chain_type="stuff", retriever=docsearch.as_retriever())

    #For the query, should we pass the entire recent chat history as the query, or just the most recent question?
  
    # Serialize the list to a JSON string
    chat_string = json.dumps(recent_chat)
    print("CHAT STRING=", chat_string)

    result = qa({"query":chat_string})
    print("RESULT = ", result)

    return result