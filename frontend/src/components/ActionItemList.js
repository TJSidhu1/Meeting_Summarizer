import React from "react";

const ActionItemList = ({ actions }) => {
  console.log("📝 Action Items received:", actions);
  console.log("Array?", Array.isArray(actions));
  console.log("typeof actions:", typeof actions);


  if (!actions) return <p>Loading action items...</p>;

  const actionArray = Array.isArray(actions) ? actions : [];

  return (
    <div>
      <h2>Action Items</h2>
      {actionArray.length === 0 ? (
        <p>No action items found.</p>
      ) : (
        <ul>
          {actionArray.map((action, index) => (
            <li key={index}>{action}</li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default ActionItemList;
