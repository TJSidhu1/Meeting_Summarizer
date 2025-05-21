import React from 'react';

const SummaryCard = ({ summary }) => {
  return (
    <div>
      <h2>Meeting Summary</h2>
      <p>{summary}</p>
    </div>
  );
};

export default SummaryCard;
