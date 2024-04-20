import logo from "./logo.svg";
import "./App.css";
import Chat from "./components/chat/chat";
import FileUpload from "./components/fileupload/fileupload"; // Import the FileUpload component

function App() {
  const handleFileUpload = (e) => {
    console.log(e);
  };
  return (
    <div className="App">
      <FileUpload onFileUpload={handleFileUpload} />{" "}
      {/* Render the FileUpload component */}
      <Chat />
    </div>
  );
}

export default App;
