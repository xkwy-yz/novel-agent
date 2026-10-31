# tools/memory_tool.py
import os
import json

MEMORY_FILE = "novel_memory.json"

def save_memory(plot_text: str):
    history = []
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
    history.append(plot_text)
    history = history[-2:] # 只保留最近 2 条，防止 token 太长
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def get_recent_memory() -> str:
    if not os.path.exists(MEMORY_FILE):
        return "暂无前情提要。"
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)
    return "\n".join(history) if history else "暂无前情提要。"