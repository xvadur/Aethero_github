export default function handler(req, res) {
  if (req.method === 'GET') {
    // Logic to list all teams
    return res.status(200).json({ teams: ['Team A', 'Team B', 'Team C'] });
  }
  return res.status(405).json({ error: 'Method not allowed' });
}
