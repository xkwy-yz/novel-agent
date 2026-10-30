# 模拟一个本地设定库（在真实项目中，这里会连接 ChromaDB 向量数据库）
NOVEL_SETTINGS = {
    "主角设定": "陈星，21岁，开局满级，异能是【无限吞噬】。性格沉稳、杀伐果断、绝不吃亏。口头禅：'地球有危险？无所谓我会出手'。",
    "世界观": "蓝星觉醒，存在隐秘官方组织【龙盾】，地球之外有异空间深渊和宇宙虫族。",
    "目前进度": "陈星正在自己的出租屋里吃泡面。"
}

def search_setting(keyword: str) -> str:
    """根据关键词检索小说设定"""
    print(f"  [工具调用] 📖 正在翻阅设定集，检索关键词: {keyword}")
    results = []
    for key, value in NOVEL_SETTINGS.items():
        if keyword in key or keyword in value:
            results.append(f"【{key}】: {value}")
    return "\n".join(results) if results else "未找到相关设定。"