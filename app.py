# app.py
import streamlit as st
from config import NovelConfig
from agents.plot_agent import PlotAgent
from agents.reviewer_agent import ReviewerAgent

# 设置网页标题
st.set_page_config(page_title="AI 网文辅助助手", page_icon="📝")
st.title("📝 AI 网文辅助创作系统")

# 侧边栏
with st.sidebar:
    st.header("关于系统")
    st.write("基于多智能体（Multi-Agent）架构的辅助写作工具。")
    st.write("包含：剧情推演 Agent、毒点审核 Agent。")

# 实例化配置
config = NovelConfig()
llm_config = config.llm.model_dump()
plot_agent = PlotAgent(llm_config)
reviewer = ReviewerAgent(llm_config)

# 输入区
st.subheader("1. 输入当前剧情节点")
topic = st.text_area("请描述你卡文的地方，或者当前的主角处境：",
                     value="陈星在吃泡面时，遇到A级异界巨兽破墙而入，砸坏了他的电视。")

if st.button("🚀 让 AI 推演剧情"):
    if topic:
        with st.spinner("AI 大神正在思考..."):
            output = plot_agent.run({"topic": topic})
            st.success("推演完成！")
            st.markdown(output["plot_suggestions"])
    else:
        st.warning("请先输入剧情节点！")

# 草稿审核区
st.divider()
st.subheader("2. 草稿毒点审核")
draft = st.text_area("把你写好的草稿贴在这里：",
                     value="陈星看着被砸坏的电视，心里十分难过。那只巨兽冲他咆哮，陈星却叹了口气，说：“你走吧，你也是有生命的，我不想杀你。”于是，陈星把泡面让给了巨兽吃。")

if st.button("🧐 开始审核"):
    if draft:
        with st.spinner("老书虫正在审稿..."):
            review_output = reviewer.run({"draft": draft})
            st.error("审核报告生成完毕（红字警告）")
            st.write(review_output["review_report"])
    else:
        st.warning("请先输入草稿！")