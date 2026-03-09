import Chatbot from "./Chatbot";
import Dashboard from "./dashboard";
import QuestionPage from "./questionPage";
import { BrowserRouter,Routes,Route } from "react-router-dom";
import StudentsQuestions from "./StudentsQuestionsPage";
function App() {
  return (
    <>
     <BrowserRouter>
     <Routes>
      <Route path="/" element={<Chatbot/>}/>
      <Route path="/admin" element={<Dashboard/>}/>
      <Route path="/questions" element={<QuestionPage/>}/>
      <Route path="/studentsquestions" element={<StudentsQuestions/>}/>
     </Routes>
     </BrowserRouter>
    </>
  )
}

export default App


/*<Chatbot />
     <Dashboard/> */