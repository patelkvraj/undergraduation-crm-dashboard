import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // This effect runs when the component mounts
    axios.get('http://127.0.0.1:8000/api/students/') // Make a GET request to our Django API
      .then(response => {
        setStudents(response.data); // Store the fetched student data
        setLoading(false); // Set loading to false once data is fetched
      })
      .catch(error => {
        console.error("There was an error fetching the students!", error);
        setLoading(false);
      });
  }, []); // The empty array ensures this effect runs only once

  if (loading) {
    return <div>Loading...</div>; // Show a loading message
  }

  return (
    <div className="App">
      <h1>Student Directory</h1>
      <ul>
        {students.map(student => (
          <li key={student.id}>{student.name} - {student.email}</li> // List the students
        ))}
      </ul>
    </div>
  );
}

export default App;
