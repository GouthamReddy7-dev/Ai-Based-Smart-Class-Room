import { UseQuestions } from "./zustand_slice"
import { useState } from "react"
export default function StudentsQuestions(){
    const{questions}=UseQuestions()
    console.log(questions)
    const [opt,setopt]=useState({})
    const[score,setscore]=useState(-1)
    function appendvalues(questionIndex,optionIndex){
        setopt(priv=>({...priv,[questionIndex]:optionIndex}))
    }
        
    function getfinalscore(){
    const final = Object.values(opt) // selected answers
    const original = questions.map(q => q.answer) // correct answers

    let sc = 0

    for(let i=0;i<final.length;i++){
        if(final[i] === original[i]){
            sc++
        }
    }

    setscore(sc)
}
    return(
        <>
        {questions.length>0?
        (<>
        <h1>Questions : </h1>
        {questions.map((item,index)=>(
        <div key={index}>
            <h1>{item.question}</h1>
            <br />
            {item.options.map((option,i) => (
                <lable key={i}><input type="radio" value={i} name={`question-${index}`} onChange={()=>appendvalues(index,i)}/>{option} <br /> <br /></lable>
                
            )   
            )}
        </div>
    ))}
        </>)
        :
        (<>
        <h1>No Questions</h1>
        </>)}
        <br />
        <button onClick={getfinalscore}>Submit</button>
        <br />
        <br />
        <div style={{display:score>0?"block":"none"}}>
            <h1>Your Score:{score}/5 </h1>
        </div>
        </>
    )
}

/*{score>0?(<div>
            <h1>Your Score:{score} </h1>
        </div>):(<h1></h1>)} */