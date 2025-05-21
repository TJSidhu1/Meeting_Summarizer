import React, { useState } from 'react';
import axios from 'axios';
import FileUpload from './components/FileUpload';
import SummaryCard from './components/SummaryCard';
import ActionItemList from './components/ActionItemList';
import DecisionLogList from './components/DecisionLogList';

function App() {
  const [data, setData] = useState(null);

const handleUpload = async (file) => {
  console.log("Received file in App.js:", file);
  const formData = new FormData();
  formData.append('file', file);

  try {
    const res = await axios.post('http://localhost:8000/process-audio/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
    console.log("Server response:", res.data);
    setData(res.data);
  } catch (error) {
    console.error('Upload failed:', error);
  }
};


  return (
    <div className="App">
      <h1>AI Meeting Assistant</h1>
      <FileUpload onUpload={handleUpload} />
      {data && (
        <>
          <SummaryCard summary={data.summary} />
          <ActionItemList actions={data.actions} />
          <DecisionLogList decisions={data.decisions} />
        </>
      )}
    </div>
  );
}

export default App;
