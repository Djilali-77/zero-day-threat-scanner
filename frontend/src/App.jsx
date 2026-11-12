import { useState } from 'react';
import axios from 'axios';
import TrafficForm from './components/TrafficForm';
import ScanResult from './components/ScanResult';  
import BatchUpload from './components/BatchUpload';  

function App() {
  const [formData, setFormData] = useState({
    duration: 0, protocol_type: "tcp", service: "http", 
    flag: "SF", src_bytes: 215, dst_bytes: 45076, count: 1
  });

  const [scanResult, setScanResult] = useState(null);

  const handleChange = (e) => {
    const { name, value, type } = e.target;
    const parsedValue = type === 'number' ? Number(value) : value;
    setFormData({ ...formData, [name]: parsedValue });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setScanResult(null);

    try {
      const API_URL = "http://127.0.0.1:8000";
      const response = await axios.post(`${API_URL}/predict`, formData);
      setScanResult(response.data);
    } catch (error) {
      console.error("Error calling API: ", error);
      setScanResult({ status: 'danger', message: 'Connection Error to Backend' });
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 flex flex-col items-center py-12 px-4 font-sans text-slate-200">
      <header className="mb-10 text-center">
        <h1 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-emerald-400">
          Zero-Day Threat Scanner
        </h1>
        <p className="text-slate-400 mt-2">AI-Powered Network Anomaly Detection</p>
      </header>

      <main className="w-full">
        <TrafficForm 
          formData={formData} 
          handleChange={handleChange} 
          handleSubmit={handleSubmit} 
        />

        <BatchUpload setScanResult={setScanResult} />
        
        <ScanResult result={scanResult} />
      </main>
    </div>
  );
}

export default App;