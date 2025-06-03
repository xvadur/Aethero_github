import os
import json
import datetime

class AetheroBridge:
    """
    Centrálna trieda na komunikáciu agentov s AetheroOS pamäťou.
    """
    @staticmethod
    def load_context(agent_name):
        path = f"/aethero_kernel/memory/{agent_name.lower()}.json"
        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)
        else:
            with open(path, "w") as f:
                json.dump({}, f)
            return {}

    @staticmethod
    def save_context(agent_name, context):
        path = f"/aethero_kernel/memory/{agent_name.lower()}.json"
        with open(path, "w") as f:
            json.dump(context, f)

    @staticmethod
    def log(agent_name, message):
        print(f"[AetheroBridge][{agent_name}] {message}")

    @staticmethod
    def log_output(agent, content):
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        log_dir = "memory"
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, f"{agent.lower()}_output_{ts}.txt")
        with open(log_path, "w") as f:
            f.write(content if isinstance(content, str) else str(content))

    @staticmethod
    def read_logs():
        log_dir = "memory"
        if not os.path.exists(log_dir):
            return []
        logs = []
        for fname in os.listdir(log_dir):
            if fname.endswith(".txt"):
                with open(os.path.join(log_dir, fname), "r") as f:
                    logs.append(f.read())
        return logs
