# agents/plot_agent.py
from typing import Dict, Any
from agents.base import BaseAgent
from tools.setting_tool import search_setting
from tools.memory_tool import get_recent_memory, save_memory  # 引入记忆


class PlotAgent(BaseAgent):
    def __init__(self, config: Dict[str, Any]):
        super().__init__("PlotArchitect", config)

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        topic = input_data.get("topic", "")
        print(f"  [PlotAgent] 🧠 正在为你推演剧情：{topic}...")

        # 1. 使用 RAG 检索相关的世界观/设定
        setting_info = search_setting(topic)  # 注意这里用 topic 去检索，而不是写死的"主角设定"

        # 2. 获取短期记忆（前两章写了什么）
        history = get_recent_memory()

        # 3. 组装终极 Prompt
        prompt = f"""结合以下小说设定（自动从数据库检索）：
{setting_info}

【前情提要】（请保持剧情连贯）：
{history}

请围绕当前剧情节点【{topic}】，推演出 3 个不同的剧情走向。
要求：
1. 必须符合主角杀伐果断的性格（绝不能写圣母）。
2. 必须包含极高的期待感和爽点。
3. 简要描述每一段大概会发生什么。"""

        plot_result = self.chat(prompt, system_prompt="你是一个全网白金级的网文大神，精通番茄小说的爽文套路。")

        # 4. 将本次推进的剧情存入短期记忆
        save_memory(f"推进节点：{topic}")

        return {"plot_suggestions": plot_result}