import { useEffect, useState } from 'react';
import useAppState from '../../store/state';

const fetchLogs = async () => {
  const response = await fetch('/api/logs');
  const data = await response.json();
  return data;
};

const ParserLogsPanel = () => {
  const { logs, addLog } = useAppState();
  const [filteredLogs, setFilteredLogs] = useState<string[]>([]);

  useEffect(() => {
    fetchLogs().then((data) => {
      data.forEach((log: string) => addLog(log));
    });
  }, [addLog]);

  return (
    <div>
      <h2>Parser Logs</h2>
      <div>
        {logs.length === 0 ? (
          <p>No logs available.</p>
        ) : (
          logs.map((log, index) => <div key={index}>{log}</div>)
        )}
      </div>
    </div>
  );
};

export default ParserLogsPanel;