import React, { useState } from "react";

const UploadForm = () => {
  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://localhost:5000/predict", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();
    setPrediction(result.prediction);
  };

  return (
    <div className="max-w-md mx-auto p-4">
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="file"
          onChange={handleFileChange}
          className="block w-full text-sm text-gray-500"
        />
        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Upload and Predict
        </button>
      </form>
      {prediction && <p className="mt-4 text-xl">Prediction: {prediction}</p>}
    </div>
  );
};

export default UploadForm;