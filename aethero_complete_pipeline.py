#!/usr/bin/env python3
"""
Aethero Complete Pipeline - Full automation script
Kompletný audit a analýza system pre Slovak Healthcare Developer
"""

import subprocess
import sys
import os
import time
from datetime import datetime
from pathlib import Path

class AetheroCompletePipeline:
    """
    Kompletný pipeline pre Aethero audit systém
    Automatizuje celý proces od auditu po monitoring
    """
    
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.scripts = {
            'audit': 'aethero_audit.py',
            'dashboard': 'aethero_dashboard.py', 
            'metrics': 'aethero_metrics_integration.py'
        }
        self.execution_log = []
        
    def log_execution(self, step: str, status: str, message: str = ""):
        """Logovanie krokov pipeline"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {step}: {status}"
        if message:
            log_entry += f" - {message}"
        
        print(log_entry)
        self.execution_log.append(log_entry)
    
    def check_dependencies(self) -> bool:
        """Kontrola dostupnosti potrebných skriptov"""
        self.log_execution("DEPENDENCY_CHECK", "STARTED", "Checking script availability")
        
        missing_scripts = []
        for name, script in self.scripts.items():
            script_path = self.base_dir / script
            if not script_path.exists():
                missing_scripts.append(script)
        
        if missing_scripts:
            self.log_execution("DEPENDENCY_CHECK", "FAILED", f"Missing: {', '.join(missing_scripts)}")
            return False
        
        self.log_execution("DEPENDENCY_CHECK", "SUCCESS", "All scripts available")
        return True
    
    def run_audit_analysis(self, days: int = 7) -> bool:
        """Spustenie audit analýzy"""
        self.log_execution("AUDIT_ANALYSIS", "STARTED", f"Analyzing last {days} days")
        
        try:
            audit_script = self.base_dir / self.scripts['audit']
            result = subprocess.run([
                sys.executable, str(audit_script), '--days', str(days)
            ], capture_output=True, text=True, cwd=self.base_dir)
            
            if result.returncode == 0:
                self.log_execution("AUDIT_ANALYSIS", "SUCCESS", "Audit completed")
                return True
            else:
                self.log_execution("AUDIT_ANALYSIS", "FAILED", f"Error: {result.stderr}")
                return False
                
        except Exception as e:
            self.log_execution("AUDIT_ANALYSIS", "ERROR", str(e))
            return False
    
    def generate_dashboard(self) -> bool:
        """Generovanie dashboard"""
        self.log_execution("DASHBOARD_GENERATION", "STARTED", "Creating visual dashboard")
        
        try:
            dashboard_script = self.base_dir / self.scripts['dashboard']
            result = subprocess.run([
                sys.executable, str(dashboard_script)
            ], capture_output=True, text=True, cwd=self.base_dir)
            
            if result.returncode == 0:
                self.log_execution("DASHBOARD_GENERATION", "SUCCESS", "Dashboard created")
                return True
            else:
                self.log_execution("DASHBOARD_GENERATION", "FAILED", f"Error: {result.stderr}")
                return False
                
        except Exception as e:
            self.log_execution("DASHBOARD_GENERATION", "ERROR", str(e))
            return False
    
    def setup_monitoring(self) -> bool:
        """Nastavenie monitoring infraštruktúry"""
        self.log_execution("MONITORING_SETUP", "STARTED", "Setting up Prometheus/Grafana integration")
        
        try:
            metrics_script = self.base_dir / self.scripts['metrics']
            result = subprocess.run([
                sys.executable, str(metrics_script), '--setup'
            ], capture_output=True, text=True, cwd=self.base_dir)
            
            if result.returncode == 0:
                self.log_execution("MONITORING_SETUP", "SUCCESS", "Monitoring infrastructure ready")
                return True
            else:
                self.log_execution("MONITORING_SETUP", "FAILED", f"Error: {result.stderr}")
                return False
                
        except Exception as e:
            self.log_execution("MONITORING_SETUP", "ERROR", str(e))
            return False
    
    def push_initial_metrics(self) -> bool:
        """Push počiatočných metrík do Prometheus"""
        self.log_execution("METRICS_PUSH", "STARTED", "Pushing metrics to Prometheus")
        
        try:
            metrics_script = self.base_dir / self.scripts['metrics']
            result = subprocess.run([
                sys.executable, str(metrics_script), '--push-once'
            ], capture_output=True, text=True, cwd=self.base_dir)
            
            if result.returncode == 0:
                self.log_execution("METRICS_PUSH", "SUCCESS", "Metrics pushed successfully")
                return True
            else:
                self.log_execution("METRICS_PUSH", "WARNING", "Pushgateway might not be running")
                return True  # Non-critical failure
                
        except Exception as e:
            self.log_execution("METRICS_PUSH", "WARNING", str(e))
            return True  # Non-critical failure
    
    def generate_summary_report(self) -> str:
        """Generovanie súhrnného reportu"""
        self.log_execution("SUMMARY_REPORT", "STARTED", "Creating executive summary")
        
        # Hľadanie vygenerovaných súborov
        generated_files = {
            'audit_json': list(self.base_dir.glob('aethero_audit_*.json')),
            'audit_csv': list(self.base_dir.glob('aethero_audit_units_*.csv')),
            'dashboard_html': list(self.base_dir.glob('aethero_dashboard_*.html')),
            'grafana_config': list(self.base_dir.glob('aethero_grafana_dashboard.json')),
            'monitoring_setup': list(self.base_dir.glob('aethero_monitoring_setup.md'))
        }
        
        # Zisťovanie štatistík z audit JSON
        audit_stats = {}
        if generated_files['audit_json']:
            try:
                import json
                with open(generated_files['audit_json'][-1], 'r', encoding='utf-8') as f:
                    audit_data = json.load(f)
                    audit_stats = audit_data.get('summary_statistics', {})
            except:
                pass
        
        # Generovanie reportu
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report = f"""
        ═══════════════════════════════════════════════════════════════
        🚀 AETHERO COMPLETE AUDIT PIPELINE REPORT
        ═══════════════════════════════════════════════════════════════
        
        📅 Generated: {timestamp}
        🏥 Context: Slovak Healthcare Developer Solo Performance Analysis
        ⚡ System: Aethero Introspective Development Productivity Measurement
        
        ───────────────────────────────────────────────────────────────
        📊 EXECUTION SUMMARY
        ───────────────────────────────────────────────────────────────
        """
        
        for log_entry in self.execution_log:
            report += f"\n        {log_entry}"
        
        report += f"""
        
        ───────────────────────────────────────────────────────────────
        📈 PERFORMANCE METRICS
        ───────────────────────────────────────────────────────────────
        """
        
        if audit_stats:
            report += f"""
        🎯 Total Aetherony Generated: {audit_stats.get('total_aetherony_generated', 'N/A')}
        ⚡ Average Aetherony/Hour: {audit_stats.get('average_aetherony_per_hour', 'N/A')}
        🧠 Average Cognitive Load: {audit_stats.get('average_cognitive_load', 'N/A')}/10
        🔥 Development Efficiency: {audit_stats.get('development_efficiency_rating', 'N/A')}
        📅 Most Productive Day: {audit_stats.get('most_productive_day', 'N/A')}
        """
        
        report += f"""
        
        ───────────────────────────────────────────────────────────────
        📁 GENERATED FILES
        ───────────────────────────────────────────────────────────────
        """
        
        for file_type, files in generated_files.items():
            if files:
                latest_file = max(files, key=lambda f: f.stat().st_mtime)
                report += f"\n        📄 {file_type.upper()}: {latest_file.name}"
            else:
                report += f"\n        ❌ {file_type.upper()}: Not generated"
        
        report += f"""
        
        ───────────────────────────────────────────────────────────────
        🔧 NEXT STEPS
        ───────────────────────────────────────────────────────────────
        
        1. 📊 Dashboard Access:
           - Open: {generated_files['dashboard_html'][-1].name if generated_files['dashboard_html'] else 'N/A'}
           - Or view CSV data in Excel/LibreOffice
        
        2. 🔄 Continuous Monitoring:
           - Setup Prometheus Pushgateway: docker run -d -p 9091:9091 prom/pushgateway
           - Import Grafana dashboard: aethero_grafana_dashboard.json
           - Start monitoring: python3 aethero_metrics_integration.py --start-monitoring
        
        3. 📈 Performance Optimization:
           - Monitor cognitive load patterns
           - Optimize development sessions based on rhythm analysis
           - Track Aetheron generation efficiency over time
        
        4. 🏥 Slovak Healthcare Context:
           - Integrate with medical work schedule
           - Balance development time with healthcare duties
           - Optimize part-time development productivity
        
        ───────────────────────────────────────────────────────────────
        💡 AETHERO DEFINITION REMINDER
        ───────────────────────────────────────────────────────────────
        
        1 Aetheron = 1 hour of effective development work
        Measured by: Git commits (30%) + Shell commands (20%) + 
                    Cognitive coherence (30%) + Time efficiency (20%)
        
        🎯 Goal: Maximize Aetheron generation while maintaining
               sustainable cognitive load and work-life balance
        
        ═══════════════════════════════════════════════════════════════
        """
        
        # Zápis reportu do súboru
        report_filename = f"aethero_complete_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        report_path = self.base_dir / report_filename
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        self.log_execution("SUMMARY_REPORT", "SUCCESS", f"Report saved to {report_filename}")
        return str(report_path)
    
    def run_complete_pipeline(self, days: int = 7, skip_monitoring: bool = False) -> bool:
        """Spustenie kompletného pipeline"""
        start_time = time.time()
        
        print("🚀 AETHERO COMPLETE PIPELINE - STARTING")
        print("=" * 60)
        print(f"🏥 Slovak Healthcare Developer Productivity Analysis")
        print(f"📅 Analyzing last {days} days of development activity")
        print("=" * 60)
        
        # 1. Kontrola dependencies
        if not self.check_dependencies():
            return False
        
        # 2. Audit analýza
        if not self.run_audit_analysis(days):
            return False
        
        # 3. Dashboard generovanie
        if not self.generate_dashboard():
            return False
        
        # 4. Monitoring setup (voliteľné)
        if not skip_monitoring:
            self.setup_monitoring()
            self.push_initial_metrics()
        
        # 5. Súhrnný report
        report_path = self.generate_summary_report()
        
        # Finálny súhrn
        execution_time = time.time() - start_time
        
        print("\n" + "=" * 60)
        print("✅ AETHERO PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 60)
        print(f"⏱️  Execution time: {execution_time:.1f} seconds")
        print(f"📄 Complete report: {Path(report_path).name}")
        print(f"🎯 Ready for development productivity analysis!")
        
        # Zobrazenie reportu
        try:
            with open(report_path, 'r', encoding='utf-8') as f:
                print(f.read())
        except:
            pass
        
        return True

def main():
    """Hlavná funkcia complete pipeline"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Aethero Complete Development Audit Pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 aethero_complete_pipeline.py                # Full pipeline, last 7 days
  python3 aethero_complete_pipeline.py --days 30      # Last 30 days
  python3 aethero_complete_pipeline.py --skip-monitoring  # Without Prometheus setup
        """
    )
    
    parser.add_argument('--days', type=int, default=7, 
                       help='Number of days to analyze (default: 7)')
    parser.add_argument('--skip-monitoring', action='store_true',
                       help='Skip Prometheus/Grafana monitoring setup')
    
    args = parser.parse_args()
    
    pipeline = AetheroCompletePipeline()
    success = pipeline.run_complete_pipeline(
        days=args.days, 
        skip_monitoring=args.skip_monitoring
    )
    
    if not success:
        print("\n❌ Pipeline execution failed. Check logs above.")
        sys.exit(1)
    
    print("\n🎉 Aethero audit pipeline completed successfully!")
    print("🔗 Check generated files for detailed analysis.")

if __name__ == "__main__":
    main()
