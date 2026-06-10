import { useState, useEffect, useRef } from "react";
import "./App.css";

function App() {

  const [question, setQuestion] = useState("");
  const [chatHistory, setChatHistory] = useState([]);
  const [isTyping, setIsTyping] = useState(false);

  const [darkMode, setDarkMode] = useState(
    localStorage.getItem("theme") === "dark"
  );

  const [language, setLanguage] = useState("en-US");

  const bottomRef = useRef(null);

  const sampleQuestions = [
    "What is dengue?",
    "How can dengue be prevented?",
    "What are the symptoms of malaria?",
    "How to maintain hand hygiene?",
    "What is first aid?",
    "Tips for healthy nutrition"
  ];

  // Dark Mode
  useEffect(() => {

    if (darkMode) {

      document.body.classList.add("dark");
      localStorage.setItem("theme", "dark");

    } else {

      document.body.classList.remove("dark");
      localStorage.setItem("theme", "light");

    }

  }, [darkMode]);

  // Auto Scroll
  useEffect(() => {

    bottomRef.current?.scrollIntoView({
      behavior: "smooth"
    });

  }, [chatHistory]);
    // Voice Input
  const startListening = () => {

    const SpeechRecognition =
      window.SpeechRecognition ||
      window.webkitSpeechRecognition;

    if (!SpeechRecognition) {

      alert("Speech Recognition not supported.");

      return;
    }

    const recognition = new SpeechRecognition();

    recognition.lang = language;

    recognition.start();

    recognition.onresult = (event) => {

      const transcript =
        event.results[0][0].transcript;

      setQuestion(transcript);

      setTimeout(() => {

        askQuestion(transcript);

      }, 300);

    };

  };

  // Voice Output
  const speakAnswer = (text) => {

    window.speechSynthesis.cancel();

    const speech =
      new SpeechSynthesisUtterance(text);

    speech.lang = language;

    window.speechSynthesis.speak(speech);

  };

  // Ask Question
  const askQuestion = async (
    inputQuestion = question
  ) => {

    if (!inputQuestion.trim()) return;

    setIsTyping(true);

    try {

      // Local backend
      const response = await fetch(
        `http://127.0.0.1:8000/api/chat/?question=${encodeURIComponent(inputQuestion)}`
      );

      const data = await response.json();

      const newChat = {

        question: inputQuestion,

        answer:
          data.answer ||
          "No response received.",

        sources:
          data.sources || [],

        time:
          new Date().toLocaleTimeString()

      };

      setChatHistory(prev => [

        ...prev,

        newChat

      ]);

      setQuestion("");

    }

    catch {

      setChatHistory(prev => [

        ...prev,

        {

          question: inputQuestion,

          answer:
            "Unable to connect to SmartHealth AI.",

          sources: [],

          time:
            new Date().toLocaleTimeString()

        }

      ]);

    }

    setIsTyping(false);

  };

  return (

    <div className="app">
            {/* Sidebar */}
      <div className="sidebar">

        <h2>🩺 SmartHealth AI</h2>

        <p className="tagline">
          Your Personal Healthcare Assistant
        </p>

        <button
          className="new-chat-btn"
          onClick={() => setChatHistory([])}
        >
          + New Chat
        </button>

        <button
          className="theme-btn"
          onClick={() => setDarkMode(!darkMode)}
        >
          {
            darkMode
              ? "☀️ Light Mode"
              : "🌙 Dark Mode"
          }
        </button>

        <div className="sidebar-section">

          <h3>Sample Questions</h3>

          {

            sampleQuestions.map((q, index) => (

              <button
                key={index}
                className="sample-btn"
                onClick={() => askQuestion(q)}
              >

                {q}

              </button>

            ))

          }

        </div>

        <div className="sidebar-section">

          <h3>Recent Questions</h3>

          {

            chatHistory.length === 0 ?

              <p>No chats yet</p>

              :

              chatHistory.map((chat, index) => (

                <div
                  key={index}
                  className="history-item"
                >

                  {chat.question}

                </div>

              ))

          }

        </div>

      </div>


      {/* Main Content */}
      <div className="main-content">

        <div className="header">

          <h1>🩺 SmartHealth AI Assistant</h1>

          <p className="subtitle">

            AI-powered healthcare guidance and awareness assistant

          </p>

        </div>


        <div className="chat-container">

          {

            chatHistory.length === 0 && (

              <div className="welcome">

                <h2>👋 Welcome to SmartHealth AI</h2>

                <p>

                  Ask health-related questions powered by WHO documents and AI.

                </p>

              </div>

            )

          }


          {

            chatHistory.map((chat, index) => (

              <div key={index}>

                <div className="user-message">

                  👤 {chat.question}

                </div>

                <div className="bot-message">

                  🤖 {chat.answer}

                  <br />
                  <br />

                  <button
                    className="speak-btn"
                    onClick={() => speakAnswer(chat.answer)}
                  >

                    🔊 Speak

                  </button>

                  {

                    chat.sources.length > 0 && (

                      <div className="source-box">

                        <strong>📄 Sources</strong>

                        {

                          chat.sources.map((source, idx) => (

                            <div key={idx}>

                              • {source}

                            </div>

                          ))

                        }

                      </div>

                    )

                  }

                  <div className="time">

                    {chat.time}

                  </div>

                </div>

              </div>

            ))

          }


          {

            isTyping && (

              <div className="bot-message">

                🤖 SmartHealth AI is thinking...

              </div>

            )

          }

          <div ref={bottomRef}></div>

        </div>


        {/* Language */}
        <div className="language-selector">

          <label>🌐 Language:</label>

          <select
            value={language}
            onChange={(e) =>
              setLanguage(e.target.value)
            }
          >

            <option value="en-US">English</option>
            <option value="te-IN">Telugu</option>
            <option value="hi-IN">Hindi</option>

          </select>

        </div>


        {/* Input */}
        <div className="input-area">

          <input
            type="text"
            placeholder="Type your health question here..."
            value={question}
            onChange={(e) =>
              setQuestion(e.target.value)
            }
            onKeyDown={(e) =>
              e.key === "Enter" &&
              askQuestion()
            }
          />

          <button
            onClick={() => askQuestion()}
          >

            ➤ Send

          </button>

          <button
            className="voice-btn"
            onClick={startListening}
          >

            🎤

          </button>

        </div>


        <div className="footer">

          Powered by Groq • Django • React • RAG

        </div>

      </div>

    </div>

  );

}

export default App;
    