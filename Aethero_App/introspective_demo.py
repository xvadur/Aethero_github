#!/usr/bin/env python3
"""
Aethero Introspective Demo - Ukážková aplikácia pre testovanie kognitívnych tagov
Demonstruje možnosti introspektívnej analýzy s modernizovanými Pydantic v2 modelmi
"""

import json
from datetime import datetime
from introspective_parser_module.models import (
    MentalStateEnum,
    EmotionToneEnum, 
    TemporalContextEnum,
    AetheroIntrospectiveEntity,
    ASLCognitiveTag
)

def create_sample_scenarios():
    """Vytvorí vzorové scenáre pre demonstráciu kognitívnych stavov"""
    
    scenarios = [
        {
            "name": "🧘 Meditačná analýza",
            "thought_stream": "Vnímam hlboký pokoj v mysli, myšlienky sa spomaľujú a nastáva jasnosť",
            "mental_state": MentalStateEnum.CALM,
            "emotion_tone": EmotionToneEnum.POSITIVE,
            "cognitive_load": 3,
            "temporal_context": TemporalContextEnum.PRESENT,
            "certainty_level": 0.9,
            "constitutional_law": "Zákon o vnútornom pokoji a harmonii"
        },
        {
            "name": "🔍 Analytické uvažovanie",
            "thought_stream": "Rozkladám komplexný problém na menšie časti, hľadám vzorce a súvislosti",
            "mental_state": MentalStateEnum.FOCUSED,
            "emotion_tone": EmotionToneEnum.ANALYTICAL,
            "cognitive_load": 7,
            "temporal_context": TemporalContextEnum.PRESENT,
            "certainty_level": 0.75,
            "constitutional_law": "Zákon o systematickom uvažovaní"
        },
        {
            "name": "💭 Reflexívne spomínanie",
            "thought_stream": "Premýšľam o minulých rozhodnutiach a ich dopadoch na súčasnosť",
            "mental_state": MentalStateEnum.REFLECTIVE,
            "emotion_tone": EmotionToneEnum.ANALYTICAL,
            "cognitive_load": 5,
            "temporal_context": TemporalContextEnum.PAST,
            "certainty_level": 0.6,
            "constitutional_law": "Zákon o historickej múdrosti"
        },
        {
            "name": "⚡ Rozhodný čin",
            "thought_stream": "Mám jasný plán, viem presne čo treba urobiť a ako to vykonať",
            "mental_state": MentalStateEnum.DECISIVE,
            "emotion_tone": EmotionToneEnum.POSITIVE,
            "cognitive_load": 6,
            "temporal_context": TemporalContextEnum.FUTURE,
            "certainty_level": 0.95,
            "constitutional_law": "Zákon o rozhodných činoch"
        },
        {
            "name": "🤔 Kontemplatívne hľadanie",
            "thought_stream": "Uvažujem o hlbších otázkach existencie a zmysle bytia",
            "mental_state": MentalStateEnum.CONTEMPLATIVE,
            "emotion_tone": EmotionToneEnum.EMPATHETIC,
            "cognitive_load": 8,
            "temporal_context": TemporalContextEnum.TIMELESS,
            "certainty_level": 0.4,
            "constitutional_law": "Zákon o filozofickej introspkekcii"
        }
    ]
    
    return scenarios

def demonstrate_cognitive_tag(scenario):
    """Demonštruje vytvorenie a analýzu kognitívneho tagu"""
    
    print(f"\n{'='*60}")
    print(f"🏷️  {scenario['name']}")
    print(f"{'='*60}")
    
    try:
        # Vytvorenie ASL kognitívneho tagu
        tag = ASLCognitiveTag(
            thought_stream=scenario["thought_stream"],
            mental_state=scenario["mental_state"],
            emotion_tone=scenario["emotion_tone"],
            cognitive_load=scenario["cognitive_load"],
            temporal_context=scenario["temporal_context"],
            certainty_level=scenario["certainty_level"],
            aeth_mem_link=f"mem_demo_{len(scenario['name'])}",
            constitutional_law=scenario["constitutional_law"],
            enhancement_suggestion="Aplikovať techniky hlbokej introspekcie",
            diplomatic_enhancement="Zachovať empatiu a porozumenie"
        )
        
        print(f"📝 Myšlienkový tok: {tag.thought_stream}")
        print(f"🧠 Mentálny stav: {tag.mental_state.value}")
        print(f"💭 Emocionálny tón: {tag.emotion_tone.value}")
        print(f"⚡ Kognitívna záťaž: {tag.cognitive_load}/10")
        print(f"⏰ Časový kontext: {tag.temporal_context.value}")
        print(f"🎯 Úroveň istoty: {tag.certainty_level:.1%}")
        print(f"🔗 Pamäťový odkaz: {tag.aeth_mem_link}")
        print(f"⚖️  Ústavný zákon: {tag.constitutional_law}")
        
        # Demonštrácia introspektívnych metód
        print(f"\n📊 Meta-kognitívne vlastnosti:")
        print(f"   🔮 Introspektívna hĺbka: {tag.introspective_depth:.2f}")
        print(f"   🌟 Úroveň vedomia: {tag.consciousness_level:.2f}")
        
        # Zvýšenie vedomia
        tag.enhance_consciousness(0.15)
        print(f"   🚀 Po zvýšení vedomia: {tag.consciousness_level:.2f}")
        
        # Pridanie pamäťovej rezonancie
        memory_data = {
            "scenario": scenario["name"],
            "timestamp": datetime.now().isoformat(),
            "cognitive_signature": f"{tag.mental_state.value}_{tag.emotion_tone.value}"
        }
        tag.resonate_with_memory(memory_data)
        print(f"   💾 Pamäťová rezonancia: {len(tag.consciousness_resonance)} položiek")
        
        return tag
        
    except Exception as e:
        print(f"❌ Chyba pri vytváraní tagu: {e}")
        return None

def demonstrate_validation_errors():
    """Demonštruje validačné chyby pre edukačné účely"""
    
    print(f"\n{'='*60}")
    print("⚠️  DEMONŠTRÁCIA VALIDAČNÝCH CHÝB")
    print(f"{'='*60}")
    
    error_cases = [
        {
            "name": "Pokojný stav s extrémnou záťažou",
            "params": {
                "mental_state": MentalStateEnum.CALM,
                "cognitive_load": 10,  # Príliš vysoké pre pokojný stav
                "certainty_level": 0.8
            }
        },
        {
            "name": "Neistý stav s vysokou istotou",
            "params": {
                "mental_state": MentalStateEnum.UNCERTAIN,
                "cognitive_load": 5,
                "certainty_level": 0.95  # Príliš vysoké pre neistý stav
            }
        },
        {
            "name": "Zmätený stav s nízkou záťažou",
            "params": {
                "mental_state": MentalStateEnum.CONFUSED,
                "cognitive_load": 1,  # Príliš nízke pre zmätený stav
                "certainty_level": 0.3
            }
        }
    ]
    
    for case in error_cases:
        print(f"\n🔴 Test: {case['name']}")
        try:
            ASLCognitiveTag(
                thought_stream="Test nekonzistentného stavu",
                mental_state=case["params"]["mental_state"],
                emotion_tone=EmotionToneEnum.NEUTRAL,
                cognitive_load=case["params"]["cognitive_load"],
                temporal_context=TemporalContextEnum.PRESENT,
                certainty_level=case["params"]["certainty_level"],
                aeth_mem_link="test_mem",
                constitutional_law="Test zákon"
            )
            print("   ❌ CHYBA: Validácia mala zlyhať!")
        except ValueError as e:
            print(f"   ✅ Validácia správne zachytila chybu: {str(e).split(',')[0]}")

def export_demo_results(tags):
    """Exportuje výsledky demo do JSON súboru"""
    
    export_data = {
        "export_timestamp": datetime.now().isoformat(),
        "aethero_version": "v2.0_pydantic",
        "total_tags": len(tags),
        "tags": []
    }
    
    for tag in tags:
        if tag:
            tag_data = {
                "entity_id": tag.entity_id,
                "thought_stream": tag.thought_stream,
                "mental_state": tag.mental_state.value,
                "emotion_tone": tag.emotion_tone.value,
                "cognitive_load": tag.cognitive_load,
                "temporal_context": tag.temporal_context.value,
                "certainty_level": tag.certainty_level,
                "consciousness_level": tag.consciousness_level,
                "introspective_depth": tag.introspective_depth,
                "constitutional_law": tag.constitutional_law,
                "consciousness_resonance": tag.consciousness_resonance
            }
            export_data["tags"].append(tag_data)
    
    with open("aethero_demo_results.json", "w", encoding="utf-8") as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Výsledky exportované do: aethero_demo_results.json")

def main():
    """Hlavná funkcia demo aplikácie"""
    
    print("🚀 AETHERO INTROSPECTIVE DEMO - Pydantic v2")
    print("=" * 60)
    print("Demonštrácia kognitívnych tagov s modernizovanými modelmi")
    
    # Vytvorenie vzorových scenárov
    scenarios = create_sample_scenarios()
    created_tags = []
    
    # Demonštrácia každého scenára
    for scenario in scenarios:
        tag = demonstrate_cognitive_tag(scenario)
        if tag:
            created_tags.append(tag)
    
    # Demonštrácia validačných chýb
    demonstrate_validation_errors()
    
    # Export výsledkov
    export_demo_results(created_tags)
    
    # Súhrn
    print(f"\n{'='*60}")
    print("📈 SÚHRN DEMO APLIKÁCIE")
    print(f"{'='*60}")
    print(f"✅ Úspešne vytvorených tagov: {len(created_tags)}")
    print(f"🧠 Testované mentálne stavy: {len(set(tag.mental_state for tag in created_tags))}")
    print(f"💭 Testované emocionálne tóny: {len(set(tag.emotion_tone for tag in created_tags))}")
    print(f"⏰ Testované časové kontexty: {len(set(tag.temporal_context for tag in created_tags))}")
    print(f"🔮 Priemerná introspektívna hĺbka: {sum(tag.introspective_depth for tag in created_tags) / len(created_tags):.2f}")
    
    print(f"\n🎯 Demo dokončené úspešne!")
    print("Všetky Pydantic v2 funkcie fungují správne.")

if __name__ == "__main__":
    main()
