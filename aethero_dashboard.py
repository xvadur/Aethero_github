#!/usr/bin/env python3
"""
Aethero Dashboard - Vizualizácia a analýza Aetheron jednotiek
Real-time dashboard pre slovak healthcare developer productivity
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from datetime import datetime, timedelta
import numpy as np
from typing import Dict, List, Any
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import os
import glob

class AetheroDashboard:
    """
    Interaktívny dashboard pre vizualizáciu Aetheron audit výsledkov
    """
    
    def __init__(self):
        self.audit_data = None
        self.df_units = None
        self.df_sessions = None
        
        # Štýlové nastavenia
        plt.style.use('seaborn-v0_8-darkgrid')
        sns.set_palette("husl")
        
    def load_latest_audit_data(self, audit_dir: str = ".") -> bool:
        """Načítanie najnovších audit dát"""
        audit_files = glob.glob(os.path.join(audit_dir, "aethero_audit_*.json"))
        
        if not audit_files:
            print("❌ Žiadne audit súbory nenájdené")
            return False
        
        # Najnovší súbor
        latest_file = max(audit_files, key=os.path.getctime)
        
        try:
            with open(latest_file, 'r', encoding='utf-8') as f:
                self.audit_data = json.load(f)
            
            # Konverzia na pandas DataFrames
            self._prepare_dataframes()
            print(f"✅ Audit dáta načítané z: {latest_file}")
            return True
            
        except Exception as e:
            print(f"❌ Chyba pri načítaní audit dát: {e}")
            return False
    
    def _prepare_dataframes(self):
        """Príprava pandas DataFrames pre analýzu"""
        if not self.audit_data:
            return
        
        # DataFrame pre Aetheron jednotky
        units_data = []
        for unit in self.audit_data.get('aetheron_units', []):
            unit_dict = unit.copy()
            unit_dict['timestamp'] = pd.to_datetime(unit_dict['timestamp'])
            unit_dict['hour'] = unit_dict['timestamp'].hour
            unit_dict['day_of_week'] = unit_dict['timestamp'].day_name()
            unit_dict['date'] = unit_dict['timestamp'].date()
            units_data.append(unit_dict)
        
        self.df_units = pd.DataFrame(units_data)
        
        # DataFrame pre relácie
        sessions_data = []
        for session in self.audit_data.get('development_sessions', []):
            session_dict = session.copy()
            session_dict['start_time'] = pd.to_datetime(session_dict['start_time'])
            session_dict['end_time'] = pd.to_datetime(session_dict['end_time'])
            session_dict['date'] = session_dict['start_time'].date()
            sessions_data.append(session_dict)
        
        self.df_sessions = pd.DataFrame(sessions_data)
    
    def create_productivity_timeline(self) -> go.Figure:
        """Timeline produktivity s Aetheron jednotkami"""
        if self.df_units is None or len(self.df_units) == 0:
            return go.Figure().add_annotation(text="Žiadne dáta na zobrazenie")
        
        fig = go.Figure()
        
        # Hlavná línia Aetheron hodnôt
        fig.add_trace(go.Scatter(
            x=self.df_units['timestamp'],
            y=self.df_units['aetheron_value'],
            mode='lines+markers',
            name='Aetheron Value',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8, color='#1f77b4')
        ))
        
        # Kognitívna záťaž ako secondary y-axis
        fig.add_trace(go.Scatter(
            x=self.df_units['timestamp'],
            y=self.df_units['cognitive_load_estimate'],
            mode='lines',
            name='Cognitive Load',
            yaxis='y2',
            line=dict(color='#ff7f0e', width=2, dash='dash'),
            opacity=0.7
        ))
        
        fig.update_layout(
            title='🚀 Slovak Healthcare Developer - Productivity Timeline',
            xaxis_title='Time',
            yaxis_title='Aetheron Value',
            yaxis2=dict(
                title='Cognitive Load',
                overlaying='y',
                side='right',
                range=[0, 10]
            ),
            hovermode='x unified',
            template='plotly_dark'
        )
        
        return fig
    
    def create_daily_productivity_heatmap(self) -> go.Figure:
        """Heatmapa dennej produktivity"""
        if self.df_units is None or len(self.df_units) == 0:
            return go.Figure()
        
        # Pivot table pre heatmapu
        daily_productivity = self.df_units.groupby(['date', 'hour'])['aetheron_value'].sum().reset_index()
        pivot_data = daily_productivity.pivot(index='date', columns='hour', values='aetheron_value').fillna(0)
        
        fig = go.Figure(data=go.Heatmap(
            z=pivot_data.values,
            x=[f"{h:02d}:00" for h in pivot_data.columns],
            y=[str(d) for d in pivot_data.index],
            colorscale='Viridis',
            colorbar=dict(title="Aetheron Value")
        ))
        
        fig.update_layout(
            title='📅 Daily Development Rhythm Heatmap',
            xaxis_title='Hour of Day',
            yaxis_title='Date',
            template='plotly_dark'
        )
        
        return fig
    
    def create_cognitive_analysis_radar(self) -> go.Figure:
        """Radar chart pre kognitívnu analýzu"""
        if self.df_units is None or len(self.df_units) == 0:
            return go.Figure()
        
        # Agregované metriky
        metrics = {
            'Avg Aetheron Value': self.df_units['aetheron_value'].mean(),
            'Avg Rhythm Score': self.df_units['development_rhythm_score'].mean(),
            'Avg Efficiency': self.df_units['efficiency_multiplier'].mean(),
            'Cognitive Coherence': 10 - self.df_units['cognitive_load_estimate'].mean(),
            'Git Activity': self.df_units['git_commit_count'].mean() * 2,
            'Shell Activity': self.df_units['shell_commands_count'].mean() / 2
        }
        
        # Normalizácia na 0-10 škálu
        max_values = {'Avg Aetheron Value': 5, 'Avg Rhythm Score': 1, 'Avg Efficiency': 1,
                     'Cognitive Coherence': 10, 'Git Activity': 10, 'Shell Activity': 10}
        
        normalized_metrics = {}
        for key, value in metrics.items():
            normalized_metrics[key] = min(10, (value / max_values[key]) * 10)
        
        categories = list(normalized_metrics.keys())
        values = list(normalized_metrics.values())
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=values + [values[0]],  # Zatvorenie kruhu
            theta=categories + [categories[0]],
            fill='toself',
            name='Slovak Developer Profile',
            line_color='#1f77b4'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            title='🧠 Cognitive Performance Radar - Slovak Healthcare Dev',
            template='plotly_dark'
        )
        
        return fig
    
    def create_session_analysis_chart(self) -> go.Figure:
        """Analýza vývojových relácií"""
        if self.df_sessions is None or len(self.df_sessions) == 0:
            return go.Figure()
        
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Session Duration vs Aetherony', 'Productivity Rating Distribution',
                           'Cognitive Coherence vs Output', 'Sessions by Day of Week'),
            specs=[[{"secondary_y": False}, {"type": "pie"}],
                   [{"secondary_y": False}, {"type": "bar"}]]
        )
        
        # 1. Duration vs Aetherony scatter
        fig.add_trace(go.Scatter(
            x=self.df_sessions['duration_hours'],
            y=self.df_sessions['total_aetherony'],
            mode='markers',
            marker=dict(
                size=self.df_sessions['cognitive_coherence'] * 20,
                color=self.df_sessions['cognitive_coherence'],
                colorscale='Viridis',
                showscale=True
            ),
            name='Sessions'
        ), row=1, col=1)
        
        # 2. Productivity rating pie
        rating_counts = self.df_sessions['productivity_rating'].value_counts()
        fig.add_trace(go.Pie(
            labels=rating_counts.index,
            values=rating_counts.values,
            name="Productivity"
        ), row=1, col=2)
        
        # 3. Cognitive coherence vs commits
        fig.add_trace(go.Scatter(
            x=self.df_sessions['cognitive_coherence'],
            y=self.df_sessions['commits_count'],
            mode='markers',
            name='Coherence vs Commits'
        ), row=2, col=1)
        
        # 4. Sessions by day of week
        if 'start_time' in self.df_sessions.columns:
            daily_sessions = self.df_sessions.groupby(
                self.df_sessions['start_time'].dt.day_name()
            ).size().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                             'Friday', 'Saturday', 'Sunday'], fill_value=0)
            
            fig.add_trace(go.Bar(
                x=daily_sessions.index,
                y=daily_sessions.values,
                name='Sessions per Day'
            ), row=2, col=2)
        
        fig.update_layout(
            title='📊 Development Sessions Analysis',
            template='plotly_dark',
            height=800
        )
        
        return fig
    
    def generate_executive_summary(self) -> Dict[str, Any]:
        """Generovanie executive summary pre management"""
        if not self.audit_data:
            return {}
        
        metadata = self.audit_data.get('audit_metadata', {})
        summary_stats = self.audit_data.get('summary_statistics', {})
        
        # Výpočet ROI a human capital efficiency
        total_aetherony = metadata.get('total_aetherony_generated', 0)
        total_sessions = metadata.get('total_sessions', 0)
        
        # Odhad nákladov vs výstup (na základe SK healthcare salary)
        avg_slovak_dev_hourly_rate = 25  # EUR/hour
        estimated_dev_hours = total_sessions * 2  # Priemer 2h na session
        estimated_cost = estimated_dev_hours * avg_slovak_dev_hourly_rate
        
        aetheron_value_eur = total_aetherony * 50  # 1 Aetheron = 50 EUR value
        roi_percentage = ((aetheron_value_eur - estimated_cost) / estimated_cost * 100) if estimated_cost > 0 else 0
        
        return {
            'performance_summary': {
                'total_aetherony_generated': total_aetherony,
                'development_efficiency_rating': summary_stats.get('development_efficiency_rating', 'N/A'),
                'average_productivity_per_hour': summary_stats.get('average_aetherony_per_hour', 0),
                'most_productive_day': summary_stats.get('most_productive_day', 'N/A')
            },
            'business_metrics': {
                'estimated_development_hours': estimated_dev_hours,
                'estimated_development_cost_eur': estimated_cost,
                'generated_value_eur': aetheron_value_eur,
                'roi_percentage': round(roi_percentage, 2),
                'human_capital_efficiency': 'Vysoká' if roi_percentage > 100 else 'Stredná'
            },
            'cognitive_insights': {
                'average_cognitive_load': summary_stats.get('average_cognitive_load', 0),
                'cognitive_coherence_trend': 'Stable' if summary_stats.get('average_cognitive_load', 0) < 6 else 'High Load',
                'top_development_patterns': summary_stats.get('top_development_patterns', {})
            },
            'recommendations': self._generate_recommendations(summary_stats, total_aetherony)
        }
    
    def _generate_recommendations(self, stats: Dict, total_aetherony: float) -> List[str]:
        """AI-powered recommendations pre zlepšenie produktivity"""
        recommendations = []
        
        avg_cognitive_load = stats.get('average_cognitive_load', 5)
        avg_rhythm = stats.get('average_rhythm_score', 0.5)
        
        if avg_cognitive_load > 7:
            recommendations.append("🧠 Vysoká kognitívna záťaž - zvážte kratšie working sessions s prestávkami")
        
        if avg_rhythm < 0.6:
            recommendations.append("⚡ Nízky development rhythm - implementujte Pomodoro technique")
        
        if total_aetherony < 10:
            recommendations.append("📈 Nízka produktivita - analyzujte time management a eliminujte distrakcie")
        
        if 'debugging' in str(stats.get('top_development_patterns', {})):
            recommendations.append("🐛 Vysoký debugging ratio - investujte do test coverage a code review")
        
        recommendations.append("🏥 Slovak healthcare context: Optimálne pre part-time development vedľa medicínskej praxe")
        
        return recommendations
    
    def export_dashboard_report(self, output_dir: str = ".") -> str:
        """Export dashboard do HTML reportu"""
        if not self.audit_data:
            return ""
        
        # Generovanie všetkých chartov
        timeline_chart = self.create_productivity_timeline()
        heatmap_chart = self.create_daily_productivity_heatmap()
        radar_chart = self.create_cognitive_analysis_radar()
        session_chart = self.create_session_analysis_chart()
        
        executive_summary = self.generate_executive_summary()
        
        # HTML template
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Aethero Development Audit Dashboard</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; background: #1e1e1e; color: white; }}
                .container {{ max-width: 1200px; margin: 0 auto; }}
                .header {{ text-align: center; margin-bottom: 30px; }}
                .chart-container {{ margin: 20px 0; }}
                .summary-box {{ background: #2d2d2d; padding: 20px; border-radius: 10px; margin: 20px 0; }}
                .metric {{ display: inline-block; margin: 10px; padding: 15px; background: #3d3d3d; border-radius: 5px; }}
                .recommendations {{ background: #0d4f8c; padding: 15px; border-radius: 5px; margin: 10px 0; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🚀 Aethero Development Audit Dashboard</h1>
                    <h2>Slovak Healthcare Developer Performance Analysis</h2>
                    <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                </div>
                
                <div class="summary-box">
                    <h3>📊 Executive Summary</h3>
                    <div class="metric">
                        <strong>Total Aetherony:</strong> {executive_summary.get('performance_summary', {}).get('total_aetherony_generated', 0):.2f}
                    </div>
                    <div class="metric">
                        <strong>Efficiency Rating:</strong> {executive_summary.get('performance_summary', {}).get('development_efficiency_rating', 'N/A')}
                    </div>
                    <div class="metric">
                        <strong>ROI:</strong> {executive_summary.get('business_metrics', {}).get('roi_percentage', 0):.1f}%
                    </div>
                    <div class="metric">
                        <strong>Most Productive Day:</strong> {executive_summary.get('performance_summary', {}).get('most_productive_day', 'N/A')}
                    </div>
                </div>
                
                <div class="chart-container">
                    <div id="timeline-chart"></div>
                </div>
                
                <div class="chart-container">
                    <div id="heatmap-chart"></div>
                </div>
                
                <div class="chart-container">
                    <div id="radar-chart"></div>
                </div>
                
                <div class="chart-container">
                    <div id="session-chart"></div>
                </div>
                
                <div class="summary-box">
                    <h3>💡 AI-Powered Recommendations</h3>
                    {''.join([f'<div class="recommendations">{rec}</div>' for rec in executive_summary.get('recommendations', [])])}
                </div>
            </div>
            
            <script>
                Plotly.newPlot('timeline-chart', {timeline_chart.to_json()});
                Plotly.newPlot('heatmap-chart', {heatmap_chart.to_json()});
                Plotly.newPlot('radar-chart', {radar_chart.to_json()});
                Plotly.newPlot('session-chart', {session_chart.to_json()});
            </script>
        </body>
        </html>
        """
        
        # Zápis súboru
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"aethero_dashboard_{timestamp}.html"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filepath

def main():
    """Hlavná funkcia dashboard aplikácie"""
    dashboard = AetheroDashboard()
    
    if dashboard.load_latest_audit_data():
        print("🎯 Generujem Aethero Dashboard...")
        
        # Export HTML dashboard
        report_path = dashboard.export_dashboard_report()
        print(f"📊 Dashboard vygenerovaný: {report_path}")
        
        # Executive summary
        summary = dashboard.generate_executive_summary()
        print("\n" + "="*50)
        print("📈 EXECUTIVE SUMMARY")
        print("="*50)
        
        perf = summary.get('performance_summary', {})
        business = summary.get('business_metrics', {})
        
        print(f"🚀 Total Aetherony Generated: {perf.get('total_aetherony_generated', 0):.2f}")
        print(f"⚡ Efficiency Rating: {perf.get('development_efficiency_rating', 'N/A')}")
        print(f"💰 ROI: {business.get('roi_percentage', 0):.1f}%")
        print(f"🧠 Human Capital Efficiency: {business.get('human_capital_efficiency', 'N/A')}")
        
        print("\n💡 Recommendations:")
        for rec in summary.get('recommendations', []):
            print(f"   {rec}")
        
    else:
        print("❌ Spustite najprv aethero_audit.py pre generovanie dát")

if __name__ == "__main__":
    main()
