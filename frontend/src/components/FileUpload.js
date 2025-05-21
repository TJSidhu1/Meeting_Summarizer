import React, { useState } from 'react';

const FileUpload = ({ onUpload }) => {
  const [file, setFile] = useState(null);

const handleChange = (e) => {
  console.log("File selected:", e.target.files[0]);
  setFile(e.target.files[0]);
};

const handleSubmit = (e) => {
  e.preventDefault();
  console.log("Submit button clicked");
  if (file) {
    console.log("Uploading file to parent:", file);
    onUpload(file);
  } else {
    console.log("No file selected");
  }
};

  return (
    <div>
      <h2>Upload Meeting Audio</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="audio/*" onChange={handleChange} />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
};

export default FileUpload;
