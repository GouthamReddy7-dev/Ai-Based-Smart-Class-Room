import express from "express"
import cors from "cors"
import mongoose from "mongoose"

const app=express()

app.use(cors())

app.use(express.json())

mongoose.connect("mongodb://localhost:27017/question_Db")

const mongoschema=new mongoose.Schema({
    question:String
})

const questionmodel=mongoose.model("questions",mongoschema)

app.post("/dbsend",(req,res)=>{
    const {question}=req.body
    console.log(question)
    questionmodel.create(req.body)
    res.json({message:"sended successfully"})
})

app.get("/getdata",(req,res)=>{
    questionmodel.find()
    .then(result=>res.json(result))
    .catch(err=>res.json(err))
})

app.listen(3001,()=>{
    console.log("server is listening !")
})