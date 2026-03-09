from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms import Ollama
#from langchain_ollama import OllamaLLM
apikey="Your Api Key"
#llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=apikey,temperature=0.7)#took 35 seconds
llm=Ollama(model="llama3.1:8b",temperature=0.7)

from langchain.document_loaders.csv_loader import CSVLoader
loder=CSVLoader(file_path="react_faq_75_questions.csv",source_column="prompt",encoding="latin-1") # if utf-8 dosent work then use this : latin-1
data=loder.load()

#txt data loading 

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_loader=TextLoader(file_path="transscript.txt",encoding="utf-8")
text_docs=text_loader.load()


text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)

text_documents=text_splitter.split_documents(text_docs)

from langchain.embeddings import HuggingFaceEmbeddings
embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")



from langchain.vectorstores import FAISS
vectorDB=FAISS.from_documents(documents=data+text_documents,embedding=embeddings)


vectorDB.save_local("RAG_index")

retriver=vectorDB.as_retriever()


from langchain.prompts import PromptTemplate

prompt=PromptTemplate(input_variables=["context","question"],template="""
You are a strict question answering system.
Use ONLY the information present in the context below.
If the answer to the question is NOT explicitly present in the context,
reply with EXACTLY the following sentence and nothing else:
sorry i couldnot find it i will send it to teacher.
and do not give any other explanation.
                      
context:
{context}               

Question:
{question}

Answer:""")

from langchain.chains import RetrievalQA
chain=RetrievalQA.from_chain_type(llm=llm,chain_type="stuff",retriever=retriver,return_source_documents=True,chain_type_kwargs={"prompt": prompt})

answer=chain("What is React and the student name to be what ?")
print(answer["result"])
"""  answer=chain("What is React and the student name to be what ?")
React is a JavaScript library for building user interfaces, mainly for single-page applications.
The student name to be passed is Rahul."""