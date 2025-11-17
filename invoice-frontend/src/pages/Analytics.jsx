import { useLocation } from "react-router-dom";

function Analytics() {
  const location = useLocation();
  const result = location.state?.result;

  return (
    <div style={{ padding: "20px" }}>
      <h1>Invoice Analysis</h1>

      {!result ? (
        <p>No data received. Please upload an invoice first.</p>
      ) : (
        <div
          style={{
            border: "1px solid #ccc",
            padding: "20px",
            width: "80%",
            borderRadius: "8px",
            backgroundColor: "#f2f2f2",
            lineHeight: "1.8",
            fontSize: "18px"
          }}
        >
          <p><strong>Date:</strong> {Array.isArray(result.Date) ? result.Date.join(", ") : result.Date}</p>

          <p><strong>Total Amount:</strong> 
            {Array.isArray(result["Total Amount"]) 
              ? result["Total Amount"].join(", ") 
              : result["Total Amount"]}
          </p>

          <p><strong>GST:</strong> 
            {Array.isArray(result.GST) ? result.GST.join(", ") : result.GST}
          </p>

          <p><strong>Rates Found:</strong> 
            {Array.isArray(result["Rates Found"]) 
              ? result["Rates Found"].join(", ") 
              : result["Rates Found"]}
          </p>
        </div>
      )}
    </div>
  );
}

export default Analytics;
