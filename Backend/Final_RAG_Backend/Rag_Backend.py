from fastapi import FastAPI
from fastapi import UploadFile,File
from fastapi.middleware.cors import CORSMiddleware
import shutil
from pydantic import BaseModel
import os
from TextTranscribe import TranscribeText
from langchain_community.llms import Ollama
import json
app=FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=False,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )


"""class userdata(BaseModel):
    name:str
    email:str
    num:int"""

@app.post("/get_audio")
def getAudio(audio:UploadFile=File(...)): #(...) means this is required or =file(required=true)
    temp_path=f"temp_{audio.filename}"
    with open(temp_path,"wb") as buffer:
        shutil.copyfileobj(audio.file,buffer) #data is been copying from audio.file to temp_path
    Text_Data=TranscribeText(temp_path)
    llm=Ollama(model="llama3.1:8b",temperature=0.7)
    answer=llm.invoke(f"give me 5 questions and 4 options for each question with answer in json form from the following data(the questions and answers should be from the provided data only do not go out side of that data and do not give it by yourself. and only give the questions,options,answer for that no extra text and no extra response is required just give that ) : {Text_Data} ,and maintain this format : {newstr}")
    print(answer)
    clean = str(answer).replace("```json", "").replace("```", "").strip()
    data = json.loads(clean)
    #os.remove(temp_path)
    return {"quest":data}

newstr="""```json
{
  "questions": [
    {
      "question": "",
      "options": [],
      "answer": option number, example(0,1,2,3)
    },
    {
      "question": "",
      "options": [],
      "answer": option number, example(0,1,2,3)
    },
    {
      "question": "",
      "options": [],
      "answer": option number, example(0,1,2,3)
    },
    {
      "question": "",
      "options": [],
      "answer": option number, example(0,1,2,3)
    },
    {
      "question": "",
      "options": [],
      "answer": option number, example(0,1,2,3)
    }
  ]
}
```"""



raw_string="""```json
{
  "questions": [
    {
      "question": "What does the min function do in CSS?",
      "options": ["Sets the smallest of a list of expressions as the value of a CSS property", "Returns the biggest of a list of expressions as the value of a property", "Ensures the final value never goes below min, never goes above max, and always stays at the preferred value while it fits between both", "Is used to specify a minimum size"],
      "answer": 0
    },
    {
      "question": "How can the max function be useful?",
      "options": ["To specify a maximum size", "To specify a minimum size", "To return the biggest of a list of expressions as the value of a property", "To combine different CSS units"],
      "answer": 1
    },
    {
      "question": "What is the purpose of the clamp function?",
      "options": ["Ensures the final value never goes below min, never goes above max, and always stays at the preferred value while it fits between both", "Is used to specify a minimum size", "Returns the biggest of a list of expressions as the value of a property", "Sets the smallest of a list of expressions as the value of a CSS property"],
      "answer": 0
    },
    {
      "question": "How can you use the clamp function for responsive font sizes?",
      "options": ["By using it with viewport-based units like VW", "By combining it with zoomable units like REM", "By using it to specify a minimum and maximum font size", "By using it to set a single font size"],
      "answer": 3
    },
    {
      "question": "Why is it dangerous to use only viewport-based units for font sizes?",
      "options": ["Because they don't respond to user zooming", "Because they are not flexible enough", "Because they are too large on small screens", "Because they are too small on large screens"],
      "answer": 0
    }
  ]
}
```"""
@app.get("/getaudio")
def sendaudio():
    clean = raw_string.replace("```json", "").replace("```", "").strip()
    data = json.loads(clean)

    return {"quest":data}
#to run uvicorn FileName:app --reload


































"""from fastapi  import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import UploadFile,File
import shutil
app=FastAPI()

app.add_middleware(CORSMiddleware)



@app.post("/get_audio")
def getAudio(audio:UploadFile=File(...)): #(...) means this is required or =file(required=true)
    temp_path=f"temp_{audio.filename}"
    with open(temp_path,"wb") as buffer:
        shutil.copyfileobj(audio.file,buffer) #data is been copying from audio.file to temp_path


    return {"status":"OK"}"""