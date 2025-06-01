import React from 'react';
import { motion } from 'framer-motion';

interface IntrospectiveHeaderProps {
  modes: string[];
  activeMode: string;
  user: { name: string; avatarUrl: string };
  onModeChange: (mode: string) => void;
  onLogout: () => void;
}

const IntrospectiveHeader: React.FC<IntrospectiveHeaderProps> = ({
  modes,
  activeMode,
  user,
  onModeChange,
  onLogout,
}) => {
  return (
    <motion.header
      className="bg-red-700 text-white flex justify-between items-center p-4"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      <div className="flex items-center space-x-4">
        <img
          src="/logo.svg"
          alt="AetheroOS Logo"
          className="h-10 w-10"
        />
        <h1 className="text-xl font-bold">AetheroOS</h1>
      </div>
      <nav className="flex space-x-4">
        {modes.map((mode) => (
          <button
            key={mode}
            className={`px-4 py-2 rounded ${
              mode === activeMode ? 'bg-white text-red-700' : 'bg-red-600'
            }`}
            onClick={() => onModeChange(mode)}
          >
            {mode.charAt(0).toUpperCase() + mode.slice(1)}
          </button>
        ))}
      </nav>
      <div className="flex items-center space-x-4">
        <img
          src={user.avatarUrl}
          alt={user.name}
          className="h-10 w-10 rounded-full border-2 border-white"
        />
        <span>{user.name}</span>
        <button
          onClick={onLogout}
          className="px-4 py-2 bg-red-600 rounded hover:bg-red-500"
        >
          Logout
        </button>
      </div>
    </motion.header>
  );
};

export default IntrospectiveHeader;
