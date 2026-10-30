from typing import Dict, Any
from agents.base import BaseAgent
from tools.setting_tool import search_setting


class PlotAgent(BaseAgent):
    def __init__(self, config: Dict[str, Any]):
        super().__init__("PlotArchitect", config)

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        topic = input_data.get("topic", "")
        print(f"  [PlotAgent] 🧠 正在为你推演剧情：{topic}...")

        # 1. 检索设定，防止人设崩塌
        setting_info = search_setting("主角设定")

        # 2. 生成三个爽点走向
        prompt = f"""结合以下小说设定：
{setting_info}

请围绕当前剧情节点【{topic}】，推演出 3 个不同的剧情走向。
要求：
1. 必须符合主角杀伐果断的性格（绝不能写圣母）。
2. 必须包含极高的期待感和爽点。
3. 简要描述每一段大概会发生什么。"""

        plot_result = self.chat(prompt, system_prompt="你是一个全网白金级的网文大神，精通番茄小说的爽文套路。")
        return {"plot_suggestions": plot_result}