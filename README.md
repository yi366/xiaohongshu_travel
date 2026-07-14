# xiaohongshu_travel 小红书文旅爬虫项目

## 📌 项目简介
本项目为课程作业，旨在通过 Python 爬虫批量抓取小红书平台“文旅类”笔记数据，输出结构化 CSV 数据集，用于后续数据分析与可视化。项目聚焦“爆款笔记”识别与用户互动行为分析。

## 👥 小组成员及分工
- **成员 A**：Git 仓库管理 + Python 爬虫开发（数据采集层）
- **成员 B**：数据清洗、统计分析、Matplotlib 可视化（应用处理层）
- **成员 C**：Quarto 期末完整学术报告主笔（期末 60% 分值核心）
- **成员 D**：项目配套文档归档 + 报告补充完善 + 仓库文档编写（本角色）

## 🛠️ 环境部署步骤
1. 克隆仓库：`git clone https://github.com/yi366/xiaohongshu_travel.git`
2. 安装依赖：`pip install -r requirements.txt`
3. 运行爬虫：`python scripts/spider.py`
4. 运行分析：`python scripts/analysis.py`

## 📁 项目目录结构

## 📊 数据分类规则
本项目无无效数据，收集互动数据，因此通过标题关键词区分爆款/普通笔记：
包含【攻略、路线、Citywalk、行程】标记为爆款笔记，其余为普通笔记。

## 🚀 项目开发流程
全部开发过程截图存放于 `/screenshot` 目录，包含：
1. 项目本地分支列表截图
2. 完整Git提交开发日志截图
3. 团队成员正常远程协作截图
4. 原始数据集 raw.csv 文件截图

## 📄 交付物清单
- [x] 爬虫代码 (spider.py)
- [x] 数据分析代码 (analysis.py)
- [x] 原始数据 (raw.csv)
- [x] 清洗数据 (clean.csv)
- [x] 可视化图表 (figures/)
- [x] 完整文档 (docs/)
- [x] Git提交记录截图
- [x] 小组分工表
- [x] 项目交付物清单
