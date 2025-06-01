import React from 'react';
import { motion } from 'framer-motion';

interface AgentAvatarProps {
  name: string;
  avatarUrl: string;
  status: 'online' | 'offline' | 'busy';
}

const statusColors = {
  online: 'bg-green-500',
  offline: 'bg-gray-500',
  busy: 'bg-yellow-500',
};

const AgentAvatar: React.FC<AgentAvatarProps> = ({ name, avatarUrl, status }) => {
  return (
    <motion.div
      className="flex items-center space-x-4 p-4 bg-gray-800 rounded-lg shadow-lg"
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <div className="relative">
        <img
          src={avatarUrl}
          alt={`${name}'s avatar`}
          className="w-16 h-16 rounded-full border-2 border-gray-700"
        />
        <span
          className={`absolute bottom-0 right-0 w-4 h-4 rounded-full border-2 border-gray-800 ${statusColors[status]}`}
        ></span>
      </div>
      <div>
        <h3 className="text-lg font-bold text-white">{name}</h3>
        <p className="text-sm text-gray-400 capitalize">{status}</p>
      </div>
    </motion.div>
  );
};

export default AgentAvatar;
