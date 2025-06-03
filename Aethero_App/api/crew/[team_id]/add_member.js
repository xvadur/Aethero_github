export default function handler(req, res) {
  const { team_id } = req.query;
  if (req.method === 'POST') {
    const { member } = req.body;
    if (!member) {
      return res.status(400).json({ error: 'Member details are required' });
    }
    // Logic to add a member to the team
    return res.status(200).json({ message: `Member added to team ${team_id}` });
  }
  return res.status(405).json({ error: 'Method not allowed' });
}
