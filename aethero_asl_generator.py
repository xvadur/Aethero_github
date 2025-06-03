#!/usr/bin/env python3
"""
Aethero ASL Cognitive Tag Generator
Generovanie ASL cognitive tagov na základe development aktivít pre audit systém
"""

import json
import sys
import os
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import random
import uuid

# Import existujúcich Aethero komponentov
sys.path.append('/Users/_xvadur/Desktop/Aethero_github/Aethero_App')
from introspective_parser_module.models import (
    ASLCognitiveTag, MentalStateEnum, EmotionToneEnum, 
    TemporalContextEnum, AetheroIntrospectiveEntity
)
from introspective_parser_module.metrics import CognitiveMetricsAnalyzer

class DevelopmentActivityAnalyzer:
    """
    Analyzátor development aktivít pre generovanie ASL cognitive tagov
    """
    
    def __init__(self):
        self.cognitive_analyzer = CognitiveMetricsAnalyzer()
        
        # Mapping development patterns na cognitive states
        self.activity_cognitive_mapping = {
            # Git commit patterns
            'bug_fix': {
                'mental_state': MentalStateEnum.FOCUSED,
                'emotion_tone': EmotionToneEnum.ANALYTICAL,
                'cognitive_load_range': (6, 9),
                'certainty_range': (0.3, 0.6)
            },
            'feature_development': {
                'mental_state': MentalStateEnum.CONTEMPLATIVE,
                'emotion_tone': EmotionToneEnum.POSITIVE,
                'cognitive_load_range': (4, 7),
                'certainty_range': (0.6, 0.9)
            },
            'refactoring': {
                'mental_state': MentalStateEnum.REFLECTIVE,
                'emotion_tone': EmotionToneEnum.ANALYTICAL,
                'cognitive_load_range': (5, 8),
                'certainty_range': (0.7, 0.9)
            },
            'testing': {
                'mental_state': MentalStateEnum.DECISIVE,
                'emotion_tone': EmotionToneEnum.CRITICAL,
                'cognitive_load_range': (3, 6),
                'certainty_range': (0.8, 1.0)
            },
            # Shell command patterns
            'complex_scripting': {
                'mental_state': MentalStateEnum.FOCUSED,
                'emotion_tone': EmotionToneEnum.ANALYTICAL,
                'cognitive_load_range': (7, 10),
                'certainty_range': (0.4, 0.7)
            },
            'routine_commands': {
                'mental_state': MentalStateEnum.CALM,
                'emotion_tone': EmotionToneEnum.NEUTRAL,
                'cognitive_load_range': (2, 4),
                'certainty_range': (0.8, 1.0)
            },
            'debugging_investigation': {
                'mental_state': MentalStateEnum.CONFUSED,
                'emotion_tone': EmotionToneEnum.CRITICAL,
                'cognitive_load_range': (8, 10),
                'certainty_range': (0.1, 0.4)
            }
        }
        
        # Slovak healthcare developer specific patterns
        self.healthcare_dev_contexts = {
            'medical_break_context': {
                'mental_state': MentalStateEnum.REFLECTIVE,
                'emotion_tone': EmotionToneEnum.EMPATHETIC,
                'thought_stream_templates': [
                    "Premýšľam o integrácii zdravotníckych systémov počas prestávky",
                    "Analyzujem optimalizácie pre healthtech riešenie",
                    "Uvažujem o bezpečnosti pacientskych dát v novom module"
                ]
            },
            'evening_development': {
                'mental_state': MentalStateEnum.CONTEMPLATIVE,
                'emotion_tone': EmotionToneEnum.POSITIVE,
                'thought_stream_templates': [
                    "Večerný development - vyššia koncentrácia po medicínskej zmene",
                    "Implementujem funkcionalitu pre zdravotníckych pracovníkov",
                    "Optimalizujem workflow pre slovenskú zdravotnícku prax"
                ]
            },
            'weekend_coding': {
                'mental_state': MentalStateEnum.FOCUSED,
                'emotion_tone': EmotionToneEnum.ANALYTICAL,
                'thought_stream_templates': [
                    "Víkendový deep work na komplexnom healthcare module",
                    "Refaktoring healthcare API pre lepšiu integráciu",
                    "Implementácia AI asistenta pre slovenskú medicínu"
                ]
            }
        }
    
    def analyze_commit_cognitive_pattern(self, commit: Dict[str, Any]) -> str:
        """Analýza commit-u pre určenie cognitive pattern"""
        subject = commit.get('subject', '').lower()
        
        # Bug fixes
        if any(keyword in subject for keyword in ['fix', 'bug', 'error', 'issue']):
            return 'bug_fix'
        
        # Feature development
        if any(keyword in subject for keyword in ['feat', 'feature', 'add', 'implement', 'create']):
            return 'feature_development'
        
        # Refactoring
        if any(keyword in subject for keyword in ['refactor', 'clean', 'optimize', 'improve']):
            return 'refactoring'
        
        # Testing
        if any(keyword in subject for keyword in ['test', 'spec', 'coverage']):
            return 'testing'
        
        # Default
        return 'feature_development'
    
    def analyze_command_cognitive_pattern(self, command: Dict[str, Any]) -> str:
        """Analýza shell command pre určenie cognitive pattern"""
        cmd_text = command.get('command', '').lower()
        complexity = command.get('complexity_score', 3.0)
        
        # Complex scripting
        if complexity >= 7.0 or any(keyword in cmd_text for keyword in ['docker-compose', 'terraform', 'kubectl']):
            return 'complex_scripting'
        
        # Debugging investigation
        if any(keyword in cmd_text for keyword in ['grep -r', 'find', 'ps aux', 'netstat', 'strace']):
            return 'debugging_investigation'
        
        # Routine commands
        return 'routine_commands'
    
    def determine_slovak_healthcare_context(self, timestamp: datetime) -> Optional[str]:
        """Určenie slovenského zdravotníckeho kontextu na základe času"""
        hour = timestamp.hour
        weekday = timestamp.weekday()
        
        # Večerný development (po zdravotníckej zmene)
        if 18 <= hour <= 23 and weekday < 5:
            return 'evening_development'
        
        # Víkendový coding
        if weekday >= 5:  # Sobota, nedeľa
            return 'weekend_coding'
        
        # Prestávky v práci (obed, krátke prestávky)
        if (12 <= hour <= 13) or (15 <= hour <= 16) and weekday < 5:
            return 'medical_break_context'
        
        return None
    
    def generate_thought_stream(self, pattern: str, commit: Dict = None, command: Dict = None, 
                              healthcare_context: str = None) -> str:
        """Generovanie thought stream na základe patternu a kontextu"""
        
        base_templates = {
            'bug_fix': [
                "Identifikujem príčinu chyby v {context} module",
                "Analyzujem stack trace pre efektívne riešenie",
                "Debugging komplexného problému vyžaduje systematický prístup",
                "Riešim kritickú chybu ktorá blokuje {context} funkcionalitu"
            ],
            'feature_development': [
                "Implementujem novú funkcionalitu pre {context}",
                "Navrhujem architektúru pre scalable riešenie",
                "Vytvárám user-friendly interface pre healthcare workers",
                "Optimalizujem performance novej {context} feature"
            ],
            'refactoring': [
                "Vylepšujem code quality a maintainability",
                "Refaktoring legacy kódu pre lepšiu čitateľnosť",
                "Optimalizujem algoritmy pre vyššiu efektivitu",
                "Restructuring {context} module pre lepšiu architektúru"
            ],
            'testing': [
                "Zabezpečujem quality assurance pre {context}",
                "Vytváram comprehensive test coverage",
                "Validujem funkcionalitu pre production deployment",
                "Testing edge cases pre robustné riešenie"
            ],
            'complex_scripting': [
                "Automatizujem complex deployment process",
                "Konfigurujem infraštruktúru pre {context}",
                "Scripting pre efektívnejší development workflow",
                "Implementujem CI/CD pipeline optimalizácie"
            ],
            'debugging_investigation': [
                "Vyšetrujem neočakávané správanie systému",
                "Analyzujem system logs pre root cause",
                "Troubleshooting komplexného infrastructure problému",
                "Identifikujem performance bottleneck v {context}"
            ],
            'routine_commands': [
                "Vykonávam bežné development operácie",
                "Navigujem projektovou štruktúrou efektívne",
                "Jednoduchý task management a file operations",
                "Udržiavam development environment"
            ]
        }
        
        # Výber template
        templates = base_templates.get(pattern, base_templates['feature_development'])
        template = random.choice(templates)
        
        # Určenie kontextu na základe dostupných informácií
        context = "healthcare"
        if commit:
            if 'health' in commit.get('subject', '').lower():
                context = "healthcare system"
            elif 'api' in commit.get('subject', '').lower():
                context = "API"
            elif 'ui' in commit.get('subject', '').lower():
                context = "user interface"
        
        # Healthcare context enhancement
        if healthcare_context and healthcare_context in self.healthcare_dev_contexts:
            hc_templates = self.healthcare_dev_contexts[healthcare_context]['thought_stream_templates']
            if random.random() < 0.3:  # 30% šanca na healthcare-specific thought
                return random.choice(hc_templates)
        
        return template.format(context=context)
    
    def generate_asl_cognitive_tag(self, activity_data: Dict[str, Any], 
                                  pattern: str, timestamp: datetime) -> ASLCognitiveTag:
        """Generovanie ASL cognitive tag pre konkrétnu aktivitu"""
        
        # Získanie cognitive mapping pre pattern
        cognitive_mapping = self.activity_cognitive_mapping.get(pattern, 
                           self.activity_cognitive_mapping['feature_development'])
        
        # Healthcare context
        healthcare_context = self.determine_slovak_healthcare_context(timestamp)
        if healthcare_context and healthcare_context in self.healthcare_dev_contexts:
            hc_context = self.healthcare_dev_contexts[healthcare_context]
            # Override cognitive states for healthcare context
            if random.random() < 0.4:  # 40% šanca na healthcare override
                cognitive_mapping['mental_state'] = hc_context['mental_state']
                cognitive_mapping['emotion_tone'] = hc_context['emotion_tone']
        
        # Generovanie hodnôt
        cognitive_load = random.randint(*cognitive_mapping['cognitive_load_range'])
        certainty_level = random.uniform(*cognitive_mapping['certainty_range'])
        
        # Temporal context na základe času
        hour = timestamp.hour
        if 6 <= hour <= 12:
            temporal_context = TemporalContextEnum.PRESENT
        elif 13 <= hour <= 18:
            temporal_context = TemporalContextEnum.FUTURE
        else:
            temporal_context = TemporalContextEnum.PAST
        
        # Thought stream generovanie
        commit_data = activity_data.get('commit')
        command_data = activity_data.get('command') 
        thought_stream = self.generate_thought_stream(
            pattern, commit_data, command_data, healthcare_context
        )
        
        # Constitutional law - Slovak healthcare specific
        constitutional_laws = [
            "Zákon č. 576/2004 Z. z. o zdravotnej starostlivosti - digitalizácia",
            "GDPR compliance pre pacientske dáta",
            "Zákon č. 18/2018 Z. z. o ochrane osobných údajov",
            "ISO 27001 - bezpečnosť zdravotníckych informácií",
            "Etický kódex pre healthcare AI systémy"
        ]
        constitutional_law = random.choice(constitutional_laws)
        
        # Enhancement suggestions
        enhancement_suggestions = [
            "Implementovať batch processing pre vyššiu efektivitu",
            "Pridať comprehensive logging pre lepší debugging",
            "Optimalizovať databázové queries",
            "Implementovať caching layer pre performance",
            "Pridať automated testing coverage",
            "Vylepšiť error handling a user feedback",
            "Implementovať real-time monitoring",
            "Optimalizovať mobile responsiveness"
        ]
        
        # Diplomatic enhancement for Slovak healthcare context
        diplomatic_enhancements = [
            "Zohľadniť potreby slovenských zdravotníckych pracovníkov",
            "Integrovať s existujúcimi nemocničnými systémami",
            "Zabezpečiť compliance s SK zdravotníckou legislatívou",
            "Optimalizovať pre slovenské jazykové špecifiká",
            "Koordinovať s Ministerstvom zdravotníctva SR",
            "Implementovať podporu pre rural healthcare",
            "Zabezpečiť interoperabilitu s eHealth systémami"
        ]
        
        try:
            # Vytvorenie ASL cognitive tag
            asl_tag = ASLCognitiveTag(
                thought_stream=thought_stream,
                mental_state=cognitive_mapping['mental_state'],
                emotion_tone=cognitive_mapping['emotion_tone'],
                cognitive_load=cognitive_load,
                temporal_context=temporal_context,
                certainty_level=certainty_level,
                aeth_mem_link=f"mem_link_{uuid.uuid4().hex[:8]}",
                constitutional_law=constitutional_law,
                enhancement_suggestion=random.choice(enhancement_suggestions),
                diplomatic_enhancement=random.choice(diplomatic_enhancements)
            )
            
            return asl_tag
            
        except Exception as e:
            print(f"[ERROR] Failed to create ASL tag: {e}")
            # Fallback simple tag
            return self._create_fallback_tag(thought_stream, timestamp)
    
    def _create_fallback_tag(self, thought_stream: str, timestamp: datetime) -> ASLCognitiveTag:
        """Vytvorenie fallback ASL tag v prípade chyby"""
        return ASLCognitiveTag(
            thought_stream=thought_stream,
            mental_state=MentalStateEnum.CALM,
            emotion_tone=EmotionToneEnum.NEUTRAL,
            cognitive_load=5,
            temporal_context=TemporalContextEnum.PRESENT,
            certainty_level=0.7,
            aeth_mem_link=f"fallback_{uuid.uuid4().hex[:8]}",
            constitutional_law="Základný etický kódex pre AI systémy",
            enhancement_suggestion="Optimalizovať cognitive tag generation",
            diplomatic_enhancement="Zlepšiť error handling pre ASL systém"
        )

class AetheroASLGenerator:
    """
    Hlavný generátor ASL cognitive tagov pre audit systém
    """
    
    def __init__(self):
        self.activity_analyzer = DevelopmentActivityAnalyzer()
        self.cognitive_analyzer = CognitiveMetricsAnalyzer()
    
    def load_audit_data(self, audit_file: str) -> Optional[Dict[str, Any]]:
        """Načítanie audit dát"""
        try:
            with open(audit_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[ERROR] Failed to load audit data: {e}")
            return None
    
    def generate_asl_tags_from_audit(self, audit_data: Dict[str, Any]) -> List[ASLCognitiveTag]:
        """Generovanie ASL tagov z audit dát"""
        asl_tags = []
        
        # Processing development sessions
        sessions = audit_data.get('development_sessions', [])
        
        for session in sessions:
            session_start = datetime.fromisoformat(session['start_time'])
            
            # Simulácia aktivít v rámci session
            commits_count = session.get('commits_count', 0)
            commands_count = session.get('commands_count', 0)
            
            # Generovanie tagov na základe aktivít
            total_activities = commits_count + commands_count
            if total_activities == 0:
                continue
                
            # Rozdelenie času session na aktivity
            session_duration = timedelta(hours=session.get('duration_hours', 1))
            activity_interval = session_duration / total_activities if total_activities > 0 else timedelta(minutes=30)
            
            current_time = session_start
            
            # Generovanie commit tagov
            for i in range(commits_count):
                commit_data = {
                    'commit': {
                        'subject': f"Commit {i+1} in session",
                        'timestamp': current_time
                    }
                }
                
                pattern = self.activity_analyzer.analyze_commit_cognitive_pattern(commit_data['commit'])
                asl_tag = self.activity_analyzer.generate_asl_cognitive_tag(
                    commit_data, pattern, current_time
                )
                asl_tags.append(asl_tag)
                current_time += activity_interval
            
            # Generovanie command tagov
            for i in range(commands_count):
                command_data = {
                    'command': {
                        'command': f"development_command_{i+1}",
                        'complexity_score': random.uniform(3.0, 8.0),
                        'timestamp': current_time
                    }
                }
                
                pattern = self.activity_analyzer.analyze_command_cognitive_pattern(command_data['command'])
                asl_tag = self.activity_analyzer.generate_asl_cognitive_tag(
                    command_data, pattern, current_time
                )
                asl_tags.append(asl_tag)
                current_time += activity_interval
        
        return asl_tags
    
    def calculate_cognitive_coherence_metrics(self, asl_tags: List[ASLCognitiveTag]) -> Dict[str, Any]:
        """Výpočet cognitive coherence metrík"""
        if not asl_tags:
            return {}
        
        coherence_rate = self.cognitive_analyzer.calculate_consciousness_coherence_rate(asl_tags)
        
        # Dodatočné analýzy
        mental_state_distribution = {}
        emotion_tone_distribution = {}
        cognitive_load_stats = []
        certainty_stats = []
        
        for tag in asl_tags:
            # Distribúcie
            mental_state = tag.mental_state.value
            emotion_tone = tag.emotion_tone.value
            
            mental_state_distribution[mental_state] = mental_state_distribution.get(mental_state, 0) + 1
            emotion_tone_distribution[emotion_tone] = emotion_tone_distribution.get(emotion_tone, 0) + 1
            
            # Štatistiky
            cognitive_load_stats.append(tag.cognitive_load)
            certainty_stats.append(tag.certainty_level)
        
        import statistics
        
        return {
            'consciousness_coherence_rate': coherence_rate,
            'total_tags_analyzed': len(asl_tags),
            'mental_state_distribution': mental_state_distribution,
            'emotion_tone_distribution': emotion_tone_distribution,
            'cognitive_load_statistics': {
                'mean': statistics.mean(cognitive_load_stats),
                'median': statistics.median(cognitive_load_stats),
                'stdev': statistics.stdev(cognitive_load_stats) if len(cognitive_load_stats) > 1 else 0
            },
            'certainty_statistics': {
                'mean': statistics.mean(certainty_stats),
                'median': statistics.median(certainty_stats),
                'stdev': statistics.stdev(certainty_stats) if len(certainty_stats) > 1 else 0
            }
        }
    
    def export_asl_tags(self, asl_tags: List[ASLCognitiveTag], 
                       coherence_metrics: Dict[str, Any]) -> str:
        """Export ASL tagov do JSON súboru"""
        
        # Konverzia ASL tagov na serializovateľné objekty
        tags_data = []
        for tag in asl_tags:
            tag_dict = {
                'entity_id': tag.entity_id,
                'creation_moment': tag.creation_moment.isoformat(),
                'consciousness_level': tag.consciousness_level,
                'thought_stream': tag.thought_stream,
                'mental_state': tag.mental_state.value,
                'emotion_tone': tag.emotion_tone.value,
                'cognitive_load': tag.cognitive_load,
                'temporal_context': tag.temporal_context.value,
                'certainty_level': tag.certainty_level,
                'aeth_mem_link': tag.aeth_mem_link,
                'constitutional_law': tag.constitutional_law,
                'enhancement_suggestion': tag.enhancement_suggestion,
                'diplomatic_enhancement': tag.diplomatic_enhancement,
                'introspective_depth': tag.introspective_depth,
                'consciousness_resonance': tag.consciousness_resonance
            }
            tags_data.append(tag_dict)
        
        # Export data
        export_data = {
            'asl_generation_metadata': {
                'generated_at': datetime.now().isoformat(),
                'total_tags': len(asl_tags),
                'generation_context': 'aethero_audit_system',
                'slovak_healthcare_optimization': True
            },
            'cognitive_coherence_analysis': coherence_metrics,
            'asl_cognitive_tags': tags_data
        }
        
        # Zápis súboru
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"aethero_asl_cognitive_tags_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        print(f"[ASL] Exported {len(asl_tags)} cognitive tags to: {filename}")
        return filename
    
    def run_asl_generation(self, audit_file: str = None) -> Optional[str]:
        """Spustenie celého ASL generation procesu"""
        
        # Hľadanie najnovšieho audit súboru ak nie je špecifikovaný
        if not audit_file:
            import glob
            audit_files = glob.glob("aethero_audit_*.json")
            if not audit_files:
                print("[ERROR] No audit files found. Run aethero_audit.py first.")
                return None
            audit_file = max(audit_files, key=os.path.getctime)
        
        print(f"🧠 ASL Cognitive Tag Generation - Processing: {audit_file}")
        
        # Načítanie audit dát
        audit_data = self.load_audit_data(audit_file)
        if not audit_data:
            return None
        
        # Generovanie ASL tagov
        print("🔄 Generating ASL cognitive tags from development activities...")
        asl_tags = self.generate_asl_tags_from_audit(audit_data)
        
        if not asl_tags:
            print("[WARNING] No ASL tags generated")
            return None
        
        # Analýza cognitive coherence
        print("📊 Analyzing cognitive coherence metrics...")
        coherence_metrics = self.calculate_cognitive_coherence_metrics(asl_tags)
        
        # Export
        print("💾 Exporting ASL cognitive tags...")
        export_file = self.export_asl_tags(asl_tags, coherence_metrics)
        
        # Súhrn
        print("\n" + "="*50)
        print("🧠 ASL COGNITIVE TAG GENERATION COMPLETE")
        print("="*50)
        print(f"📊 Generated Tags: {len(asl_tags)}")
        print(f"🎯 Consciousness Coherence: {coherence_metrics.get('consciousness_coherence_rate', 0):.3f}")
        print(f"🧠 Avg Cognitive Load: {coherence_metrics.get('cognitive_load_statistics', {}).get('mean', 0):.1f}/10")
        print(f"✅ Export File: {export_file}")
        
        return export_file

def main():
    """Hlavná funkcia ASL generátora"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Aethero ASL Cognitive Tag Generator')
    parser.add_argument('--audit-file', type=str, help='Specific audit file to process')
    
    args = parser.parse_args()
    
    generator = AetheroASLGenerator()
    result = generator.run_asl_generation(args.audit_file)
    
    if result:
        print(f"\n✅ ASL generation completed successfully!")
        print(f"📄 Output file: {result}")
    else:
        print("\n❌ ASL generation failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
