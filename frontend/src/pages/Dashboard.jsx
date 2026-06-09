import { useEffect, useState } from "react";

function Dashboard() {

  const [stats, setStats] = useState({
    total_chats: 0,
    recent_chats: []
  });

  useEffect(() => {

    fetch(
      "https://smarthealth-ai-1.onrender.com/api/dashboard/"
    )
      .then((response) => response.json())
      .then((data) => setStats(data))
      .catch((error) => {
        console.error("Dashboard Error:", error);
      });

  }, []);

  return (

    <div className="dashboard">

      <h1>📊 Dashboard</h1>

      <div className="card">

        <h2>Total Chats</h2>

        <p>{stats.total_chats}</p>

      </div>

      <h2>Recent Conversations</h2>

      {
        stats.recent_chats.map(
          (chat, index) => (
            <div
              key={index}
              className="recent-card"
            >
              {chat.question}
            </div>
          )
        )
      }

    </div>
  );
}

export default Dashboard;