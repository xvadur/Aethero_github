import React from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const data = {
  labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
  datasets: [
    {
      label: "Demo Data",
      data: [12, 19, 3, 5, 2, 9],
      fill: false,
      borderColor: "#a259f7",
      backgroundColor: "#a259f7",
      tension: 0.4,
    },
  ],
};

const options = {
  responsive: true,
  plugins: {
    legend: {
      display: true,
      labels: { color: "#fff" },
    },
    title: {
      display: true,
      text: "Sample Trend (Demo)",
      color: "#fff",
    },
  },
  scales: {
    x: {
      ticks: { color: "#fff" },
      grid: { color: "#333" },
    },
    y: {
      ticks: { color: "#fff" },
      grid: { color: "#333" },
    },
  },
};

const DemoChart: React.FC = () => (
  <div style={{ height: 220 }}>
    <Line data={data} options={options} />
  </div>
);

export default DemoChart;
