
// ex
import { useEffect, useState } from "react";

function App() {
  const [rankings, setRankings] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/rankings")
      .then(res => res.json())
      .then(data => setRankings(data));
  }, []);

  return (
    <div>
      <h1>F1 True Pace Rankings</h1>
      <table>
        <thead>
          <tr>
            <th>Driver</th>
            <th>Pace Score</th>
          </tr>
        </thead>
        <tbody>
          {rankings.map((driver, i) => (
            <tr key={i}>
              <td>{driver.Driver}</td>
              <td>{driver.pace_score.toFixed(3)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
