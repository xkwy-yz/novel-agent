import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class LLMConfig(BaseModel):
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    base_url: str = os.getenv("OPENAI_BASE_URL", "https://api.deepseek.com/v1")
    model: str = "deepseek-chat"

class NovelConfig(BaseModel):
    llm: LLMConfig = LLMConfig()