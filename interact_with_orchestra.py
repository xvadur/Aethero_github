from agents.AetheroBridge import AetheroBridge
from agents.primus_agent import PrimusAgent
from agents.lucius_agent import LuciusAgent
from agents.frontinus_agent import FrontinusAgent
from agents.archivus_agent import ArchivusAgent

# Načítaj posledné výstupy agentov
def read_last_log(agent_name):
    logs = AetheroBridge.read_logs()
    logs = [l for l in logs if agent_name.lower() in l.lower()]
    return logs[-1] if logs else "(Žiadny log nenájdený)"

bridge = AetheroBridge()
previous_outputs = {
    "Primus": read_last_log("Primus"),
    "Lucius": read_last_log("Lucius"),
    "Frontinus": read_last_log("Frontinus"),
    "Archivus": read_last_log("Archivus")
}

print("\n🧠 Posledné výstupy agentov:\n")
for name, output in previous_outputs.items():
    print(f"--- {name} ---\n{output}\n")

# 📝 Zadaj nový globálny príkaz
new_instruction = input("Zadaj nový globálny príkaz pre všetkých agentov: ")

primus = PrimusAgent(instruction=new_instruction)
lucius = LuciusAgent(instruction=new_instruction)
frontinus = FrontinusAgent(instruction=new_instruction)
archivus = ArchivusAgent(instruction=new_instruction)

primus_output = primus.run()
lucius_output = lucius.run()
frontinus_output = frontinus.run()
archivus_output = archivus.run()

bridge.log_output("Primus", primus_output)
bridge.log_output("Lucius", lucius_output)
bridge.log_output("Frontinus", frontinus_output)
bridge.log_output("Archivus", archivus_output)

print("\n✅ Nový cyklus ukončený. Výstupy sú zapísané do pamäte.")
