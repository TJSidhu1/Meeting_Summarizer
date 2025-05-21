import React from 'react';

const DecisionLogList = ({ decisions }) => {
  return (
    <div>
      <h2>Decisions</h2>
      <ul>
        {decisions.map((decision, idx) => (
          <li key={idx}>{decision}</li>
        ))}
      </ul>
    </div>
  );
};

export default DecisionLogList;
