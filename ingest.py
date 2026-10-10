import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader,TextLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_classic.text_splitter import TokenTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_classic.vectorstores import FAISS

#Loading the pdf file
loader = PyPDFLoader("data\cv\SaraAllan_CV .pdf") 
documents = loader.load()

cert_loader = PyPDFLoader("data\certification\Sara_Allan_Certificates.pdf")
cert_documents = cert_loader.load()

github_loader = DirectoryLoader("data\github", 
    glob="**/*.md",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"}
)
github_documents = github_loader.load()

linkedIn_loader = PyPDFLoader("data\linkedin\Profile.pdf")
linkedIn_documents = linkedIn_loader.load()

portfolio_loader = WebBaseLoader("https://boisterous-beijinho-627488.netlify.app/")
portfolio_documents = portfolio_loader.load()

documents.extend(cert_documents)
documents.extend(github_documents)
documents.extend(linkedIn_documents)
documents.extend(portfolio_documents)

print("Total documents:", len(documents))

#Splitting the document into chunks
text_splitter = TokenTextSplitter(
    chunk_size = 500,
    chunk_overlap = 50
)

chunks = text_splitter.split_documents(documents)
print("total chunks:", len(chunks))

#Creating embeddings for the chunks using HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}                         
)

#storing the embeddings in a vector store using FAISS
vectors = embeddings.embed_documents([chunk.page_content for chunk in chunks])
vectorDB = FAISS.from_documents(chunks, embeddings)
vectorDB.save_local("faiss_index")

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

print("API key found:", api_key is not None)

llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/free",
    temperature=0.8
)

response = llm.invoke("Say hello in one sentence.")

print(response.content)

