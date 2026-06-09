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
    "What is first aid?"
  ];

  useEffect(() => {
    if (darkMode) {
      document.body.classList.add("dark");
      localStorage.setItem("theme", "dark");
    } else {
      document.body.classList.remove("dark");
      localStorage.setItem("theme", "light");
    }
  }, [darkMode]);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth"
    });
  }, [chatHistory]);

  const speakAnswer = (text) => {
    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = language;
    window.speechSynthesis.speak(speech);
  };

  const startListening = () => {

    const SpeechRecognition =
      window.SpeechRecognition ||
      window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
      alert("Speech Recognition not supported");
      return;
    }

    const recognition = new SpeechRecognition();

    recognition.lang = language;

    recognition.start();

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setQuestion(transcript);
    };
  };

  const askQuestion = async (inputQuestion = question) => {

    if (!inputQuestion.trim()) return;

    setIsTyping(true);

    try {

      const response = await fetch(
        `https://smarthealth-ai-1.onrender.com/api/chat/?question=${encodeURIComponent(inputQuestion)}`
      );

      const data = await response.json();

      setChatHistory(prev => [
        ...prev,
        {
          question: inputQuestion,
          answer: data.answer,
          sources: data.sources || [],
          time: new Date().toLocaleTimeString()
        }
      ]);

      setQuestion("");

    } catch {

      setChatHistory(prev => [
        ...prev,
        {
          question: inputQuestion,
          answer: "Unable to connect to SmartHealth AI.",
          sources: [],
          time: new Date().toLocaleTimeString()
        }
      ]);

    }

    setIsTyping(false);
  };

  return (

    <div className="app">

      <div className="sidebar">

        <h2>🏥 SmartHealth AI</h2>

        <button onClick={() => setChatHistory([])}>
          + New Chat
        </button>

        <button onClick={() => setDarkMode(!darkMode)}>
          {darkMode ? "☀️ Light Mode" : "🌙 Dark Mode"}
        </button>

        <h3>Sample Questions</h3>

        {
          sampleQuestions.map((q, index) => (
            <button
              key={index}
              onClick={() => askQuestion(q)}
            >
              {q}
            </button>
          ))
        }

      </div>

      <div className="main-content">

        <h1>Health Awareness Assistant</h1>

        <div className="chat-container">

          {
            chatHistory.map((chat, index) => (

              <div key={index}>

                <div className="user-message">
                  👤 {chat.question}
                </div>

                <div className="bot-message">

                  🤖 {chat.answer}

                  <br /><br />

                  <button
                    onClick={() => speakAnswer(chat.answer)}
                  >
                    🔊 Speak
                  </button>

                </div>

              </div>

            ))
          }

          {
            isTyping && (
              <div className="bot-message">
                🤖 Typing...
              </div>
            )
          }

          <div ref={bottomRef}></div>

        </div>

        <div className="language-selector">

          <select
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
          >
            <option value="en-US">English</option>
            <option value="te-IN">Telugu</option>
            <option value="hi-IN">Hindi</option>
          </select>

        </div>

        <div className="input-area">

          <input
            type="text"
            value={question}
            placeholder="Ask a health question..."
            onChange={(e) => setQuestion(e.target.value)}
          />

          <button onClick={() => askQuestion()}>
            Send
          </button>

          <button onClick={startListening}>
            🎤
          </button>

        </div>

      </div>

    </div>
  );
}

export default App;