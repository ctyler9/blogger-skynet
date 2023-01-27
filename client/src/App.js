import React from 'react';
import axios from 'axios';
import './App.css';


const API_ENDPOINT = "http://127.0.0.1:8000";
const API_CLIENT = axios.create({
  baseURL: API_ENDPOINT,
  timeout: 10000
});

class App extends React.Component {
  render() {
    return (
      <div className="App">

      </div>
    );
  }
}

export default App;
