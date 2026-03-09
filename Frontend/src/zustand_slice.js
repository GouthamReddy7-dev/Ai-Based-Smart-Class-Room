import { create } from "zustand";
import {persist} from "zustand/middleware";

export const UseQuestions=create(
    persist(
        (set)=>({
            questions:[],
            AddQuestions:(item)=>
                set({questions:item}),
            ClearQuestions:()=>
                set({questions:[]})
        }),
        {
            name:"question-storage"
        }
    )
)



/*const UseQuestions=create(
    persist(
        (set)=>({
            questions:[],
            AddQuestions:(item)=>
                set((state)=>({ //best for cart but not for thiss
                    questions:[...state.questions,item]
                })),
        })
    )
) */