import React, { useState } from 'react';
import api from './api';

function App() {
  const [k, setK] = useState('');
  const [result, setResult] = useState('');

  const fetchData = async () => {
    try {
      const response = await api.get(`/n/${k}`);
      setResult(response.data); // Assuming response contains data field with JSON
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleButtonClick = () => {
    fetchData();
  };

  return (
    <div>
      <nav className='navbar navbar-dark bg-primary'>
        <div className='container-fluid'>
          <a className='navbar-brand'>
            Quan's App
          </a>
        </div>
      </nav>
      <div className='container'>
        <div className='mt-3'>
          <input
            type='number'
            value={k}
            onChange={(e) => setK(e.target.value)}
            placeholder='Enter an integer (k)'
          />
          <button onClick={handleButtonClick}>Get Result</button>
        </div>
        {result && (
          <div className='mt-3'>
            <h3>Result:</h3>
            <div className='result-container'>
              <p>k: {result.k}</p>
              <p>list_n: {result.list_n && result.list_n.join(', ')}</p>
              <p>k_exist?: {result.k_exist ? 'True' : 'False'}</p>
              <p>steps to find k: {result.step1}</p>
              <p>list_nk: {result.list_n && result.list_nk.join(', ')}</p>
              <p>steps to find all number that are less than k: {result.step2}</p>
      {/* Add more properties as needed */}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
