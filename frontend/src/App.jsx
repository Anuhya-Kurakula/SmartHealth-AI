
import { useState } from "react";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [chatHistory, setChatHistory] = useState([]);

  const sampleQuestions = [
    "What is dengue?",
    "How can dengue be prevented?",
    "What are the symptoms of malaria?",
    "How to maintain hand hygiene?",
    "What is first aid?",
    "Tips for healthy nutrition"
  ];

  const askQuestion = async (inputQuestion = question) => {
    if (!inputQuestion.trim()) return;

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/chat/?question=${encodeURIComponent(
          inputQuestion
        )}`
      );

      const data = await response.json();

      const newChat = {
        question: inputQuestion,
        answer: String(data.answer || "No response received.")
      };

      setChatHistory((prev) => [...prev, newChat]);
      setQuestion("");
    } catch (error) {
      console.error(error);

      setChatHistory((prev) => [
        ...prev,
        {
          question: inputQuestion,
          answer: "Unable to connect to SmartHealth AI."
        }
      ]);
    }
  };

  return (
    <div className="app">

      {/* Sidebar */}
      <div className="sidebar">
        <h2>🏥 SmartHealth AI</h2>

        <div className="sidebar-section">
          <h3>Sample Questions</h3>

          {sampleQuestions.map((q, index) => (
            <button
              key={index}
              className="sample-btn"
              onClick={() => askQuestion(q)}
            >
              {q}
            </button>
          ))}
        </div>

        <div className="sidebar-section">
          <h3>Recent Questions</h3>

          {chatHistory.length === 0 ? (
            <p className="empty-text">No chats yet</p>
          ) : (
            chatHistory.map((chat, index) => (
              <div key={index} className="history-item">
                {chat.question}
              </div>
            ))
          )}
        </div>
      </div>

      {/* Main Chat Area */}
      <div className="main-content">

        <div className="header">
          <h1>Health Awareness Assistant</h1>
        </div>

        <div className="chat-container">

          {chatHistory.length === 0 && (
            <div className="welcome">
              <h2>Welcome 👋</h2>
              <p>
                Ask any health-related question based on WHO health documents.
              </p>
            </div>
          )}

          {chatHistory.map((chat, index) => (
            <div key={index}>
              <div className="user-message">
                👤 {chat.question}
              </div>

              <div className="bot-message">
                🤖 {chat.answer}
              </div>
            </div>
          ))}
        </div>

        <div className="input-area">
          <input
            type="text"
            placeholder="Ask a health question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) =>
              e.key === "Enter" && askQuestion()
            }
          />

          <button onClick={() => askQuestion()}>
            Send
          </button>
        </div>

      </div>
    </div>
  );
}

export default App;

