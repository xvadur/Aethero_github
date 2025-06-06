"""
interpret_audit.py
------------------
Skript na interpretáciu auditného JSON do prehľadného Markdown reportu s analýzou a odporúčaniami (slovensky).
Použitie:
    python scripts/interpret_audit.py --input_path <input.json> --output_path <output.md> --mode full --include-analysis true --agent <meno> --language sk --context "..."
"""
import argparse
import json
import os
from datetime import datetime

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', required=True)
    parser.add_argument('--output_path', required=True)
    parser.add_argument('--mode', default='full')
    parser.add_argument('--include-analysis', default='true')
    parser.add_argument('--agent', default='Frontinus')
    parser.add_argument('--language', default='sk')
    parser.add_argument('--context', default='')
    return parser.parse_args()

def interpret_audit(audit):
    meta = audit.get('audit_metadata', {})
    summary = audit.get('summary_statistics', {})
    sessions = audit.get('development_sessions', [])
    aetherons = audit.get('aetheron_units', [])
    lines = []
    lines.append(f"# Interpretovaný auditný report AetheroOS\n")
    lines.append(f"**Dátum generovania:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    lines.append(f"**Agent:** Frontinus\n")
    lines.append(f"**Kontext:** {meta.get('aetheron_definition', {}).get('slovak_context', '')}\n")
    lines.append(f"\n---\n")
    lines.append(f"## Súhrnné štatistiky\n")
    lines.append(f"- Celkový počet vývojových relácií: {meta.get('total_sessions', '?')}")
    lines.append(f"- Celkový počet commitov: {sum([s.get('commits_count',0) for s in sessions])}")
    lines.append(f"- Celkový počet Aetheron jednotiek: {summary.get('total_aetherony_generated','?')}")
    lines.append(f"- Priemerná produktivita na hodinu: {summary.get('average_aetherony_per_hour','?')}")
    lines.append(f"- Najproduktívnejší deň: {summary.get('most_productive_day','?')}")
    lines.append(f"- Hodnotenie efektivity: {summary.get('development_efficiency_rating','?')}\n")
    lines.append(f"---\n")
    lines.append(f"## Vývojové relácie\n")
    for i, s in enumerate(sessions,1):
        lines.append(f"### Relácia {i}")
        lines.append(f"- Trvanie: {s.get('duration_hours','?'):.2f} hod\n- Commity: {s.get('commits_count','?')}\n- Produktivita: {s.get('productivity_rating','?')}\n- Kognitívna koherencia: {s.get('cognitive_coherence','?'):.2f}")
    lines.append(f"\n---\n")
    lines.append(f"## Aetheron jednotky (výber)\n")
    for a in aetherons:
        lines.append(f"- {a.get('timestamp','?')}: {a.get('aetheron_value','?'):.2f} Aetheron, commity: {a.get('git_commit_count','?')}, tagy: {', '.join(a.get('context_tags',[]))}")
    lines.append(f"\n---\n")
    lines.append(f"## Analýza a odporúčania\n")
    lines.append(f"- Priemerná kognitívna záťaž: {summary.get('average_cognitive_load','?')}\n- Priemerný vývojový rytmus: {summary.get('average_rhythm_score','?')}\n- Najčastejší vzor: {', '.join([f'{k} ({v}x)' for k,v in summary.get('top_development_patterns',{}).items()])}")
    if summary.get('total_aetherony_generated',0) > 5:
        lines.append("- Vývoj je efektívny, odporúčame pokračovať v nastavenom tempe.")
    else:
        lines.append("- Produktivita je nižšia, odporúčame analyzovať prekážky a optimalizovať procesy.")
    if summary.get('average_cognitive_load',0) > 7:
        lines.append("- Pozor na vysokú kognitívnu záťaž, zvážte rozdelenie úloh alebo oddych.")
    if summary.get('average_rhythm_score',0) < 0.4:
        lines.append("- Vývojový rytmus je nízky, odporúčame lepšie plánovanie a pravidelné commitovanie.")
    lines.append(f"\n---\n")
    lines.append(f"**Audit interpretoval agent Frontinus.**\n")
    return '\n'.join(lines)

def main():
    args = parse_args()
    with open(args.input_path, 'r', encoding='utf-8') as f:
        audit = json.load(f)
    report = interpret_audit(audit)
    os.makedirs(os.path.dirname(args.output_path), exist_ok=True)
    with open(args.output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"[OK] Interpretovaný audit uložený do {args.output_path}")

if __name__ == "__main__":
    main()
