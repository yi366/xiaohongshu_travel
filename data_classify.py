import pandas as pd

df = pd.read_csv("data/xhs-data.csv")

# 根据标签数量划分爆款/普通笔记
def judge_hot(row):
    tag_list = eval(row["tags"])
    if len(tag_list) >= 3:
        return "爆款笔记"
    else:
        return "普通笔记"

df["笔记类型"] = df.apply(judge_hot, axis=1)

# 导出带分类标签的新数据集
df.to_csv("data/labeled_xhs.csv", index=False, encoding="utf-8-sig")
print("数据集分类完成，已生成 labeled_xhs.csv")