# 导入所需工具库
import pandas as pd
import matplotlib.pyplot as plt
import jieba
from collections import Counter

# ====================== 1.读取原始爬虫数据 ======================
# 适配中文表头
df = pd.read_csv("data/raw.csv", encoding="utf-8")
print("✅ 原始数据读取成功，总条数：", len(df))

# ====================== 2.数据清洗处理 ======================
# 改用csv真实中文列名：正文、点赞数、收藏数
df = df.drop_duplicates()
df = df.dropna(subset=["正文","点赞数","收藏数"])

# 3）新增分析需要的字段
# 转换点赞、收藏为数字，解决字符串无法比较报错
df["点赞数"] = pd.to_numeric(df["点赞数"], errors="coerce").fillna(0)
df["收藏数"] = pd.to_numeric(df["收藏数"], errors="coerce").fillna(0)

df["总互动量"] = df["点赞数"] + df["收藏数"]
# 互动超1000判定为爆款笔记
df["是否爆款"] = df["总互动量"].apply(lambda x:1 if x>0 else 0)
# 4）文本分词，过滤无意义虚词
stop_words = {"的","了","是","我","很","也","就","都","还","有","去","在","和","不"}
def clean_text(text):
    words = jieba.lcut(str(text))
    valid_words = [w for w in words if w not in stop_words and len(w) > 1]
    return " ".join(valid_words)
df["清洗正文"] = df["正文"].apply(clean_text)

# 5）简易情感打分，统计正向旅游词汇
positive_word_list = {"推荐","好看","绝美","好玩","值得","舒服","宝藏","治愈"}
def get_sentiment_score(text):
    word_arr = text.split()
    score = sum(1 for word in word_arr if word in positive_word_list)
    return score
df["情感分数"] = df["清洗正文"].apply(get_sentiment_score)

# 导出清洗完毕的数据
df.to_csv("data/clean.csv", index=False, encoding="utf-8-sig")
print("✅ 数据清洗完成，已生成 data/clean.csv")

# ====================== 3.统计指标计算 ======================
# 1）爆款与普通笔记互动均值对比
group_result = df.groupby("是否爆款")[["点赞数","收藏数","总互动量"]].mean()
print("\n📊 1.爆款与普通笔记互动均值：")
print(group_result)

# 2）点赞、收藏相关性
corr_result = df[["点赞数","收藏数"]].corr()
print("\n📊 2.点赞&收藏相关性矩阵：")
print(corr_result)

# 3）全文本高频关键词TOP20
all_words = []
for text in df["清洗正文"]:
    all_words.extend(text.split())
word_top20 = Counter(all_words).most_common(20)
print("\n📊 3.笔记高频关键词TOP20：")
print(word_top20)

# 4）情感分布统计
high_sentiment = len(df[df["情感分数"] >= 3])
low_sentiment = len(df[df["情感分数"] < 3])
avg_sentiment = df["情感分数"].mean()
print(f"\n📊 4.平均情感得分：{avg_sentiment}")
print(f"高正向情感笔记：{high_sentiment}条，普通情感：{low_sentiment}条")

# ====================== 4.绘制四张分析图表 ======================
# 解决中文乱码
plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 图表1：爆款/普通笔记点赞对比柱状图
plt.figure(figsize=(7,4))
bar_data = df.groupby("是否爆款")["点赞数"].mean()
plt.bar(["普通笔记","爆款笔记"], bar_data.values, color=["#cccccc","#ff784f"])
plt.title("爆款与普通笔记平均点赞数量对比")
plt.ylabel("平均点赞数")
plt.savefig("figures/bar_like.png", dpi=300)
plt.close()

# 图表2：点赞收藏散点图
plt.figure(figsize=(7,4))
plt.scatter(df["点赞数"], df["收藏数"], alpha=0.4)
plt.title("笔记点赞与收藏数量分布关系")
plt.xlabel("点赞数")
plt.ylabel("收藏数")
plt.savefig("figures/scatter_corr.png", dpi=300)
plt.close()

# 图表3：高频关键词横向柱状图
top10_words = dict(word_top20[:10])
plt.figure(figsize=(9,4))
plt.barh(list(top10_words.keys()), list(top10_words.values()))
plt.title("小红书文旅笔记前10高频关键词")
plt.savefig("figures/word_frequency.png", dpi=300)
plt.close()

# 图表4：情感分布饼图
plt.figure(figsize=(5,5))
plt.pie([high_sentiment, low_sentiment], labels=["高正向情感","中性/低情感"], autopct="%1.1f%%")
plt.title("用户笔记情感整体分布")
plt.savefig("figures/pie_emotion.png", dpi=300)
plt.close()

print("\n✅ 全部图表生成完毕，图片保存在 figures 文件夹")