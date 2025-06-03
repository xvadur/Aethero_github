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
    outputs = {}
    for agent in agents:
        output = agent.run()
        outputs[agent.name] = output
    copilot_block = "```comment\n"
    for name, output in outputs.items():
        copilot_block += f"// {name} Output:\n{output}\n\n"
    copilot_block += "```"
    print(copilot_block)
    return outputs

if __name__ == "__main__":
    run_orchestration()
    # Prehľad logov (voliteľné):
    logs = AetheroBridge.read_logs()
    print("\n---\nVšetky logy:\n", "\n---\n".join(logs))