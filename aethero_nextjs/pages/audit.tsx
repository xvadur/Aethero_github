import React from "react";
import Head from "next/head";
import fs from "fs";
import path from "path";

interface SummaryStatistics {
  total_aetherony_generated: number;
  average_aetherony_per_hour: number;
  average_cognitive_load: number;
  average_rhythm_score: number;
  most_productive_day: string;
  productivity_by_day: Record<string, number>;
  top_development_patterns: Record<string, number>;
  development_efficiency_rating: string;
}

interface AuditPageProps {
  summary: SummaryStatistics | null;
  error?: string;
}

const AuditPage: React.FC<AuditPageProps> = ({ summary, error }) => (
  <>
    <Head>
      <title>Aethero Audit Report</title>
    </Head>
    <main className="container mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold mb-4">Aethero Audit Report</h1>
      {error && <div className="text-red-500">{error}</div>}
      {summary ? (
        <div className="bg-lab-panel rounded-lg p-6 shadow mb-8">
          <div className="mb-2">Celkový počet Aetheron jednotiek: <b>{summary.total_aetherony_generated}</b></div>
          <div className="mb-2">Priemer na hodinu: <b>{summary.average_aetherony_per_hour}</b></div>
          <div className="mb-2">Priemerná kognitívna záťaž: <b>{summary.average_cognitive_load}</b></div>
          <div className="mb-2">Priemerný rytmus: <b>{summary.average_rhythm_score}</b></div>
          <div className="mb-2">Najproduktívnejší deň: <b>{summary.most_productive_day}</b></div>
          <div className="mb-2">Efektivita: <b>{summary.development_efficiency_rating}</b></div>
          <div className="mt-4">
            <b>Top development patterns:</b>
            <ul className="list-disc ml-6">
              {Object.entries(summary.top_development_patterns).map(([tag, count]) => (
                <li key={tag}>{tag}: {count}</li>
              ))}
            </ul>
          </div>
        </div>
      ) : (
        <div>Žiadne dáta na zobrazenie.</div>
      )}
    </main>
  </>
);

export async function getServerSideProps() {
  try {
    const auditDir = process.cwd();
    const files = fs.readdirSync(auditDir);
    const jsonFiles = files.filter(f => f.startsWith("aethero_audit_") && f.endsWith(".json"));
    if (jsonFiles.length === 0) {
      return { props: { summary: null, error: "Nenašiel sa žiadny auditný JSON report." } };
    }
    // Najnovší podľa mena
    const latest = jsonFiles.sort().reverse()[0];
    const data = JSON.parse(fs.readFileSync(path.join(auditDir, latest), "utf-8"));
    return { props: { summary: data.summary_statistics } };
  } catch (e) {
    return { props: { summary: null, error: (e as Error).message } };
  }
}

export default AuditPage;
