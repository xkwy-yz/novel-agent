from abc import ABC, abstractmethod
from typing import Dict, Any
from openai import OpenAI

class BaseAgent(ABC):
    def __init__(self, name: str, config: Dict[str, Any]):
        self.name = name
        self.config = config
        self.client = OpenAI(
            api_key=config.get("api_key"),
            base_url=config.get("base_url")
        )
        self.model = config.get("model", "deepseek-chat")

    def chat(self, prompt: str, system_prompt: str = "你是一个专业的网文大神") -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8  # 写小说温度稍微高一点，更有创造力
        )
        return response.choices[0].message.content

    @abstractmethod
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        pass