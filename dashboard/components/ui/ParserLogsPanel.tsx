import React from 'react';
import { motion } from 'framer-motion';

interface ASLLog {
  id: string;
  timestamp: string;
  type: string;
  payload: Record<string, any>;
}

interface ParserLogsPanelProps {
  logs: ASLLog[];
  onFilter: (type: string) => void;
  onExport: (format: 'json' | 'csv') => void;
}

const ParserLogsPanel: React.FC<ParserLogsPanelProps> = ({ logs, onFilter, onExport }) => {
  return (
    <motion.section
      className="bg-gray-900 text-white p-4 rounded-lg shadow-md"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      <header className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-bold">Parser Logs</h2>
        <div className="flex space-x-2">
          <button
            onClick={() => onFilter('query')}
            className="px-4 py-2 bg-gray-700 rounded hover:bg-gray-600"
          >
            Filter: Query
          </button>
          <button
            onClick={() => onFilter('reflection')}
            className="px-4 py-2 bg-gray-700 rounded hover:bg-gray-600"
          >
            Filter: Reflection
          </button>
          <button
            onClick={() => onExport('json')}
            className="px-4 py-2 bg-gray-700 rounded hover:bg-gray-600"
          >
            Export JSON
          </button>
          <button
            onClick={() => onExport('csv')}
            className="px-4 py-2 bg-gray-700 rounded hover:bg-gray-600"
          >
            Export CSV
          </button>
        </div>
      </header>
      <ul className="space-y-2 max-h-96 overflow-y-auto">
        {logs.map((log) => (
          <li
            key={log.id}
            className="p-3 bg-gray-800 rounded hover:bg-gray-700 transition"
          >
            <p className="text-sm text-gray-400">{log.timestamp}</p>
            <p className="font-bold">{log.type}</p>
            <pre className="text-sm bg-gray-700 p-2 rounded mt-2">
              {JSON.stringify(log.payload, null, 2)}
            </pre>
          </li>
        ))}
      </ul>
    </motion.section>
  );
};

export default ParserLogsPanel;
