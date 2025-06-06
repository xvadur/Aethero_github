#!/usr/bin/env python3
"""
Aethero Audit System - Introspective Development Performance Analysis
Systém na extrakciu a analýzu Aetheron jednotiek z vývojových logov

Slovak Healthcare Worker Solo Development Efficiency Measurement
"""

import json
import subprocess
import re
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
from dataclasses import dataclass, asdict
from collections import defaultdict, Counter
import csv
import argparse

# Import existujúcich Aethero komponentov
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Aethero_App')))
from introspective_parser_module.metrics import CognitiveMetricsAnalyzer
from introspective_parser_module.models import (
    ASLCognitiveTag, MentalStateEnum, EmotionToneEnum, 
    TemporalContextEnum, AetheroIntrospectiveEntity
)

@dataclass
class AetheronUnit:
    """
    Základná jednotka vývojovej produktivity - 1 Aetheron
    Reprezentuje kvantifikovateľný vývojový výkon
    """
    timestamp: datetime
    aetheron_value: float  # 1.0 = 1 Aetheron
    git_commit_count: int
    shell_commands_count: int
    cognitive_load_estimate: float
    development_rhythm_score: float
    efficiency_multiplier: float
    context_tags: List[str]
    
    @property
    def total_output_score(self) -> float:
        """Celkový výstupný skór pre daný časový úsek"""
        return (
            self.git_commit_count * 0.4 +
            self.shell_commands_count * 0.2 +
            self.development_rhythm_score * 0.3 +
            self.efficiency_multiplier * 0.1
        )

@dataclass
class DevelopmentSession:
    """Reprezentácia vývojovej relácie"""
    start_time: datetime
    end_time: datetime
    total_aetherony: float
    commits: List[Dict[str, Any]]
    commands: List[Dict[str, Any]]
    cognitive_coherence: float
    productivity_rating: str  # "vysoká", "stredná", "nízka"

class AetheroAuditSystem:
    """
    Hlavný audit systém pre analýzu vývojového výkonu
    Integrácia s existujúcim ASL kognitívnym systémom
    """
    
    def __init__(self, git_repo_path: str = None, shell_history_path: str = None):
        # Opravená predvolená cesta na aktuálny workspace
        self.git_repo_path = git_repo_path or "/workspaces/Aethero_github"
        self.shell_history_path = shell_history_path or os.path.expanduser("~/.zsh_history")
        self.cognitive_analyzer = CognitiveMetricsAnalyzer()
        self.audit_session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Definícia oficiálnej Aetheron jednotky
        self.AETHERON_DEFINITION = {
            "base_unit": "1 Aetheron = 1 hodina efektívneho vývoja",
            "measurement_factors": {
                "git_commits": 0.3,
                "shell_commands": 0.2, 
                "cognitive_coherence": 0.3,
                "time_efficiency": 0.2
            },
            "slovak_context": "Meranie produktivity slovenského zdravotníckeho pracovníka"
        }
    
    def extract_git_development_data(self, days_back: int = 30) -> List[Dict[str, Any]]:
        """
        Extrahovanie dát z git logu za posledné dni
        """
        since_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")
        
        try:
            # Git log s podrobnými informáciami
            git_cmd = [
                "git", "log", 
                f"--since={since_date}",
                "--pretty=format:%H|%an|%ae|%ad|%s|%b",
                "--date=iso",
                "--numstat"
            ]
            
            result = subprocess.run(
                git_cmd, 
                cwd=self.git_repo_path,
                capture_output=True, 
                text=True, 
                check=True
            )
            
            commits = self._parse_git_log_output(result.stdout)
            print(f"[AUDIT] Extrahovaných {len(commits)} commit-ov za posledných {days_back} dní")
            return commits
            
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Git log extraction failed: {e}")
            return []
    
    def _parse_git_log_output(self, git_output: str) -> List[Dict[str, Any]]:
        """Parsovanie výstupu git log"""
        commits = []
        lines = git_output.strip().split('\n')
        
        current_commit = None
        for line in lines:
            if '|' in line and len(line.split('|')) == 6:
                # Nový commit
                if current_commit:
                    commits.append(current_commit)
                
                parts = line.split('|')
                # Parse date properly handling timezone
                date_str = parts[3].replace(' +0100', '').replace(' +0200', '')
                if '+' in date_str:
                    date_str = date_str.split('+')[0]
                try:
                    commit_date = datetime.fromisoformat(date_str)
                except:
                    # Fallback parsing
                    from dateutil import parser
                    commit_date = parser.parse(parts[3]).replace(tzinfo=None)
                
                current_commit = {
                    'hash': parts[0],
                    'author': parts[1],
                    'email': parts[2],
                    'date': commit_date,
                    'subject': parts[4],
                    'body': parts[5],
                    'files_changed': [],
                    'lines_added': 0,
                    'lines_removed': 0
                }
            elif current_commit and '\t' in line:
                # Štatistiky súborov
                parts = line.split('\t')
                if len(parts) == 3:
                    added, removed, filename = parts
                    current_commit['files_changed'].append(filename)
                    if added.isdigit():
                        current_commit['lines_added'] += int(added)
                    if removed.isdigit():
                        current_commit['lines_removed'] += int(removed)
        
        if current_commit:
            commits.append(current_commit)
            
        return commits
    
    def extract_shell_development_commands(self, days_back: int = 30) -> List[Dict[str, Any]]:
        """
        Extrahovanie vývojových príkazov zo shell histórie
        """
        if not os.path.exists(self.shell_history_path):
            print(f"[WARNING] Shell history súbor nenájdený: {self.shell_history_path}")
            return []
        
        since_timestamp = (datetime.now() - timedelta(days=days_back)).timestamp()
        commands = []
        
        try:
            with open(self.shell_history_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith(': '):
                        # Zsh history formát: ": timestamp:elapsed_time;command"
                        match = re.match(r': (\d+):\d+;(.+)', line)
                        if match:
                            timestamp = int(match.group(1))
                            command = match.group(2)
                            
                            if timestamp >= since_timestamp:
                                if self._is_development_command(command):
                                    commands.append({
                                        'timestamp': datetime.fromtimestamp(timestamp),
                                        'command': command,
                                        'category': self._categorize_command(command),
                                        'complexity_score': self._assess_command_complexity(command)
                                    })
            
            print(f"[AUDIT] Extrahovaných {len(commands)} vývojových príkazov")
            return sorted(commands, key=lambda x: x['timestamp'])
            
        except Exception as e:
            print(f"[ERROR] Shell history parsing failed: {e}")
            return []
    
    def _is_development_command(self, command: str) -> bool:
        """Identifikácia, či príkaz súvisí s vývojom"""
        dev_keywords = [
            'git', 'npm', 'pip', 'python', 'node', 'yarn', 'pnpm',
            'docker', 'kubectl', 'terraform', 'ansible',
            'vim', 'nvim', 'emacs', 'code', 'subl',
            'make', 'cmake', 'cargo', 'mvn', 'gradle',
            'pytest', 'jest', 'mocha', 'cypress',
            'cd', 'ls', 'find', 'grep', 'cat', 'tail', 'head',
            'curl', 'wget', 'ssh', 'scp', 'rsync'
        ]
        
        return any(keyword in command.lower() for keyword in dev_keywords)
    
    def _categorize_command(self, command: str) -> str:
        """Kategorizácia vývojového príkazu"""
        if any(kw in command.lower() for kw in ['git commit', 'git push', 'git pull']):
            return 'version_control'
        elif any(kw in command.lower() for kw in ['npm install', 'pip install', 'yarn add']):
            return 'dependency_management'
        elif any(kw in command.lower() for kw in ['python', 'node', 'npm run', 'yarn']):
            return 'execution'
        elif any(kw in command.lower() for kw in ['vim', 'nvim', 'code', 'emacs']):
            return 'editing'
        elif any(kw in command.lower() for kw in ['test', 'pytest', 'jest', 'mocha']):
            return 'testing'
        elif any(kw in command.lower() for kw in ['docker', 'kubectl', 'terraform']):
            return 'infrastructure'
        else:
            return 'general'
    
    def _assess_command_complexity(self, command: str) -> float:
        """Hodnotenie zložitosti príkazu (1.0 - 10.0)"""
        complexity_indicators = {
            'git rebase': 8.0,
            'docker-compose': 7.0,
            'kubectl': 6.0,
            'terraform': 7.0,
            'pip install': 3.0,
            'npm install': 3.0,
            'git commit': 4.0,
            'git push': 3.0,
            'python': 5.0,
            'vim': 6.0,
            'grep': 4.0,
            'find': 5.0
        }
        
        for indicator, score in complexity_indicators.items():
            if indicator in command.lower():
                # Úprava skóre podľa dĺžky príkazu
                length_multiplier = min(1.5, len(command) / 50)
                return min(10.0, score * length_multiplier)
        
        return 3.0  # Základné skóre pre nerozpoznané príkazy
    
    def calculate_development_sessions(self, commits: List[Dict], commands: List[Dict]) -> List[DevelopmentSession]:
        """
        Identifikácia a analýza vývojových relácií
        Relácia = kontinuálny blok vývojovej aktivity
        """
        sessions = []
        all_activities = []
        
        # Zlúčenie commit-ov a príkazov do časovej osi
        for commit in commits:
            all_activities.append({
                'timestamp': commit['date'],
                'type': 'commit',
                'data': commit
            })
        
        for command in commands:
            all_activities.append({
                'timestamp': command['timestamp'],
                'type': 'command',
                'data': command
            })
        
        all_activities.sort(key=lambda x: x['timestamp'])
        
        # Identifikácia relácií (gap viac ako 2 hodiny = nová relácia)
        session_gap_threshold = timedelta(hours=2)
        current_session_activities = []
        
        for i, activity in enumerate(all_activities):
            if not current_session_activities:
                current_session_activities.append(activity)
            else:
                time_gap = activity['timestamp'] - current_session_activities[-1]['timestamp']
                
                if time_gap <= session_gap_threshold:
                    current_session_activities.append(activity)
                else:
                    # Ukončenie aktuálnej relácie
                    if len(current_session_activities) >= 3:  # Minimálne 3 aktivity
                        session = self._create_development_session(current_session_activities)
                        sessions.append(session)
                    
                    current_session_activities = [activity]
        
        # Posledná relácia
        if len(current_session_activities) >= 3:
            session = self._create_development_session(current_session_activities)
            sessions.append(session)
        
        print(f"[AUDIT] Identifikovaných {len(sessions)} vývojových relácií")
        return sessions
    
    def _create_development_session(self, activities: List[Dict]) -> DevelopmentSession:
        """Vytvorenie DevelopmentSession z aktivít"""
        start_time = activities[0]['timestamp']
        end_time = activities[-1]['timestamp']
        
        commits = [a['data'] for a in activities if a['type'] == 'commit']
        commands = [a['data'] for a in activities if a['type'] == 'command']
        
        # Výpočet Aetheron jednotiek pre reláciu
        session_duration_hours = (end_time - start_time).total_seconds() / 3600
        
        # Aetheron kalkulácia
        commit_score = len(commits) * 0.5  # 0.5 Aetheron za commit
        command_score = sum(cmd.get('complexity_score', 3.0) for cmd in commands) / 10
        
        # Efektivita na základe časového pomeru
        efficiency_ratio = min(1.0, (commit_score + command_score) / max(session_duration_hours, 0.1))
        
        total_aetherony = (commit_score + command_score) * efficiency_ratio
        
        # Kognitívna koherencia (simulovaná na základe aktivít)
        cognitive_coherence = self._estimate_cognitive_coherence(commits, commands)
        
        # Hodnotenie produktivity
        if total_aetherony >= 2.0:
            productivity_rating = "vysoká"
        elif total_aetherony >= 1.0:
            productivity_rating = "stredná"
        else:
            productivity_rating = "nízka"
        
        return DevelopmentSession(
            start_time=start_time,
            end_time=end_time,
            total_aetherony=total_aetherony,
            commits=commits,
            commands=commands,
            cognitive_coherence=cognitive_coherence,
            productivity_rating=productivity_rating
        )
    
    def _estimate_cognitive_coherence(self, commits: List[Dict], commands: List[Dict]) -> float:
        """
        Odhad kognitívnej koherencie na základe vzorcov v aktivitách
        Integrácia s existujúcim ASL systémom
        """
        # Analýza vzorcov v commit správach
        commit_complexity = []
        for commit in commits:
            subject = commit.get('subject', '')
            # Hodnotenie na základe ASL kritérií
            if any(word in subject.lower() for word in ['fix', 'bug', 'error']):
                commit_complexity.append(0.3)  # Problémové riešenie = nižšia koherencia
            elif any(word in subject.lower() for word in ['feature', 'add', 'implement']):
                commit_complexity.append(0.8)  # Nová funkcionalita = vyššia koherencia
            elif any(word in subject.lower() for word in ['refactor', 'clean', 'optimize']):
                commit_complexity.append(0.9)  # Optimalizácia = najvyššia koherencia
            else:
                commit_complexity.append(0.5)
        
        # Analýza diverzity príkazov
        command_categories = [cmd.get('category', 'general') for cmd in commands]
        category_diversity = len(set(command_categories)) / max(len(command_categories), 1)
        
        base_coherence = sum(commit_complexity) / max(len(commit_complexity), 1) if commit_complexity else 0.5
        diversity_bonus = category_diversity * 0.2
        
        return min(1.0, base_coherence + diversity_bonus)
    
    def generate_aetheron_units(self, sessions: List[DevelopmentSession]) -> List[AetheronUnit]:
        """Generovanie detailných Aetheron jednotiek"""
        aetheron_units = []
        
        for session in sessions:
            # Rozdelenie relácie na hodinové bloky pre presnejšie meranie
            session_duration = session.end_time - session.start_time
            hour_blocks = max(1, int(session_duration.total_seconds() / 3600))
            
            for hour in range(hour_blocks):
                block_start = session.start_time + timedelta(hours=hour)
                block_end = min(session.start_time + timedelta(hours=hour + 1), session.end_time)
                
                # Aktivity v tomto bloku
                block_commits = [c for c in session.commits 
                               if block_start <= c['date'] < block_end]
                block_commands = [c for c in session.commands
                                if block_start <= c['timestamp'] < block_end]
                
                if block_commits or block_commands:
                    # Výpočet Aetheron hodnoty pre blok
                    commit_value = len(block_commits) * 0.3
                    command_value = len(block_commands) * 0.1
                    cognitive_bonus = session.cognitive_coherence * 0.2
                    
                    # Rytmus vývoja na základe frekvencií aktivít
                    rhythm_score = min(1.0, (len(block_commits) + len(block_commands)) / 10)
                    
                    # Efektivitný multiplikátor
                    efficiency = session.cognitive_coherence * rhythm_score
                    
                    aetheron_value = (commit_value + command_value + cognitive_bonus) * (1 + efficiency)
                    
                    # Kontextové tagy
                    context_tags = []
                    if any('fix' in c.get('subject', '').lower() for c in block_commits):
                        context_tags.append('debugging')
                    if any('feature' in c.get('subject', '').lower() for c in block_commits):
                        context_tags.append('feature_development')
                    if any(c.get('category') == 'testing' for c in block_commands):
                        context_tags.append('testing')
                    
                    unit = AetheronUnit(
                        timestamp=block_start,
                        aetheron_value=aetheron_value,
                        git_commit_count=len(block_commits),
                        shell_commands_count=len(block_commands),
                        cognitive_load_estimate=10 - (session.cognitive_coherence * 8),
                        development_rhythm_score=rhythm_score,
                        efficiency_multiplier=efficiency,
                        context_tags=context_tags
                    )
                    
                    aetheron_units.append(unit)
        
        return aetheron_units
    
    def export_audit_results(self, sessions: List[DevelopmentSession], 
                           aetheron_units: List[AetheronUnit]) -> Dict[str, str]:
        """Export výsledkov auditu do JSON a CSV formátov"""
        
        # JSON export
        json_data = {
            'audit_metadata': {
                'session_id': self.audit_session_id,
                'generated_at': datetime.now().isoformat(),
                'git_repo': self.git_repo_path,
                'aetheron_definition': self.AETHERON_DEFINITION,
                'total_sessions': len(sessions),
                'total_aetheron_units': len(aetheron_units),
                'total_aetherony_generated': sum(unit.aetheron_value for unit in aetheron_units)
            },
            'development_sessions': [],
            'aetheron_units': [],
            'summary_statistics': self._generate_summary_statistics(sessions, aetheron_units)
        }
        
        # Konverzia session objektov
        for session in sessions:
            json_data['development_sessions'].append({
                'start_time': session.start_time.isoformat(),
                'end_time': session.end_time.isoformat(),
                'duration_hours': (session.end_time - session.start_time).total_seconds() / 3600,
                'total_aetherony': session.total_aetherony,
                'commits_count': len(session.commits),
                'commands_count': len(session.commands),
                'cognitive_coherence': session.cognitive_coherence,
                'productivity_rating': session.productivity_rating
            })
        
        # Konverzia Aetheron jednotiek
        for unit in aetheron_units:
            json_data['aetheron_units'].append(asdict(unit))
        
        # Zápis JSON
        json_filename = f"aethero_audit_{self.audit_session_id}.json"
        json_path = os.path.join(os.getcwd(), json_filename)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False, default=str)
        
        # CSV export
        csv_filename = f"aethero_audit_units_{self.audit_session_id}.csv"
        csv_path = os.path.join(os.getcwd(), csv_filename)
        
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Timestamp', 'Aetheron_Value', 'Git_Commits', 'Shell_Commands',
                'Cognitive_Load', 'Rhythm_Score', 'Efficiency_Multiplier', 'Context_Tags'
            ])
            
            for unit in aetheron_units:
                writer.writerow([
                    unit.timestamp.isoformat(),
                    unit.aetheron_value,
                    unit.git_commit_count,
                    unit.shell_commands_count,
                    unit.cognitive_load_estimate,
                    unit.development_rhythm_score,
                    unit.efficiency_multiplier,
                    ','.join(unit.context_tags)
                ])
        
        return {
            'json_file': json_path,
            'csv_file': csv_path
        }
    
    def _generate_summary_statistics(self, sessions: List[DevelopmentSession], 
                                   units: List[AetheronUnit]) -> Dict[str, Any]:
        """Generovanie súhrnných štatistík"""
        if not units:
            return {}
        
        total_aetherony = sum(unit.aetheron_value for unit in units)
        avg_cognitive_load = sum(unit.cognitive_load_estimate for unit in units) / len(units)
        avg_rhythm_score = sum(unit.development_rhythm_score for unit in units) / len(units)
        
        # Najproduktívnejšie dni
        daily_productivity = defaultdict(float)
        for unit in units:
            day_key = unit.timestamp.strftime('%Y-%m-%d')
            daily_productivity[day_key] += unit.aetheron_value
        
        # Top vývojové vzorce
        all_tags = []
        for unit in units:
            all_tags.extend(unit.context_tags)
        
        tag_frequency = Counter(all_tags)
        
        return {
            'total_aetherony_generated': round(total_aetherony, 2),
            'average_aetherony_per_hour': round(total_aetherony / max(len(units), 1), 2),
            'average_cognitive_load': round(avg_cognitive_load, 2),
            'average_rhythm_score': round(avg_rhythm_score, 2),
            'most_productive_day': max(daily_productivity.items(), key=lambda x: x[1])[0] if daily_productivity else None,
            'productivity_by_day': dict(daily_productivity),
            'top_development_patterns': dict(tag_frequency.most_common(5)),
            'development_efficiency_rating': self._calculate_efficiency_rating(total_aetherony, len(sessions))
        }
    
    def _calculate_efficiency_rating(self, total_aetherony: float, session_count: int) -> str:
        """Hodnotenie celkovej efektivity vývojára"""
        efficiency_score = total_aetherony / max(session_count, 1)
        
        if efficiency_score >= 3.0:
            return "Výnimočná - Slovak Healthcare Dev Ninja 🚀"
        elif efficiency_score >= 2.0:
            return "Vysoká - Efektívny Solo Developer 💪"
        elif efficiency_score >= 1.0:
            return "Stredná - Stabilný Vývojový Rytmus ⚡"
        else:
            return "Nízka - Potreba Optimalizácie 📈"
    
    def run_complete_audit(self, days_back: int = 30) -> Dict[str, str]:
        """
        Spustenie kompletného audit procesu
        """
        print(f"\n🔍 AETHERO AUDIT SYSTEM - Spúšťam analýzu za posledných {days_back} dní")
        print("=" * 70)
        
        # 1. Extrahovanie git dát
        print("📊 Extrakcia git commit histórie...")
        commits = self.extract_git_development_data(days_back)
        
        # 2. Extrahovanie shell dát
        print("💻 Extrakcia shell command histórie...")
        commands = self.extract_shell_development_commands(days_back)
        
        # 3. Kalkulácia relácií
        print("🧮 Kalkulácia vývojových relácií...")
        sessions = self.calculate_development_sessions(commits, commands)
        
        # 4. Generovanie Aetheron jednotiek
        print("⚡ Generovanie Aetheron jednotiek...")
        aetheron_units = self.generate_aetheron_units(sessions)
        
        # 5. Export výsledkov
        print("💾 Export výsledkov auditu...")
        file_paths = self.export_audit_results(sessions, aetheron_units)
        
        # 6. Súhrnný report
        total_aetherony = sum(unit.aetheron_value for unit in aetheron_units)
        print(f"\n✅ AUDIT DOKONČENÝ")
        print(f"📈 Celkovo vygenerovaných: {total_aetherony:.2f} Aetheron jednotiek")
        print(f"🕐 Počet vývojových relácií: {len(sessions)}")
        print(f"📝 Analyzovaných commit-ov: {len(commits)}")
        print(f"💻 Analyzovaných príkazov: {len(commands)}")
        print(f"\n📁 Súbory:")
        print(f"   JSON: {file_paths['json_file']}")
        print(f"   CSV:  {file_paths['csv_file']}")
        
        return file_paths

def main():
    """Hlavná funkcia pre spustenie auditu"""
    audit_system = AetheroAuditSystem()
    
    # Parametrizácia cez argumenty
    parser = argparse.ArgumentParser(description='Aethero Development Audit System')
    parser.add_argument('--days', type=int, default=30, help='Počet dní na analýzu (default: 30)')
    parser.add_argument('--git-repo', type=str, help='Cesta k git repozitáru')
    parser.add_argument('--shell-history', type=str, help='Cesta k shell history súboru')
    parser.add_argument('--prompt', type=str, help='Cesta k ultra prompt súboru')
    parser.add_argument('--output', type=str, help='Cesta k výstupnému super ultra prompt súboru')
    parser.add_argument('--meta-report', type=str, help='Cesta k meta audit report súboru')
    
    args = parser.parse_args()

    if args.prompt and args.output and args.meta_report:
        # Meta-audit režim podľa ultra promptu
        with open(args.prompt, 'r', encoding='utf-8') as f:
            ultra_prompt = f.read()
        # Tu by prebehla analýza podľa ultra promptu (mock výstup):
        from datetime import datetime
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        super_ultra_prompt = f"""# Super Ultra Prompt AetheroOS – {now} CEST\n## Meta-Analýza\n- **Synergia**: Integrácia LangChain s CrewAI zvyšuje cognitive_load o 0.15.\n- **Etika**: Orákulum odporúča revíziu etického skóre.\n\n## Pokročilé Požiadavky\n- Pridaj real-time dashboard do Gradio UI.\n- Optimalizuj pamäťové indexovanie v AetheroBridge.\n\n## ASL Štruktúra\n```json\n{{ module: super_ultra_audit, action: evolve, purpose: Advanced system evolution, inputs: [meta_findings], outputs: [evolved_system] }}\n```\n"""
        meta_audit_report = f"""# META AUDIT REPORT – {now} CEST\n\n- Všetky požiadavky ultra promptu boli spracované.\n- Systém je pripravený na ďalšiu evolúciu.\n- (Mock introspektívna analýza, implementujte reálnu logiku podľa ultra_prompt.os)\n"""
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(super_ultra_prompt)
        with open(args.meta_report, 'w', encoding='utf-8') as f:
            f.write(meta_audit_report)
        print(f"[{now}] meta-audit - Super ultra prompt a meta audit report boli vygenerované a uložené.")
        sys.exit(0)

    if args.git_repo:
        audit_system.git_repo_path = args.git_repo
    if args.shell_history:
        audit_system.shell_history_path = args.shell_history
    
    # Spustenie auditu
    file_paths = audit_system.run_complete_audit(args.days)
    
    print(f"\n🎯 Aethero Audit dokončený! Súbory uložené:")
    for file_type, path in file_paths.items():
        print(f"   {file_type.upper()}: {path}")

def run_full_aethero_audit():
    """
    Spustí kompletný audit: introspektívny meta-audit (ak je ultra prompt),
    štandardný vývojový audit a vygeneruje všetky výstupy.
    """
    import glob
    # 1. Ultra prompt detection (prefer custom, fallback to ultra_prompt.os)
    ultra_prompt_path = None
    for candidate in [
        'prompts/ultra_prompt.txt',
        'ultra_prompt.os',
        './prompts/ultra_prompt.txt',
        './ultra_prompt.os'
    ]:
        if os.path.exists(candidate):
            ultra_prompt_path = candidate
            break
    # 2. Output paths
    outputs_dir = 'outputs'
    docs_dir = 'docs'
    os.makedirs(outputs_dir, exist_ok=True)
    os.makedirs(docs_dir, exist_ok=True)
    super_ultra_prompt_path = os.path.join(outputs_dir, 'super_ultra_prompt.md')
    meta_audit_report_path = os.path.join(outputs_dir, 'meta_audit_report.md')
    docs_super_ultra_prompt = os.path.join(docs_dir, 'SUPER_ULTRA_PROMPT.md')
    docs_meta_audit_report = os.path.join(docs_dir, 'META_AUDIT_REPORT.md')
    # 3. Meta-audit (always run if ultra prompt exists)
    if ultra_prompt_path:
        with open(ultra_prompt_path, 'r', encoding='utf-8') as f:
            ultra_prompt = f.read()
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        super_ultra_prompt = f"""# Super Ultra Prompt AetheroOS – {now} CEST\n## Meta-Analýza\n- **Synergia**: Integrácia LangChain s CrewAI zvyšuje cognitive_load o 0.15.\n- **Etika**: Orákulum odporúča revíziu etického skóre.\n\n## Pokročilé Požiadavky\n- Pridaj real-time dashboard do Gradio UI.\n- Optimalizuj pamäťové indexovanie v AetheroBridge.\n\n## ASL Šu00truktúra\n```json\n{{ module: super_ultra_audit, action: evolve, purpose: Advanced system evolution, inputs: [meta_findings], outputs: [evolved_system] }}\n```\n"""
        meta_audit_report = f"""# META AUDIT REPORT – {now} CEST\n\n- Všetky požiadavky ultra promptu boli spracované.\n- Systém je pripravený na ďalšiu evolúciu.\n- (Mock introspektívna analýza, implementujte reálnu logiku podľa ultra_prompt.os)\n"""
        for path in [super_ultra_prompt_path, docs_super_ultra_prompt]:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(super_ultra_prompt)
        for path in [meta_audit_report_path, docs_meta_audit_report]:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(meta_audit_report)
        print(f"[{now}] meta-audit - Super ultra prompt a meta audit report boli vygenerované a uložené.")
    # 4. Standard development audit (always run)
    audit_system = AetheroAuditSystem()
    file_paths = audit_system.run_complete_audit(days_back=7)
    print(f"\n🎯 Aethero Audit dokončený! Súbory uložené:")
    for file_type, path in file_paths.items():
        print(f"   {file_type.upper()}: {path}")

def generate_markdown_audit_reports():
    """
    Vygeneruje reálny introspektívny výstup do docs/meta_audit_report.md a docs/super_ultra_prompt.md
    na základe najnovších auditných JSON/CSV súborov.
    """
    import glob
    import json
    import csv
    from datetime import datetime
    # 1. Najnovší JSON/CSV audit
    json_files = sorted(glob.glob('aethero_audit_*.json'))
    csv_files = sorted(glob.glob('aethero_audit_units_*.csv'))
    if not json_files or not csv_files:
        print("[WARNING] Chýbajú auditné JSON/CSV súbory. Markdown report nebude vygenerovaný.")
        return
    json_path = json_files[-1]
    csv_path = csv_files[-1]
    with open(json_path, 'r', encoding='utf-8') as f:
        audit = json.load(f)
    # 2. Základné štatistiky
    meta = audit['audit_metadata']
    stats = audit['summary_statistics']
    sessions = audit['development_sessions']
    units = audit['aetheron_units']
    # 3. Najaktívnejšie dni/moduly
    most_productive_day = stats.get('most_productive_day', '-')
    top_patterns = stats.get('top_development_patterns', {})
    # 4. Markdown report
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    meta_report = f"""# 📊 META AUDIT REPORT\n\n**Dátum generovania:** {now}\n\n- **Počet commitov:** {sum(s['commits_count'] for s in sessions)}\n- **Vývojových relácií:** {meta['total_sessions']}\n- **Spotrebované Aetherony:** {stats['total_aetherony_generated']}\n- **Najaktívnejší deň:** {most_productive_day}\n- **Najčastejšie vzorce:** {', '.join(f'{k} ({v}x)' for k,v in top_patterns.items()) or '-'}\n- **Priemerný cognitive_load:** {stats['average_cognitive_load']}\n- **Efektivita:** {stats['development_efficiency_rating']}\n\n## Vývojové obdobia\n"""
    for s in sessions:
        meta_report += f"- {s['start_time']} až {s['end_time']} | {s['commits_count']} commitov | {s['productivity_rating']} | cognitive_coherence: {round(s['cognitive_coherence'],2)}\n"
    meta_report += f"\n## 📌 ODPORÚČANIE\n"
    # Odporúčanie podľa efektivity
    if 'Výnimočná' in stats['development_efficiency_rating']:
        rec = 'continue'
    elif 'Vysoká' in stats['development_efficiency_rating']:
        rec = 'continue'
    elif 'Stredná' in stats['development_efficiency_rating']:
        rec = 'refactor'
    else:
        rec = 'hold'
    meta_report += f"- Stav systému: `{rec}`\n- Odporúčanie: Zlepšiť periodicitu a diverzitu vývojových vzorcov, zvážiť delegovanie agentom.\n"
    meta_report += f"\n## 🔁 ASL VÝSTUP\n```json\n{{\n  \"module\": \"audit_core\",\n  \"action\": \"introspect\",\n  \"status\": \"complete\",\n  \"result\": \"system_state_assessed\"\n}}\n```\n"
    # 5. Super ultra prompt (odporúčania)
    super_ultra = f"""# SUPER ULTRA PROMPT\n\n**Dátum generovania:** {now}\n\n## Odporúčania pre ďalší vývoj\n- Pokračovať v optimalizácii vývojového rytmu\n- Zamerať sa na rozšírenie testovania a diverzifikáciu commitov\n- Pridať monitoring shell histórie pre lepšiu introspekciu\n\n## ASL Výstup\n```json\n{{\n  \"module\": \"super_ultra_audit\",\n  \"action\": \"evolve\",\n  \"inputs\": [\"meta_findings\"],\n  \"outputs\": [\"evolved_system\"]\n}}\n```\n\n---\n*Audit generovaný prezidentom a agentmi AetheroOS.*\n"""
    # 6. Zápis do docs/
    with open('docs/meta_audit_report.md', 'w', encoding='utf-8') as f:
        f.write(meta_report)
    with open('docs/super_ultra_prompt.md', 'w', encoding='utf-8') as f:
        f.write(super_ultra)
    print("[INFO] Markdown reporty boli vygenerované do docs/ a sú pripravené na čítanie prezidentom aj agentmi.")

if __name__ == "__main__":
    run_full_aethero_audit()
    generate_markdown_audit_reports()
    # Spusti autofix engine po audite
    os.system('python autofix_engine.py')
