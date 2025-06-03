#!/usr/bin/env python3
"""
ASL Log Formatter Module - Aethero Syntax Language Log Formatter
Direktíva: AETH-PROMPT-GEN-2025-0003
Agent: Primus (Dirigens Primus Aetheri)
Verzia: 1.0

Deterministický ASL logovací formátovač pre agenta Archivus.
Bez stavovosti, bez externých závislostí.
"""

import uuid
from datetime import datetime
from typing import Dict, Any


class ASLLogFormatter:
    """
    ASL (Aethero Syntax Language) Log Formatter
    
    Deterministická trieda pre formátovanie štandardizovaných
    logovacích správ pre agenta Archivus.
    
    Princípy:
    - Bezstavovosť (stateless)
    - Determinizmus (okrem UUID generácie)
    - Žiadne externé závislosti
    - ASL kompatibilita
    """
    
    ASL_LOG_VERSION = "1.0"
    
    def format_log(self, 
                   agent_id: str, 
                   event_type: str, 
                   timestamp: datetime, 
                   payload: dict, 
                   status_code: int) -> Dict[str, Any]:
        """
        Formátuje ASL logovací záznam pre agenta Archivus.
        
        Args:
            agent_id (str): Identifikátor zdrojového agenta
            event_type (str): Typ udalosti (napr. "EXECUTION", "ERROR", "INFO")
            timestamp (datetime): Časová známka udalosti
            payload (dict): Dátový obsah správy
            status_code (int): Kód stavu vykonania (200=úspech, 500=chyba, atď.)
            
        Returns:
            Dict[str, Any]: Štruktúrovaná ASL logovacia správa
            
        Example:
            >>> formatter = ASLLogFormatter()
            >>> log = formatter.format_log(
            ...     agent_id="PRIMUS",
            ...     event_type="EXECUTION",
            ...     timestamp=datetime.now(),
            ...     payload={"action": "create_module", "result": "success"},
            ...     status_code=200
            ... )
            >>> print(log["aethero_log_version"])
            1.0
        """
        # Validácia vstupných parametrov
        if not isinstance(agent_id, str) or not agent_id.strip():
            raise ValueError("agent_id musí byť neprázdny string")
        
        if not isinstance(event_type, str) or not event_type.strip():
            raise ValueError("event_type musí byť neprázdny string")
        
        if not isinstance(timestamp, datetime):
            raise ValueError("timestamp musí byť datetime objekt")
        
        if not isinstance(payload, dict):
            raise ValueError("payload musí byť dictionary")
        
        if not isinstance(status_code, int):
            raise ValueError("status_code musí byť integer")
        
        # Generovanie unikátneho log_id (jediná nedeterministická operácia)
        log_id = str(uuid.uuid4())
        
        # Konverzia timestamp na ISO 8601 UTC formát
        timestamp_utc_iso = timestamp.isoformat() + "Z" if timestamp.tzinfo is None else timestamp.isoformat()
        
        # Deterministické vytvorenie ASL log štruktúry
        asl_log = {
            "aethero_log_version": self.ASL_LOG_VERSION,
            "log_id": log_id,
            "timestamp_utc_iso": timestamp_utc_iso,
            "source_agent_id": agent_id.strip().upper(),
            "event_type": event_type.strip().upper(),
            "execution_status_code": status_code,
            "data_payload": payload.copy()  # Shallow copy pre bezpečnosť
        }
        
        return asl_log
    
    @classmethod
    def create_standard_payload(cls, 
                               action: str, 
                               result: str = None, 
                               details: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Pomocná metóda pre vytvorenie štandardizovaného payload.
        
        Args:
            action (str): Vykonaná akcia
            result (str, optional): Výsledok akcie
            details (Dict[str, Any], optional): Dodatočné detaily
            
        Returns:
            Dict[str, Any]: Štandardizovaný payload
        """
        payload = {"action": action}
        
        if result is not None:
            payload["result"] = result
            
        if details is not None and isinstance(details, dict):
            payload["details"] = details.copy()
            
        return payload
    
    @classmethod
    def get_status_codes(cls) -> Dict[str, int]:
        """
        Vracia štandardné ASL status kódy.
        
        Returns:
            Dict[str, int]: Mapovanie názvov na kódy
        """
        return {
            "SUCCESS": 200,
            "CREATED": 201,
            "ACCEPTED": 202,
            "BAD_REQUEST": 400,
            "UNAUTHORIZED": 401,
            "FORBIDDEN": 403,
            "NOT_FOUND": 404,
            "INTERNAL_ERROR": 500,
            "NOT_IMPLEMENTED": 501,
            "SERVICE_UNAVAILABLE": 503
        }


# Príklad použitia modulu
if __name__ == "__main__":
    # Demonstrácia funkcionality ASL Log Formatter
    formatter = ASLLogFormatter()
    
    # Test základného logu
    test_timestamp = datetime(2025, 6, 2, 11, 30, 44)
    test_payload = formatter.create_standard_payload(
        action="module_creation",
        result="success",
        details={"module_name": "asl_log_formatter.py", "lines_of_code": 150}
    )
    
    test_log = formatter.format_log(
        agent_id="PRIMUS",
        event_type="EXECUTION",
        timestamp=test_timestamp,
        payload=test_payload,
        status_code=formatter.get_status_codes()["SUCCESS"]
    )
    
    print("🎯 ASL Log Formatter - Test Výstup:")
    print("=" * 50)
    for key, value in test_log.items():
        print(f"{key}: {value}")
    
    print("\n✅ ASL Log Formatter úspešne vytvorený!")
    print("📋 Modul pripravený pre agenta Archivus")
    print(f"🔧 Verzia ASL: {ASLLogFormatter.ASL_LOG_VERSION}")
