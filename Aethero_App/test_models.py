#!/usr/bin/env python3
"""
Test súbor pre overenie funkčnosti models.py s Pydantic v2
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'introspective_parser_module'))

from introspective_parser_module.models import (
    MentalStateEnum,
    EmotionToneEnum, 
    TemporalContextEnum,
    AetheroIntrospectiveEntity,
    ASLCognitiveTag
)

def test_enum_functionality():
    """Test základnej funkčnosti enumerácií"""
    print("🧠 Testovanie enumerácií...")
    
    # Test mentálnych stavov
    state = MentalStateEnum.CALM
    print(f"   Mentálny stav: {state}")
    
    # Test emocionálnych tónov
    emotion = EmotionToneEnum.ANALYTICAL
    print(f"   Emocionálny tón: {emotion}")
    
    # Test časových kontextov
    temporal = TemporalContextEnum.PRESENT
    print(f"   Časový kontext: {temporal}")

def test_introspective_entity():
    """Test základnej introspektívnej entity"""
    print("\n🔮 Testovanie AetheroIntrospectiveEntity...")
    
    entity = AetheroIntrospectiveEntity()
    print(f"   Entity ID: {entity.entity_id}")
    print(f"   Čas vytvorenia: {entity.creation_moment}")
    print(f"   Úroveň vedomia: {entity.consciousness_level}")

def test_asl_cognitive_tag():
    """Test hlavného ASL kognitívneho tagu"""
    print("\n🏷️  Testovanie ASLCognitiveTag...")
    
    try:
        tag = ASLCognitiveTag(
            thought_stream="Analyzujem komplexné myšlienkové procesy",
            mental_state=MentalStateEnum.ANALYTICAL,
            emotion_tone=EmotionToneEnum.ANALYTICAL,
            cognitive_load=5,
            temporal_context=TemporalContextEnum.PRESENT,
            certainty_level=0.8,
            aeth_mem_link="mem_001",
            constitutional_law="Zákon o vedomej analýze"
        )
        
        print(f"   Myšlienkový tok: {tag.thought_stream}")
        print(f"   Mentálny stav: {tag.mental_state}")
        print(f"   Kognitívna záťaž: {tag.cognitive_load}")
        print(f"   Úroveň istoty: {tag.certainty_level}")
        
        # Test introspektívnych metód
        tag.enhance_consciousness(0.2)
        print(f"   Zvýšené vedomie: {tag.consciousness_level}")
        
        tag.resonate_with_memory({"test": "memory_data"})
        print(f"   Pamäťová rezonancia: {tag.consciousness_resonance}")
        
    except Exception as e:
        print(f"   ❌ Chyba: {e}")
        return False
    
    return True

def test_validation_logic():
    """Test validačnej logiky"""
    print("\n✅ Testovanie validačnej logiky...")
    
    # Test nekonzistentného stavu - pokojný stav s vysokou kognitívnou záťažou
    try:
        invalid_tag = ASLCognitiveTag(
            thought_stream="Test",
            mental_state=MentalStateEnum.CALM,
            emotion_tone=EmotionToneEnum.NEUTRAL,
            cognitive_load=9,  # Vysoká záťaž s pokojným stavom
            temporal_context=TemporalContextEnum.PRESENT,
            certainty_level=0.5,
            aeth_mem_link="mem_test",
            constitutional_law="Test zákon"
        )
        print("   ❌ Validácia zlyhala - mal by byť error!")
        return False
    except ValueError as e:
        print(f"   ✅ Validácia funguje: {e}")
        return True

if __name__ == "__main__":
    print("🚀 Spúšťam testy pre Aethero introspektívne modely...\n")
    
    test_enum_functionality()
    test_introspective_entity()
    
    success = test_asl_cognitive_tag()
    if success:
        test_validation_logic()
    
    print("\n🎯 Testy dokončené!")
