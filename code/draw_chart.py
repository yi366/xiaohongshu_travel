import pandas as pd
import matplotlib.pyplot as plt
import os
from collections import Counter
import re

df = pd.read_csv("data/labeled_xhs.csv")
plt.rcParams["font.family"] = ["SimHei", "Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# 创建figures文件夹
if not os.path.exists("figures"):
    os.mkdir("figures")

# ========== 图1：柱状图 笔记数量对比 ==========
type_count = df["笔记类型"].value_counts()
plt.figure(figsize=(7,4))
bars = plt.bar(type_count.index, type_count.values, color=["#ff8888","#66aaff"])
for bar in bars:
    num = bar.get_height()
    plt.text(bar.get_x()+bar.get_width()/2, num+1, f"{num}", ha="center")
plt.title("爆款与普通文旅笔记数量对比")
plt.xlabel("笔记类型")
plt.ylabel("笔记条数")
plt.savefig("figures/bar_like.png", dpi=300, bbox_inches="tight")
plt.close()

# ========== 图2：饼图 占比分布 ==========
plt.figure(figsize=(5,5))
plt.pie(type_count.values, labels=type_count.index, autopct="%1.1f%%", colors=["#ff8888","#66aaff"])
plt.title("笔记类型占比饼图")
plt.savefig("figures/pie_emotion.png", dpi=300, bbox_inches="tight")
plt.close()

# ========== 图3：散点图（互动量关联，若无点赞收藏可忽略报错） ==========
try:
    plt.figure(figsize=(6,4))
    plt.scatter(df.index, df.iloc[:,1], alpha=0.6)
    plt.title("笔记互动量分布散点图")
    plt.xlabel("笔记序号")
    plt.ylabel("互动数据")
    plt.savefig("figures/scatter_corr.png", dpi=300, bbox_inches="tight")
except:
    print("无互动字段，跳过散点图")
plt.close()

# ========== 图4：词频简易统计图 ==========
all_text = "".join(df["标题"].astype(str))
words = re.findall(r'[\u4e00-\u9fa5a-zA-Z]+', all_text)
word_cnt = Counter(words).most_common(8)
words_list = [i[0] for i in word_cnt]
count_list = [i[1] for i in word_cnt]
plt.figure(figsize=(8,4))
plt.bar(words_list, count_list, color="#77ddaa")
plt.title("标题高频词汇统计")
plt.xticks(rotation=30)
plt.savefig("figures/word_frequency.png", dpi=300, bbox_inches="tight")
plt.close()

print("四张图表全部生成完毕，查看figures文件夹！")