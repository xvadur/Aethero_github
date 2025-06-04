import React from "react";

// DEV_0178 :: Introspective log section for dashboard
// This component displays logs in a styled section for the Aethero dashboard.

interface ParserLogsSectionProps {
  logs: string[];
}

const ParserLogsSection: React.FC<ParserLogsSectionProps> = ({ logs }) => {
  return (
    <section style={{
      background: "#181c24",
      color: "#e0e6ef",
      borderRadius: "12px",
      padding: "1.5rem",
      margin: "1.5rem 0",
      boxShadow: "0 2px 12px rgba(0,0,0,0.12)",
      fontFamily: "monospace"
    }}>
      <h2 style={{marginBottom: "1rem"}}>Introspective Logs (DEV_0178)</h2>
      <div style={{maxHeight: "320px", overflowY: "auto"}}>
        {logs.length === 0 ? (
          <div style={{opacity: 0.6}}>No logs available.</div>
        ) : (
          <ul style={{listStyle: "none", padding: 0, margin: 0}}>
            {logs.map((log, idx) => (
              <li key={idx} style={{marginBottom: "0.5rem", borderBottom: "1px solid #23283a", paddingBottom: "0.5rem"}}>
                {log}
              </li>
            ))}
          </ul>
        )}
      </div>
    </section>
  );
};

export default ParserLogsSection;
