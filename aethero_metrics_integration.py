#!/usr/bin/env python3
"""
Aethero Metrics Integration - Propojenie s existujúcim monitoring systémom
Prometheus metrics pre real-time tracking Aetheron jednotiek
"""

import json
import time
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from prometheus_client import CollectorRegistry, Gauge, Counter, Histogram, push_to_gateway
import threading
import schedule
from pathlib import Path

# Import existujúcich Aethero komponentov
sys.path.append('/Users/_xvadur/Desktop/Aethero_github/Aethero_App')
from introspective_parser_module.metrics import CognitiveMetricsAnalyzer

class AetheroMetricsCollector:
    """
    Collector pre Aethero metriky integrácia s Prometheus
    Real-time tracking development productivity
    """
    
    def __init__(self, pushgateway_url: str = "localhost:9091"):
        self.pushgateway_url = pushgateway_url
        self.registry = CollectorRegistry()
        self.cognitive_analyzer = CognitiveMetricsAnalyzer()
        
        # Definícia Prometheus metrík
        self._setup_metrics()
        
        # Monitoring stav
        self.monitoring_active = False
        self.last_audit_data = None
        
    def _setup_metrics(self):
        """Nastavenie Prometheus metrík pre Aethero systém"""
        
        # Gauge metriky (aktuálne hodnoty)
        self.aetheron_total = Gauge(
            'aethero_total_aetherony_generated',
            'Total amount of Aetheron units generated',
            registry=self.registry
        )
        
        self.aetheron_hourly_rate = Gauge(
            'aethero_hourly_productivity_rate',
            'Current hourly Aetheron generation rate',
            registry=self.registry
        )
        
        self.cognitive_load_current = Gauge(
            'aethero_cognitive_load_current',
            'Current cognitive load level (1-10)',
            registry=self.registry
        )
        
        self.cognitive_coherence = Gauge(
            'aethero_cognitive_coherence_score',
            'Cognitive coherence score (0-1)',
            registry=self.registry
        )
        
        self.development_rhythm = Gauge(
            'aethero_development_rhythm_score',
            'Current development rhythm score (0-1)',
            registry=self.registry
        )
        
        self.efficiency_multiplier = Gauge(
            'aethero_efficiency_multiplier',
            'Current efficiency multiplier',
            registry=self.registry
        )
        
        # Counter metriky (rastúce hodnoty)
        self.git_commits_total = Counter(
            'aethero_git_commits_total',
            'Total number of git commits processed',
            registry=self.registry
        )
        
        self.shell_commands_total = Counter(
            'aethero_shell_commands_total',
            'Total number of development shell commands',
            registry=self.registry
        )
        
        self.development_sessions_total = Counter(
            'aethero_development_sessions_total',
            'Total number of development sessions',
            registry=self.registry
        )
        
        # Histogram metriky (distribúcie)
        self.session_duration = Histogram(
            'aethero_session_duration_hours',
            'Duration of development sessions in hours',
            buckets=[0.5, 1.0, 2.0, 4.0, 6.0, 8.0, 12.0, float('inf')],
            registry=self.registry
        )
        
        self.aetheron_per_session = Histogram(
            'aethero_aetherony_per_session',
            'Aetheron units generated per session',
            buckets=[0.1, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0, float('inf')],
            registry=self.registry
        )
        
        # Slovak healthcare specific metrics
        self.healthcare_dev_efficiency = Gauge(
            'aethero_healthcare_dev_efficiency_score',
            'Slovak healthcare developer efficiency score',
            ['dev_context', 'work_type'],
            registry=self.registry
        )
        
        self.asl_cognitive_tags = Counter(
            'aethero_asl_cognitive_tags_total',
            'Total ASL cognitive tags processed',
            ['mental_state', 'emotion_tone'],
            registry=self.registry
        )
    
    def load_latest_audit_data(self) -> Optional[Dict[str, Any]]:
        """Načítanie najnovších audit dát"""
        try:
            audit_files = list(Path('.').glob('aethero_audit_*.json'))
            if not audit_files:
                return None
            
            latest_file = max(audit_files, key=lambda f: f.stat().st_mtime)
            
            with open(latest_file, 'r', encoding='utf-8') as f:
                return json.load(f)
                
        except Exception as e:
            print(f"[ERROR] Failed to load audit data: {e}")
            return None
    
    def update_metrics_from_audit_data(self, audit_data: Dict[str, Any]):
        """Aktualizácia Prometheus metrík z audit dát"""
        
        metadata = audit_data.get('audit_metadata', {})
        summary_stats = audit_data.get('summary_statistics', {})
        sessions = audit_data.get('development_sessions', [])
        units = audit_data.get('aetheron_units', [])
        
        # Aktualizácia základných metrík
        self.aetheron_total.set(metadata.get('total_aetherony_generated', 0))
        self.aetheron_hourly_rate.set(summary_stats.get('average_aetherony_per_hour', 0))
        self.cognitive_load_current.set(summary_stats.get('average_cognitive_load', 5))
        
        # Výpočet cognitive coherence
        if units:
            avg_cognitive_load = sum(u.get('cognitive_load_estimate', 5) for u in units) / len(units)
            coherence_score = max(0, (10 - avg_cognitive_load) / 10)
            self.cognitive_coherence.set(coherence_score)
            
            avg_rhythm = sum(u.get('development_rhythm_score', 0.5) for u in units) / len(units)
            self.development_rhythm.set(avg_rhythm)
            
            avg_efficiency = sum(u.get('efficiency_multiplier', 1.0) for u in units) / len(units)
            self.efficiency_multiplier.set(avg_efficiency)
        
        # Counters (len už existujúcich)
        total_commits = sum(s.get('commits_count', 0) for s in sessions)
        total_commands = sum(s.get('commands_count', 0) for s in sessions)
        
        # Nastavenie counterov na aktuálne hodnoty (hack pre historické dáta)
        self.git_commits_total._value._value = total_commits
        self.shell_commands_total._value._value = total_commands
        self.development_sessions_total._value._value = len(sessions)
        
        # Histogram dáta
        for session in sessions:
            duration = session.get('duration_hours', 0)
            aetherony = session.get('total_aetherony', 0)
            
            if duration > 0:
                self.session_duration.observe(duration)
            if aetherony > 0:
                self.aetheron_per_session.observe(aetherony)
        
        # Slovak healthcare specific metriky
        total_aetherony = metadata.get('total_aetherony_generated', 0)
        total_sessions = len(sessions)
        
        if total_sessions > 0:
            efficiency_score = total_aetherony / total_sessions
            self.healthcare_dev_efficiency.labels(
                dev_context='slovak_healthcare',
                work_type='solo_development'
            ).set(efficiency_score)
        
        print(f"[METRICS] Updated Prometheus metrics at {datetime.now()}")
    
    def simulate_asl_cognitive_metrics(self):
        """Simulácia ASL kognitívnych tagov pre metriky"""
        # Simulácia rôznych mental states a emotion tones
        mental_states = ['focused', 'calm', 'contemplative', 'decisive']
        emotion_tones = ['analytical', 'neutral', 'positive', 'empathetic']
        
        for mental_state in mental_states:
            for emotion_tone in emotion_tones:
                # Simulácia počtu tagov
                tag_count = hash(f"{mental_state}_{emotion_tone}") % 10 + 1
                self.asl_cognitive_tags.labels(
                    mental_state=mental_state,
                    emotion_tone=emotion_tone
                )._value._value = tag_count
    
    def push_metrics_to_prometheus(self):
        """Push metrík do Prometheus Pushgateway"""
        try:
            push_to_gateway(
                self.pushgateway_url,
                job='aethero_audit_system',
                registry=self.registry,
                grouping_key={'instance': 'slovak_healthcare_dev'}
            )
            print(f"[METRICS] Successfully pushed to Prometheus at {self.pushgateway_url}")
            
        except Exception as e:
            print(f"[ERROR] Failed to push metrics to Prometheus: {e}")
    
    def start_continuous_monitoring(self, interval_minutes: int = 15):
        """Spustenie kontinuálneho monitoringu"""
        
        def update_and_push():
            audit_data = self.load_latest_audit_data()
            if audit_data:
                self.update_metrics_from_audit_data(audit_data)
                self.simulate_asl_cognitive_metrics()
                self.push_metrics_to_prometheus()
                self.last_audit_data = audit_data
            else:
                print("[WARNING] No audit data found for metrics update")
        
        # Prvá aktualizácia
        update_and_push()
        
        # Naplánovanie opakovaných aktualizácií
        schedule.every(interval_minutes).minutes.do(update_and_push)
        
        self.monitoring_active = True
        print(f"[MONITORING] Started continuous monitoring (interval: {interval_minutes} min)")
        
        # Main monitoring loop
        while self.monitoring_active:
            schedule.run_pending()
            time.sleep(30)  # Check every 30 seconds
    
    def stop_monitoring(self):
        """Zastavenie monitoringu"""
        self.monitoring_active = False
        print("[MONITORING] Stopped continuous monitoring")
    
    def generate_grafana_dashboard_config(self) -> Dict[str, Any]:
        """Generovanie Grafana dashboard konfigurácie"""
        
        dashboard_config = {
            "dashboard": {
                "id": None,
                "title": "Aethero Development Productivity Dashboard",
                "tags": ["aethero", "development", "slovak", "healthcare"],
                "timezone": "Europe/Bratislava",
                "panels": [
                    {
                        "id": 1,
                        "title": "Total Aetherony Generated",
                        "type": "stat",
                        "targets": [{
                            "expr": "aethero_total_aetherony_generated",
                            "legendFormat": "Total Aetherony"
                        }],
                        "fieldConfig": {
                            "defaults": {
                                "color": {"mode": "palette-classic"},
                                "unit": "short",
                                "thresholds": {
                                    "steps": [
                                        {"color": "red", "value": 0},
                                        {"color": "yellow", "value": 5},
                                        {"color": "green", "value": 10}
                                    ]
                                }
                            }
                        },
                        "gridPos": {"h": 8, "w": 6, "x": 0, "y": 0}
                    },
                    {
                        "id": 2,
                        "title": "Hourly Productivity Rate",
                        "type": "graph",
                        "targets": [{
                            "expr": "aethero_hourly_productivity_rate",
                            "legendFormat": "Aetherony/Hour"
                        }],
                        "gridPos": {"h": 8, "w": 12, "x": 6, "y": 0}
                    },
                    {
                        "id": 3,
                        "title": "Cognitive Load vs Coherence",
                        "type": "graph",
                        "targets": [
                            {
                                "expr": "aethero_cognitive_load_current",
                                "legendFormat": "Cognitive Load"
                            },
                            {
                                "expr": "aethero_cognitive_coherence_score * 10",
                                "legendFormat": "Coherence Score (x10)"
                            }
                        ],
                        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 8}
                    },
                    {
                        "id": 4,
                        "title": "Development Sessions Distribution",
                        "type": "histogram",
                        "targets": [{
                            "expr": "aethero_session_duration_hours_bucket",
                            "legendFormat": "Session Duration (hours)"
                        }],
                        "gridPos": {"h": 8, "w": 6, "x": 12, "y": 8}
                    },
                    {
                        "id": 5,
                        "title": "Slovak Healthcare Dev Efficiency",
                        "type": "stat",
                        "targets": [{
                            "expr": "aethero_healthcare_dev_efficiency_score",
                            "legendFormat": "Efficiency Score"
                        }],
                        "fieldConfig": {
                            "defaults": {
                                "color": {"mode": "palette-classic"},
                                "unit": "short",
                                "thresholds": {
                                    "steps": [
                                        {"color": "red", "value": 0},
                                        {"color": "yellow", "value": 1},
                                        {"color": "green", "value": 2}
                                    ]
                                }
                            }
                        },
                        "gridPos": {"h": 4, "w": 6, "x": 0, "y": 16}
                    },
                    {
                        "id": 6,
                        "title": "ASL Cognitive Tags Heatmap",
                        "type": "heatmap",
                        "targets": [{
                            "expr": "aethero_asl_cognitive_tags_total",
                            "legendFormat": "{{mental_state}} - {{emotion_tone}}"
                        }],
                        "gridPos": {"h": 8, "w": 12, "x": 6, "y": 16}
                    }
                ],
                "time": {
                    "from": "now-24h",
                    "to": "now"
                },
                "refresh": "30s"
            }
        }
        
        return dashboard_config
    
    def export_grafana_dashboard(self, output_file: str = "aethero_grafana_dashboard.json"):
        """Export Grafana dashboard konfigurácie"""
        config = self.generate_grafana_dashboard_config()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        
        print(f"[GRAFANA] Dashboard config exported to: {output_file}")
        return output_file

class AetheroMetricsManager:
    """Manager pre celý Aethero metrics systém"""
    
    def __init__(self):
        self.collector = AetheroMetricsCollector()
        self.monitoring_thread = None
    
    def setup_monitoring_infrastructure(self):
        """Nastavenie kompletnej monitoring infraštruktúry"""
        print("🔧 Setting up Aethero Monitoring Infrastructure...")
        
        # 1. Export Grafana dashboard
        grafana_config = self.collector.export_grafana_dashboard()
        
        # 2. Inštrukcie pre setup
        setup_instructions = """
        📊 AETHERO MONITORING SETUP INSTRUCTIONS
        =======================================
        
        1. Prometheus Pushgateway Setup:
           docker run -d -p 9091:9091 prom/pushgateway
        
        2. Prometheus Config (add to prometheus.yml):
           - job_name: 'aethero-pushgateway'
             static_configs:
               - targets: ['localhost:9091']
        
        3. Grafana Dashboard Import:
           - Import: {grafana_config}
           - Or manually create using provided config
        
        4. Start Monitoring:
           python3 aethero_metrics_integration.py --start-monitoring
        
        🏥 Optimalizované pre Slovak Healthcare Developer workflow!
        """.format(grafana_config=grafana_config)
        
        print(setup_instructions)
        
        # 3. Zápis setup guide
        with open('aethero_monitoring_setup.md', 'w', encoding='utf-8') as f:
            f.write(setup_instructions)
        
        return grafana_config
    
    def start_background_monitoring(self, interval_minutes: int = 15):
        """Spustenie background monitoringu"""
        if self.monitoring_thread and self.monitoring_thread.is_alive():
            print("[WARNING] Monitoring already running")
            return
        
        def monitoring_worker():
            self.collector.start_continuous_monitoring(interval_minutes)
        
        self.monitoring_thread = threading.Thread(target=monitoring_worker, daemon=True)
        self.monitoring_thread.start()
        
        print(f"[MONITORING] Started background monitoring thread")
    
    def stop_monitoring(self):
        """Zastavenie monitoringu"""
        self.collector.stop_monitoring()
        if self.monitoring_thread:
            self.monitoring_thread.join(timeout=5)

def main():
    """Hlavná funkcia pre metrics integration"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Aethero Metrics Integration System')
    parser.add_argument('--setup', action='store_true', help='Setup monitoring infrastructure')
    parser.add_argument('--start-monitoring', action='store_true', help='Start continuous monitoring')
    parser.add_argument('--push-once', action='store_true', help='Push metrics once and exit')
    parser.add_argument('--interval', type=int, default=15, help='Monitoring interval in minutes')
    parser.add_argument('--pushgateway', type=str, default='localhost:9091', help='Pushgateway URL')
    
    args = parser.parse_args()
    
    manager = AetheroMetricsManager()
    manager.collector.pushgateway_url = args.pushgateway
    
    if args.setup:
        manager.setup_monitoring_infrastructure()
    
    elif args.push_once:
        audit_data = manager.collector.load_latest_audit_data()
        if audit_data:
            manager.collector.update_metrics_from_audit_data(audit_data)
            manager.collector.simulate_asl_cognitive_metrics()
            manager.collector.push_metrics_to_prometheus()
        else:
            print("[ERROR] No audit data found. Run aethero_audit.py first.")
    
    elif args.start_monitoring:
        try:
            manager.start_background_monitoring(args.interval)
            print(f"🔄 Monitoring started. Press Ctrl+C to stop.")
            
            # Keep main thread alive
            while True:
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n🛑 Stopping monitoring...")
            manager.stop_monitoring()
    
    else:
        print("Use --help to see available options")

if __name__ == "__main__":
    main()
