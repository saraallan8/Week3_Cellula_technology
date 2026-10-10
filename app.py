import os
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_classic.vectorstores import FAISS
from IPython.display import display, Markdown

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

vectorDB = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/free",
    temperature=0.8
)

temp = """
You are a helpful assistant answering questions about Sara Allan.

Answer the question using only the information provided in the context.
If the answer is not available in the context, say you don't know.

Keep the answer clear and concise.

## Context:
{context}

## Question:
{Question}
"""

temp = PromptTemplate.from_template(temp)

query = "What projects did Sara work on?"

similar_docs = vectorDB.similarity_search_with_score(query, k=4)

context = []

for i in similar_docs:
    context.append(i[0].page_content)

context = "\n\n".join(context)

prompt = temp.invoke({
    "context": context,
    "Question": query
})

response = llm.invoke(prompt)

print(response.content)