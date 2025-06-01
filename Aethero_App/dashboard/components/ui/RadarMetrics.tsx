import React, { useEffect } from 'react';
import { motion } from 'framer-motion';
import { Radar } from 'react-chartjs-2';
import 'chart.js/auto';
import useAppState from '../../store/state';

const fetchMetrics = async () => {
  const response = await fetch('/api/metrics');
  const data = await response.json();
  return data;
};

interface RadarMetricsProps {
  metricsData: {
    labels: string[];
    datasets: {
      label: string;
      data: number[];
      backgroundColor: string;
      borderColor: string;
      borderWidth: number;
    }[];
  };
}

const RadarMetrics: React.FC<RadarMetricsProps> = ({ metricsData }) => {
  const { metrics, setMetrics } = useAppState();

  useEffect(() => {
    fetchMetrics().then((data) => {
      setMetrics(data);
    });
  }, [setMetrics]);

  return (
    <motion.div
      className="bg-gray-800 p-6 rounded-lg shadow-lg"
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.5 }}
    >
      <h2 className="text-xl font-bold text-white mb-4">Radar Metrics</h2>
      <div className="w-full h-96">
        <Radar data={metricsData} options={{
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            r: {
              grid: {
                color: '#4B5563',
              },
              angleLines: {
                color: '#4B5563',
              },
              ticks: {
                backdropColor: 'transparent',
                color: '#D1D5DB',
              },
            },
          },
          plugins: {
            legend: {
              labels: {
                color: '#D1D5DB',
              },
            },
          },
        }} />
      </div>
    </motion.div>
  );
};

export default RadarMetrics;
