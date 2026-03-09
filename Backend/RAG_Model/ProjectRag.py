from langchain_community.llms import Ollama
from langchain.document_loaders import CSVLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
llm=Ollama(model="llama3.1:8b",temperature=0.7)

#loading csv file

loader=CSVLoader(file_path="react_faq_75_questions.csv",source_column="prompt",encoding="latin-1")
data=loader.load()

#loading transcribed data

text_data=TextLoader(file_path="transscript.txt",encoding="utf-8")
text_loader=text_data.load()

#splitting into chunkes
text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
splitted_text=text_splitter.split_documents(text_loader)

#embeddings
embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#initializing vector store
vector_db=FAISS.from_documents(documents=data+splitted_text,embedding=embeddings)
vector_db.save_local("Project_rag_index")
retriver=vector_db.as_retriever()

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

#chain
chain=RetrievalQA.from_chain_type(llm=llm,chain_type="stuff",retriever=retriver,return_source_documents=True,chain_type_kwargs={"prompt": prompt})
answer=chain("What is React and the student name to be what ?")
print(answer["result"])