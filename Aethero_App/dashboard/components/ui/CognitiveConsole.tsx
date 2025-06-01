import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import useAppState from '../../store/state';

interface CognitiveConsoleProps {
  onCommandSubmit: (command: string) => void;
  logs: string[];
}

const CognitiveConsole: React.FC<CognitiveConsoleProps> = ({ onCommandSubmit, logs }) => {
  const [command, setCommand] = useState('');
  const { addLog } = useAppState();

  useEffect(() => {
    const socket = new WebSocket('ws://localhost:8000/logs/stream');

    socket.onmessage = (event) => {
      addLog(event.data);
    };

    return () => {
      socket.close();
    };
  }, [addLog]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (command.trim()) {
      onCommandSubmit(command);
      setCommand('');
    }
  };

  return (
    <motion.div
      className="bg-gray-900 p-6 rounded-lg shadow-lg flex flex-col space-y-4"
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <h2 className="text-xl font-bold text-white">Cognitive Console</h2>
      <div className="flex-grow overflow-y-auto bg-gray-800 p-4 rounded-lg">
        {logs.length > 0 ? (
          <ul className="space-y-2">
            {logs.map((log, index) => (
              <li key={index} className="text-sm text-gray-300">
                {log}
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-gray-500">No logs available.</p>
        )}
      </div>
      <form onSubmit={handleSubmit} className="flex space-x-2">
        <input
          type="text"
          value={command}
          onChange={(e) => setCommand(e.target.value)}
          placeholder="Enter command..."
          className="flex-grow p-2 rounded-lg bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button
          type="submit"
          className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Submit
        </button>
      </form>
    </motion.div>
  );
};

export default CognitiveConsole;
