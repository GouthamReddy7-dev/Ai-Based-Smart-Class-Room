from langchain_google_genai import ChatGoogleGenerativeAI

apikey="Your Api Key"
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=apikey,temperature=0.7)


from langchain.document_loaders.csv_loader import CSVLoader
loder=CSVLoader(file_path="react_faq_75_questions.csv",source_column="prompt",encoding="latin-1") # if utf-8 dosent work then use this : latin-1
data=loder.load()

from langchain.embeddings import HuggingFaceEmbeddings
embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")



from langchain.vectorstores import FAISS
vectorDB=FAISS.from_documents(documents=data,embedding=embeddings)


vectorDB.save_local("RAG_index")

retriver=vectorDB.as_retriever()


from langchain.chains import RetrievalQA
chain=RetrievalQA.from_chain_type(llm=llm,chain_type="stuff",retriever=retriver,return_source_documents=True)




from flask import Flask,request,jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/Senddata",methods=["POST"])
def getdata():
    data=request.get_json()
    ans=data.get("datas")
    print(ans)
    newanswer=chain(ans)
    print(newanswer["result"])
    return jsonify({'result':newanswer["result"]})
app.run(debug=True,host="0.0.0.0")