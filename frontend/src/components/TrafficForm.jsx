const TrafficForm = ({ formData, handleChange, handleSubmit }) => {
  const inputStyle = "bg-slate-900 text-slate-100 border border-slate-600 rounded px-3 h-11 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 w-full";
  const labelStyle = "text-slate-300 text-sm font-semibold mb-1";

  return (
    <form onSubmit={handleSubmit} className="bg-slate-800 p-6 rounded-lg shadow-xl border border-slate-700 w-full max-w-3xl mx-auto">
      <h2 className="text-2xl font-bold text-slate-100 mb-6 border-b border-slate-600 pb-2">
        Network Traffic Parameters
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        
        <div className="flex flex-col">
          <label className={labelStyle}>Duration</label>
          <input type="number" name="duration" value={formData.duration} onChange={handleChange} className={inputStyle} />
        </div>

        <div className="flex flex-col">
          <label className={labelStyle}>Protocol Type</label>
          <select name="protocol_type" value={formData.protocol_type} onChange={handleChange} className={inputStyle}>
            <option value="tcp">TCP</option>
            <option value="udp">UDP</option>
            <option value="icmp">ICMP</option>
          </select>
        </div>

        <div className="flex flex-col">
          <label className={labelStyle}>Service</label>
          <select name="service" value={formData.service} onChange={handleChange} className={inputStyle}>
            <option value="http">HTTP</option>
            <option value="ftp">FTP</option>
            <option value="smtp">SMTP</option>
            <option value="private">Private</option>
          </select>
        </div>

        <div className="flex flex-col">
          <label className={labelStyle}>Flag</label>
          <select name="flag" value={formData.flag} onChange={handleChange} className={inputStyle}>
            <option value="SF">SF (Normal)</option>
            <option value="S0">S0 (Connection Attempt)</option>
            <option value="REJ">REJ (Rejected)</option>
          </select>
        </div>

        <div className="flex flex-col">
          <label className={labelStyle}>Source Bytes</label>
          <input type="number" name="src_bytes" value={formData.src_bytes} onChange={handleChange} className={inputStyle} />
        </div>

        <div className="flex flex-col">
          <label className={labelStyle}>Destination Bytes</label>
          <input type="number" name="dst_bytes" value={formData.dst_bytes} onChange={handleChange} className={inputStyle} />
        </div>

        <div className="flex flex-col">
          <label className={labelStyle}>Count</label>
          <input type="number" name="count" value={formData.count} onChange={handleChange} className={inputStyle} />
        </div>
      </div>

      <button type="submit" className="mt-8 w-full bg-blue-600 hover:bg-blue-500 text-white font-bold py-3 px-4 rounded h-12 transition-colors duration-200">
        Scan Traffic for Anomalies
      </button>
    </form>
  );
};

export default TrafficForm;