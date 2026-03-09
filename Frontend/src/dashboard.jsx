import axios from "axios";
import { useEffect, useState } from "react";
import "./Dashboard.css";

function Dashboard() {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:3001/getdata")
      .then((res) => setQuestions(res.data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div className="dashboard-container">
      <h2 className="dashboard-title"> Live Class Doubts</h2>

      <div className="question-list">
        {questions.length === 0 ? (
          <div className="empty-state">
            No doubts yet — students are following well
          </div>
        ) : (
          questions.map((item, index) => (
            <div className="question-card" key={index}>
              <div className="question-header">
                <span className="question-number">
                  #{index + 1}
                </span>
                <span className="status-badge">
                  UNANSWERED
                </span>
              </div>

              <p className="question-text">
                {item.question}
              </p>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default Dashboard;