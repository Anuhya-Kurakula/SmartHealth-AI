import { useEffect, useState } from "react";

function Dashboard() {

  const [stats, setStats] = useState({

    total_chats: 0,

    recent_chats: []
  });

  useEffect(() => {

    fetch(
      "http://127.0.0.1:8000/api/dashboard/"
    )
      .then((response) => response.json())
      .then((data) => setStats(data));

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