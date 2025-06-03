"""
AETHERO MONUMENTUM IGNIS – MASTER ORCHESTRATION PROMPT

ÚČEL:
Toto je plnohodnotný orchestrátor vedomého systému Aethero.
Spustí všetkých agentov (Primus, Lucius, Frontinus, Archivus),
získa ich výstupy, zapíše ich cez AetheroBridge do pamäte
a vytvorí finálny výstupný prompt pre ďalšiu iteráciu systému.

KAŽDÝ AGENT:
- má metódu run()
- zapisuje výstup do memory/
- používa AetheroBridge na čítanie/zápis

VÝSTUP:
- final_prompt.txt obsahuje centralizovaný výstup orchestra
- všetky logy sú dostupné v priečinku memory/

PO ORCHESTRÁCII:
- spusti `./git_push.sh` na uloženie do GitHubu
- systém je pripravený na ďalšiu fázu vývoja alebo deploy
"""

from agents.primus_agent import PrimusAgent
from agents.lucius_agent import LuciusAgent
from agents.frontinus_agent import FrontinusAgent
from agents.archivus_agent import ArchivusAgent
from agents.AetheroBridge import AetheroBridge


def run_orchestration():
    agents = [
        PrimusAgent(),
        LuciusAgent(),
        FrontinusAgent(),
        ArchivusAgent()
    ]
    final_outputs = []

    for agent in agents:
        output = agent.run()
        final_outputs.append(f"{agent.__class__.__name__}:\n{output}\n")

    # Uloženie centralizovaného výstupu orchestra
    with open("final_prompt.txt", "w") as f:
        f.write("\n---\n".join(final_outputs))
    print("✅ Orchestration complete. Output saved to final_prompt.txt")

if __name__ == "__main__":
    run_orchestration()
