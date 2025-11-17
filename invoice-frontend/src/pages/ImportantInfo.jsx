function ImportantInfo() {
  return (
    <div>
      <h1>Important Information</h1>
      <p>This page will show important invoice details such as:</p>

      <ul>
        <li>Total Amount</li>
        <li>Invoice Date</li>
        <li>Total GST</li>
        <li>Rate of all products</li>
      </ul>

      <div style={{ border: "1px solid black", padding: "10px", width: "80%" }}>
        <p>Important details will appear here after analysis.</p>
      </div>
    </div>
  );
}

export default ImportantInfo;