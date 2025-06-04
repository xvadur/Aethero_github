import gradio as gr
import os
from aethero_monumentum_ignis import run_orchestration
from datetime import datetime
from aslr_analyzer import ASLAnalyzer

def analyze_text_with_visuals(input_text):
    """
    Analyze the input text and generate visualizations.

    Args:
        input_text (str): The text to analyze.

    Returns:
        str: Path to the generated radar chart.
    """
    analyzer = ASLAnalyzer(input_text)
    analysis = analyzer.analyze_text()

    # Generate radar chart
    from plot_emotions import plot_radar_chart
    radar_chart_path = "outputs/visualizations/radar_chart.png"
    plot_radar_chart(analysis["emotion_map"], radar_chart_path)

    return radar_chart_path

def orchestrate_and_return_log(_):
    """
    Spustí orchestráciu a vráti cestu k log súboru.
    """
    # Spustenie orchestrácie
    run_orchestration()
    # Presun final_prompt.txt do memory/orchestration_logs/ s timestampom
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("memory/orchestration_logs", exist_ok=True)
    src = "final_prompt.txt"
    dst = f"memory/orchestration_logs/orchestration_{ts}.txt"
    if os.path.exists(src):
        os.rename(src, dst)
        return dst
    return "Orchestration log not found."

iface = gr.Interface(
    fn=analyze_text_with_visuals,
    inputs="text",
    outputs="image",
    title="Aethero Emotion Analyzer",
    description="Analyze text and visualize emotions with radar charts."
)

iface_orchestrate = gr.Interface(
    fn=orchestrate_and_return_log,
    inputs=None,
    outputs="text",
    title="Aethero Orchestration Trigger",
    description="Spustí orchestráciu všetkých agentov a uloží log do memory/orchestration_logs/."
)

if __name__ == "__main__":
    iface.launch()
    iface_orchestrate.launch()
