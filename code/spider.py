import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd

# 请求头，模拟浏览器访问
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.xiaohongshu.com/"
}

def get_xhs_note(url):
    """爬取单条小红书笔记信息"""
    # 随机延时1~3秒，防反爬
    time.sleep(random.uniform(1, 3))
    resp = requests.get(url, headers=HEADERS, timeout=15)
    if resp.status_code != 200:
        print("访问失败，状态码：", resp.status_code)
        return None

    soup = BeautifulSoup(resp.text, "lxml")
    data = {}

    # 标题
    title_tag = soup.find("title")
    data["标题"] = title_tag.get_text(strip=True) if title_tag else "无标题"

    # 正文内容
    desc_meta = soup.find("meta", attrs={"name": "description"})
    data["正文"] = desc_meta["content"] if desc_meta else "无内容"

    # 点赞、收藏（简易提取）
    html_text = resp.text
    import re
    like_res = re.search(r'"likedCount":(\d+)', html_text)
    collect_res = re.search(r'"collectedCount":(\d+)', html_text)
    data["点赞数"] = like_res.group(1) if like_res else "0"
    data["收藏数"] = collect_res.group(1) if collect_res else "0"
    data["链接"] = url
    return data

if __name__ == "__main__":
    # 粘贴多条文旅笔记链接，每条单独一行
    url_list = [
        "https://www.xiaohongshu.com/explore/69ccad090000000023020f5b?xsec_token=AB3bex3LvrKxvmp3twBJswJHKESRY2g4oym9SFzrwCY6A=&xsec_source=pc_search&source=web_explore_feed",
        "https://www.xiaohongshu.com/explore/6a0efbb90000000006034efa?xsec_token=ABw-XPm0Xr4U4c8qhM07qMr4sFAfXw8aKnKkd8fwb3dgs=&xsec_source=pc_search&source=web_explore_feed",
        "https://www.xiaohongshu.com/explore/6a0edada000000003601b79b?xsec_token=ABw-XPm0Xr4U4c8qhM07qMrzhS2F87LzfcCzs7Sapkit8=&xsec_source=pc_search&source=web_explore_feed",
        "https://www.xiaohongshu.com/explore/6a0598610000000037037220?xsec_token=ABLh8VhLsswcEWgwEQB_EMgPznlqT5V2Ad1QKDwW_i4Gs=&xsec_source=pc_search&source=web_explore_feed",
        "https://www.xiaohongshu.com/explore/68ea1c8f0000000003039274?xsec_token=AB7kYDUdIFmJJ_F3J__DrImo6cht0LlCxCP6MLPgKuz70=&xsec_source=pc_search&source=web_profile_page"
    ]
    all_data = []
    for url in url_list:
        result = get_xhs_note(url)
        if result:
            all_data.append(result)
            print(f"成功爬取：{result['标题']}")
    # 全部数据一次性写入csv
    df = pd.DataFrame(all_data)
    df.to_csv("./data/xhs_data.csv", mode="w", index=False, encoding="utf-8-sig")
    print("所有文旅笔记数据已保存到 data/xhs_data.csv")

        # 保存到data文件夹csv文件
    df = pd.DataFrame([result])
    df.to_csv("./data/xhs_data.csv", mode="a", index=False, encoding="utf-8-sig")
    print("数据已保存至 data/xhs_data.csv")