import React, { useState } from "react";
import axios from "axios";

const Chat = () => {
  const [conversation, setConversation] = useState([
    {
      role: "system",
      content:
        "Your name is Jarvis, you are my personal assistant, and will always introduce youself as such. You will refer to me as My Lord",
    },
    { role: "user", content: "Introduce yourself." },
  ]);

  const [inputMessage, setInputMessage] = useState("");

  const apiUrl = "http://localhost:1234/v1/chat/completions";

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
