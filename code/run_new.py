import pandas as pd

# 读取原始数据
df = pd.read_csv("data/xhs_data.csv")

# 判断逻辑：标题含攻略/路线/Citywalk=爆款
def judge_hot(row):
    title = str(row["标题"])
    keywords = ["攻略", "路线", "Citywalk"]
    for word in keywords:
        if word in title:
            return "爆款笔记"
    return "普通笔记"

# 新增分类列
df["笔记类型"] = df.apply(judge_hot, axis=1)

# 输出新csv
df.to_csv("data/labeled_xhs.csv", index=False, encoding="utf-8-sig")
print("数据分类完成！无报错")