from langchain_google_genai import ChatGoogleGenerativeAI

apikey="Your Api Key"
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=apikey,temperature=0.7)

#csv data loading
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








#embedding
from langchain.embeddings import HuggingFaceEmbeddings
embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


#vector database
from langchain.vectorstores import FAISS
vectorDB=FAISS.from_documents(documents=data+text_documents,embedding=embeddings)


vectorDB.save_local("RAG_index")

retriver=vectorDB.as_retriever()

#retriving the document
from langchain.chains import RetrievalQA
chain=RetrievalQA.from_chain_type(llm=llm,chain_type="stuff",retriever=retriver,return_source_documents=True)

answer=chain("explain virtual dom in detail") #I'm defining the student name to be what ?
print(answer["result"])