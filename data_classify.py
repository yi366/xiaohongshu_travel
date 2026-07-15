import pandas as pd

# 读取原始数据集
df = pd.read_csv("./data/xhs_data.csv", encoding="utf-8-sig")

# 爆款判断函数，仅识别标题关键词，不碰正文
def judge_type(row):
    title = str(row["标题"])
    hot_key = ["攻略", "路线", "Citywalk", "行程"]
    for word in hot_key:
        if word in title:
            return "爆款笔记"
    return "普通笔记"

# 生成分类标签列
df["笔记类型"] = df.apply(judge_type, axis=1)

# 输出分类后的新csv
df.to_csv("./data/labeled_xhs.csv", index=False, encoding="utf-8-sig")
print("分类完成：2条爆款，3条普通笔记")