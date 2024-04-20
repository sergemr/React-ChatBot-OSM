import React, { useEffect, useState } from "react";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import CircularProgress from "@mui/material/CircularProgress";
import axios from "axios";
import { Divider } from "@mui/material";
import SpeechSynthesis from "speech-synthesis";
import SpeechSynthesisUtterance from "speech-synthesis";
const Chat = () => {
  const [conversation, setConversation] = useState([]);
  const [inputMessage, setInputMessage] = useState("");
  const [isPlaying, setIsPlaying] = useState(false);
  const [loading, setLoading] = useState(false);

  const apiUrl = "http://localhost:8080/chat-completion";
  const handlePlayResponse = (message, stop = false) => {
    if (stop) {
      speechSynthesis.cancel(); // Stop any ongoing speech synthesis
    } else {
      const utterance = new SpeechSynthesisUtterance(message);
      speechSynthesis.cancel(); // Stop any ongoing speech synthesis
      speechSynthesis.speak(utterance);
    }
  };
  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !loading && inputMessage.trim() !== "") {
      handleSendMessage();
    }
  };
  const handleSendMessage = async () => {
    const newConversation = [
      ...conversation,
      { role: "user", content: inputMessage },
    ];
    setConversation(newConversation);
    setInputMessage("");
    setLoading(true);

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

      //SpeechSynthesis(response.data.choices[0].message.content);
    } catch (error) {
      console.error("Error sending message:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        height: "100vh",
        padding: "16px",
        // backgroundColor: "#663399", // Rebecca Purple
        background: "linear-gradient(to bottom, #fff, rgb(247 240 255))",
        color: "#fff", // White text color
      }}
    >
      <h1 style={{ color: "rebeccapurple" }}>Chatbot</h1>

      <Divider sx={{ my: 2 }} />
      <div
        style={{
          flex: 1,
          overflowY: "auto",
          marginBottom: "16px",
          textAlign: "center",
          inset: "0",
        }}
      >
        {conversation.map((message, index) => (
          <div
            key={`row-${index}`}
            style={{ margin: "center", textAlign: "center", inset: "0" }}
          >
            <div
              key={index}
              style={{
                margin: "0px auto 8px auto",
                padding: "8px",
                borderRadius: "8px",
                maxWidth: "70%",
                alignSelf: message.role === "user" ? "flex-end" : "flex-start",
                backgroundColor:
                  message.role === "user" ? "#7e57c2" : "#00acc1",
              }}
            >
              <div dangerouslySetInnerHTML={{ __html: message.content }} />
              <br />
              <div>
                {" "}
                <Button
                  variant="contained"
                  color="secondary"
                  style={{
                    display:
                      message.role === "user"
                        ? "none"
                        : isPlaying
                        ? "none"
                        : "block",
                  }}
                  button
                  onClick={() => {
                    setIsPlaying(true);
                    SpeechSynthesis(message.content);
                  }}
                >
                  Play{" "}
                </Button>
                <Button
                  variant="contained"
                  style={{
                    display:
                      message.role === "user"
                        ? "none"
                        : isPlaying
                        ? "block"
                        : "none",
                  }}
                  button
                  onClick={() => {
                    handlePlayResponse(null, true);
                    setIsPlaying(false);
                  }} // Pass null to indicate stopping playback
                >
                  {" "}
                  Stop{" "}
                </Button>
              </div>
            </div>
          </div>
        ))}
        {loading && <CircularProgress color="secondary" />}
      </div>
      <div style={{ display: "flex", margin: "25px" }}>
        <TextField
          style={{ flex: 1, marginRight: "8px", color: "#fff" }}
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          placeholder="Type your message..."
          variant="outlined"
          size="small"
          color="secondary"
          InputProps={{
            style: { color: "rebeccapurple" },
          }}
          onKeyDown={handleKeyPress}
        />
        <Button
          style={{ backgroundColor: "#ff4081", color: "#fff" }}
          onClick={handleSendMessage}
          disabled={loading || inputMessage.trim() === ""}
        >
          Send
        </Button>
      </div>
    </div>
  );
};

export default Chat;
