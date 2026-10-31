# tools/setting_tool.py
import chromadb
from chromadb.utils import embedding_functions

# 初始化本地向量数据库（数据会存在当前目录的 chroma_db 文件夹）
client = chromadb.PersistentClient(path="./chroma_db")

# 使用默认的嵌入模型（将文本转换为向量）
default_ef = embedding_functions.DefaultEmbeddingFunction()

# 获取或创建集合
collection = client.get_or_create_collection(name="novel_settings", embedding_function=default_ef)

# 首次运行，往里面塞点设定数据
if collection.count() == 0:
    print("  [系统] 正在初始化小说设定向量库...")
    collection.add(
        documents=[
            "陈星，21岁，开局满级，异能【无限吞噬】，杀伐果断，口头禅：地球有危险？无所谓我会出手。",
            "官方隐秘组织名为龙盾，负责抵御异界入侵，但高层腐败，防线摇摇欲坠。",
            "目前地球处于末日前夕，异界深渊随时可能降临，城市中会随机出现异界裂缝。"
        ],
        metadatas=[
            {"type": "character", "name": "陈星"},
            {"type": "faction", "name": "龙盾"},
            {"type": "world", "name": "地球现状"}
        ],
        ids=["id1", "id2", "id3"]
    )

def search_setting(query: str) -> str:
    """通过向量检索寻找设定"""
    print(f"  [工具调用] 📖 正在使用 RAG 向量检索设定: {query}")
    results = collection.query(
        query_texts=[query],
        n_results=2 # 返回最相似的2条
    )
    # 将结果拼接成字符串返回
    if results['documents'] and results['documents'][0]:
        return "\n".join(results['documents'][0])
    return "未找到相关设定。"