import type { NextApiRequest, NextApiResponse } from 'next';
import { analyzeWithAgents } from '../../lib/crew_orchestrator';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }
  const { introspection } = req.body;
  if (!introspection || typeof introspection !== 'string') {
    return res.status(400).json({ error: 'Missing or invalid introspection text' });
  }
  try {
    const result = await analyzeWithAgents(introspection);
    // TODO: Save to ChromaDB here (mocked/skipped for now)
    res.status(200).json({ success: true, data: result });
  } catch (e) {
    res.status(500).json({ error: 'Agent orchestration failed', details: (e as Error).message });
  }
}