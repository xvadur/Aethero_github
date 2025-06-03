export default function handler(req, res) {
  const { team_id } = req.query;
  if (req.method === 'GET') {
    // Logic to retrieve team details
    return res.status(200).json({ team_id, details: 'Team details here' });
  }
  return res.status(405).json({ error: 'Method not allowed' });
}
