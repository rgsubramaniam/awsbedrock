import boto3
import os
import re
import json
import streamlit as st
from langchain.llms.bedrock import Bedrock
from langchain.embeddings import BedrockEmbeddings
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

bedrock = boto3.client(service_name = "bedrock-runtime",region_name = "us-east-1")
bedrock_embeding = BedrockEmbeddings(model_id="amazon.titan-embed-text-v2:0",client = bedrock)

def get_documents():
    loader = PyPDFDirectoryLoader("data")
    documents = loader.load()
    text_split = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
    docs = text_split.split_documents(documents)


    

