import React from "react";
import UploadForm from "./Components/UploadForm";

function App() {
  return (
    <div style={{ backgroundColor: "#ffffff", height: "100vh" }}>
      <UploadForm />
      <a
        className="App-link mx-1 text-black"
        href="https://github.com/miktdc/digit-recognition-webapp"
        target="_blank"
        rel="noopener noreferrer"
      >
        GitHub Repository
      </a>
    </div>
  );
}

export default App;


