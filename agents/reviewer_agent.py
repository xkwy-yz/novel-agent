from typing import Dict, Any
from agents.base import BaseAgent


class ReviewerAgent(BaseAgent):
    def __init__(self, config: Dict[str, Any]):
        super().__init__("NovelReviewer", config)

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        draft = input_data.get("draft", "")
        print("  [Reviewer] 🧐 正在以老书虫视角审核草稿（找毒点）...")

        prompt = f"""请作为最挑剔的网文读者，审核以下草稿：
草稿内容：
{draft}

请严格指出：
1. 有没有“主角圣母”、“降智”的情节？
2. 节奏是否拖沓？
3. 给出 0-10 的评分。

请直接给出你的审核意见，不用客套。"""

        review_result = self.chat(prompt, system_prompt="你是一个看过上万本网文的毒舌老书虫。")
        return {"review_report": review_result}