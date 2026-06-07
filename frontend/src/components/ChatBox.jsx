function ChatBox({ answer }) {
  return (
    <div style={{
      border: "1px solid gray",
      padding: "15px",
      marginTop: "20px"
    }}>
      <h3>AI Response</h3>
      <p>{answer}</p>
    </div>
  );
}

export default ChatBox;