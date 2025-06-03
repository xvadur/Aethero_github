import os
import gradio as gr

def get_agents():
    files = os.listdir("memory")
    agents = set()
    for f in files:
        if f.endswith(".txt") and "_output_" in f:
            agents.add(f.split("_output_")[0])
    return sorted(list(agents))

def get_logs_for_agent(agent):
    files = os.listdir("memory")
    logs = [f for f in files if f.startswith(agent.lower()) and f.endswith(".txt")]
    logs.sort(reverse=True)
    return logs

def read_log(filename):
    with open(os.path.join("memory", filename), "r") as f:
        return f.read()

def export_log(filename, export_type):
    content = read_log(filename)
    export_dir = "memory"
    base = filename.rsplit(".txt", 1)[0]
    if export_type == "Markdown":
        out_path = os.path.join(export_dir, base + ".md")
        with open(out_path, "w") as f:
            f.write(f"# Log: {filename}\n\n" + content)
        return f"Exportované do {out_path}"
    elif export_type == "JSON":
        import json
        out_path = os.path.join(export_dir, base + ".json")
        with open(out_path, "w") as f:
            json.dump({"log": content}, f, ensure_ascii=False, indent=2)
        return f"Exportované do {out_path}"
    return "Neznámy formát"

def ui():
    agents = get_agents()
    with gr.Blocks() as demo:
        gr.Markdown("# Aethero Memory Viewer")
        agent = gr.Dropdown(choices=agents, label="Vyber agenta")
        log_file = gr.Dropdown(choices=[], label="Vyber log")
        log_content = gr.Textbox(label="Obsah logu", lines=20)
        export_type = gr.Radio(["Markdown", "JSON"], label="Exportovať ako")
        export_btn = gr.Button("Exportovať log")
        export_result = gr.Textbox(label="Export stav")

        def update_logs(agent):
            logs = get_logs_for_agent(agent)
            return gr.Dropdown.update(choices=logs, value=logs[0] if logs else None)

        def show_log(log_file):
            if log_file:
                return read_log(log_file)
            return ""

        agent.change(update_logs, agent, log_file)
        log_file.change(show_log, log_file, log_content)
        export_btn.click(lambda f, t: export_log(f, t), [log_file, export_type], export_result)
    return demo

if __name__ == "__main__":
    ui().launch()
