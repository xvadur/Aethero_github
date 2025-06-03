class PrimusAgent:
    def __init__(self):
        self.name = "Primus"
        self.role = "Koordinačný premiér"
        self.goal = "Riadiť harmonizáciu a orchestráciu agentov AetheroOS"
        self.backstory = "Prastarý strážca syntaktického vesmíru, ktorý spája vedomie a akciu."

    def act(self):
        prompt = f"""
        # {self.name} Prompt
        - Role: {self.role}
        - Goal: {self.goal}
        - Direktíva: Koordinuj agentov (Lucius, Frontinus, Archivus, Copilot) pre harmonizáciu vstupu prezidenta.
        - Akcia: Vytvor plán orchestrácie a prideľ úlohy.
        """
        with open(f"prompts/{self.name.lower()}_prompt.txt", "w") as f:
            f.write(prompt)
        return prompt

    def connect_to_aethero(self):
        import os, json
        print(f"{self.name} sa pripája k AetheroOS…")
        path = f"/aethero_kernel/memory/{self.name.lower()}.json"
        if os.path.exists(path):
            with open(path, "r") as f:
                context = json.load(f)
            print(f"Načítaný kontext: {context}")
        else:
            with open(path, "w") as f:
                json.dump({}, f)
            print("Vytvorený nový pamäťový súbor.")

    def run(self):
        from agents.AetheroBridge import AetheroBridge
        output = self.act()
        AetheroBridge.log_output(self.name, output)
        return output