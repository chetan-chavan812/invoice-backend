import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function UploadInvoice() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("image", file);

    try {
      const response = await axios.post("http://127.0.0.1:5000/analyze", formData);
      
      // Redirect to Analytics page with data
      navigate("/analytics", { state: { result: response.data } });

    } catch (error) {
      setMessage("Error uploading file");
    }
  };

  return (
    <div>
      <h1>Upload Invoice</h1>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
      <p>{message}</p>
    </div>
  );
}

export default UploadInvoice;
