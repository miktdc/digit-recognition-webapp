import React, { useState } from "react";

const UploadForm = () => {
  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      alert("Please upload a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:5001/predict", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      console.log("Prediction:", result.prediction);
      setPrediction(result.prediction);
    } catch (error) {
      console.error("Error:", error);
      alert("Error uploading the file or fetching the prediction.");
    }
  };


  return (
    <div className="container d-flex justify-content-center align-items-center vh-100">
      <div
        className="card p-4 shadow-sm"
        style={{
          backgroundColor: "#f8f9fa",
          borderRadius: "15px",
          maxWidth: "400px",
        }}
      >
        <h2 className="text-center mb-4">Upload a Number</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <input
              type="file"
              onChange={handleFileChange}
              className="form-control"
            />
          </div>
          <button type="submit" className="btn w-100 btn-light btn-outline-dark">
            Upload and Predict
          </button>
        </form>
        {prediction && (
          <p className="mt-4 text-center">
            Prediction: <strong>{prediction}</strong>
          </p>
        )}
      </div>
    </div>
  );
};

export default UploadForm;