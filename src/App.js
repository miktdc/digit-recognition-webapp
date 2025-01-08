import './App.css';
import UploadForm from './components/uploadForm.js';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Upload an image to get started:
        </p>
        <UploadForm />
        <a
          className="App-link"
          href="https://github.com/miktdc/digit-recognition-webapp"
          target="_blank"
          rel="noopener noreferrer"
        >
          GitHub repo
        </a>
      </header>
    </div>
  );
}

export default App;
