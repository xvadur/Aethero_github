export default function handler(req, res) {
  if (req.method === 'POST') {
    const { name } = req.body;
    if (!name) {
      return res.status(400).json({ error: 'Team name is required' });
    }
    // Logic to create a new team
    return res.status(201).json({ message: `Team '${name}' created successfully` });
  }
  return res.status(405).json({ error: 'Method not allowed' });
}
