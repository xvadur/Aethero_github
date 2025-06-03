from agents.primus_agent import PrimusAgent
from agents.lucius_agent import LuciusAgent
from agents.frontinus_agent import FrontinusAgent
from agents.archivus_agent import ArchivusAgent
from agents.AetheroBridge import AetheroBridge

primus = PrimusAgent()
lucius = LuciusAgent()
frontinus = FrontinusAgent()
archivus = ArchivusAgent()

primus_output = primus.run()
lucius_output = lucius.run()
frontinus_output = frontinus.run()
archivus_output = archivus.run()

bridge = AetheroBridge()
bridge.log_output("Primus", primus_output)
bridge.log_output("Lucius", lucius_output)
bridge.log_output("Frontinus", frontinus_output)
bridge.log_output("Archivus", archivus_output)

final_prompt = f"""
# Aethero Orchestra Výstup

## Primus
{primus_output}

## Lucius
{lucius_output}

## Frontinus
{frontinus_output}

## Archivus
{archivus_output}
"""

with open("final_prompt.txt", "w") as f:
    f.write(final_prompt)

print("Orchestrácia dokončená. Výstupný prompt uložený do final_prompt.txt.")
