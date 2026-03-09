import { useState } from "react"
import {UseQuestions} from "./zustand_slice"
import axios from "axios"
export default function QuestionPage(){
    const [audio,getaudio]=useState()
    const [ques,getques]=useState([])
    const [opt,setopt]=useState({})
    const [finalans,setfinalans]=useState([])
    const[OriginalAns,SetOriginalAns]=useState([])
    const {questions,AddQuestions}=UseQuestions()
    function send_audio(){
        if(!audio){
            alert("Please Select THhe File")
        }
        const formdata=new FormData()
        formdata.append("audio",audio)
        axios.post("http://localhost:8000/get_audio",formdata)
        .then(res=>{console.log(res.data.quest.questions)
            getques(res.data.quest.questions)
            AddQuestions(res.data.quest.questions)
        })
        .catch(err=>console.log(err))
    }
    function getquestions(){
        axios.get("http://localhost:8000/getaudio")
        .then(res=>{console.log(res.data.quest.questions)
            getques(res.data.quest.questions)
            //getques(JSON.parse(res.data.quest))
            AddQuestions(res.data.quest.questions)
        })
        .catch(err=>console.log(err))
    }
    function appendvalues(questionIndex,optionIndex){
        setopt(priv=>({...priv,[questionIndex]:optionIndex}))
    }
    function makearray(){
        console.log(opt)
        setfinalans(Object.values(opt))
        

    }
    function getoriginalanswers(){
        //SetOriginalAns(priv=>[...priv,ques.forEach((item)=>{return item.answer})])
        ques.map((item)=>{  //for setting the answers into an array !
            SetOriginalAns(priv=>[...priv,item.answer])
        })
        let apl=[]
        //ques.forEach((item)=>{OriginalAns.push(item.answer)})
        console.log(OriginalAns)
    }
    return(
    <>
    <input type="file" accept="audio/*" onChange={(e)=>getaudio(e.target.files[0])} />
    <button onClick={send_audio}>Send Audio</button>
    <button onClick={getquestions}>Get questions</button>
    <br />
    <br />
    {ques.length>0?(<>
    <h1>Questions : </h1>
    {ques.map((item,index)=>(
        <div key={index}>
            <h1>{item.question}</h1>
            <br />
            {item.options.map((option,i) => (
                <lable key={i}><input type="radio" value={i} name={`question-${index}`} onChange={()=>appendvalues(index,i)}/>{option} <br /> <br /></lable>
                
            )   
            )}
        </div>
    ))}
    
    </>) :<h1>No questions available right now!</h1>}
    <button onClick={makearray}>Show options</button>
    <button onClick={()=>console.log(finalans)}>s</button>
    <button onClick={getoriginalanswers}>Get original answers</button>
    <button onClick={()=>console.log(OriginalAns)}>just</button>
    </>
    )
}



// task : combine the make array,and get original answer


/*

name={`question-${index}`} this is used to give one name to one question so that you cannot choose other question




<input type="file" accept="audio/*" onChange={(e)=>getaudio(e.target.files[0])} />
    <button onClick={send_audio}>Send Audio</button>
    <button onClick={getquestions}>Get questions</button>
    <br />
    <br />
    {ques.length>0?(<>
    <h1>Questions : </h1>
    {ques.map((item,index)=>(
        <div key={index}>
            <h1>{item.question}</h1>
            <br />
            {item.options.map((option,i) => (
                <lable key={i}><input type="radio" value={i} onChange={appendvalues}/>{option} <br /> <br /></lable>
                
            )   
            )}
        </div>
    ))}
    
    </>) :<h1>No questions available right now!</h1>}
    <button onClick={()=>console.log(opt)}>Show options</button>
    </>
    
    
    
    
    use form to handel empty values*/