import React, { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState("");

  useEffect(() => {
    fetch("/api/data")
      .then((response) => response.json())
      .then((data) => setData(data.message));
  }, []);

  return (
    <div>
      <h1>{data}</h1>
    </div>
  );
}

export default App;
