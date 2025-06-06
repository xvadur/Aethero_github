import React from "react";

const tableData = [
  { genre: "Action", sales: 1200, growth: "+8%", rating: "A" },
  { genre: "Comedy", sales: 950, growth: "+3%", rating: "B" },
  { genre: "Drama", sales: 800, growth: "-2%", rating: "B-" },
  { genre: "Fantasy", sales: 1100, growth: "+5%", rating: "A-" },
  { genre: "Horror", sales: 600, growth: "0%", rating: "C+" },
];

const DemoTable: React.FC = () => (
  <table className="w-full data-table">
    <thead>
      <tr>
        <th className="text-left p-2">Genre</th>
        <th className="text-left p-2">Sales</th>
        <th className="text-left p-2">Growth</th>
        <th className="text-left p-2">Rating</th>
      </tr>
    </thead>
    <tbody>
      {tableData.map((row, idx) => (
        <tr key={idx} className="border-t border-lab-border">
          <td className="p-2">{row.genre}</td>
          <td className="p-2">{row.sales}</td>
          <td className="p-2">{row.growth}</td>
          <td className="p-2">{row.rating}</td>
        </tr>
      ))}
    </tbody>
  </table>
);

export default DemoTable;
