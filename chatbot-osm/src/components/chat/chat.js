import React, { useState } from "react";
import axios from "axios";

const Chat = () => {
  const [conversation, setConversation] = useState([]);

  const [inputMessage, setInputMessage] = useState("");

  const apiUrl = "http://localhost:8080/chat-completion";

  const handleSendMessage = async () => {
    const newConversation = [
      ...conversation,
      { role: "user", content: inputMessage },
    ];
    setConversation(newConversation);
    setInputMessage("");

    try {
      const response = await axios.post(apiUrl, {
        messages: newConversation,
        temperature: 0.7,
        max_tokens: -1,
        stream: false,
      });

      const botReply = response.data.choices[0].message.content;
      setConversation([
        ...newConversation,
        { role: "assistant", content: botReply },
      ]);
    } catch (error) {
      console.error("Error sending message:", error);
    }
  };

  return (
    <div>
      <div style={{ maxHeight: "300px", overflowY: "auto" }}>
        {conversation.map((message, index) => (
          <div key={index} className={message.role}>
            {message.content}
          </div>
        ))}
      </div>
      <div>
        <input
          type="text"
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          placeholder="Type your message..."
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chat;
