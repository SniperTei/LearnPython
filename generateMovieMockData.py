# from faker import Faker
import random
from datetime import datetime

# 创建一个 Faker 实例
# faker = Faker("zh_CN")

# 生成模拟电影数据的函数
def generate_movie_data():
    movies = []
    for i in range(1, 11):
        movie = {
            "id": i,
            "title": "fakename",  # 随机生成一个单词作为标题
            "genre": "动作",
            "rating": round(random.uniform(7.0, 9.5), 1),  # 随机生成一个评分
            "actors": "fakeactor",  # 随机生成一个姓名作为演员
            "release_date": "2010-01-02",  # 随机生成一个发布日期
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "updated_at": datetime.now().strftime("%Y-%m-%d"),
            "created_by": "zhengnan",
            "updated_by": "zhengnan"
        }
        movies.append(movie)
    return movies

# def showMockData():
#     {"title": "复仇者联盟", "genre": "动作,科幻", "rating": 7.8, "actors": "埃文斯", "release_date": "2010-01-02", "created_at": "2024-05-21", "updated_at": "2024-05-21", "created_by": "zhengnan", "updated_by": "zhengnan"}
#     {"title": "钢铁侠", "genre": "动作,科幻", "rating": 9.2, "actors": "罗伯特唐尼", "release_date": "2010-01-02", "created_at": "2024-05-21", "updated_at": "2024-05-21", "created_by": "zhengnan", "updated_by": "zhengnan"}
#     {"title": "蝴蝶效应", "genre": "惊悚", "rating": 7.9, "actors": "无名", "release_date": "2010-01-02", "created_at": "2024-05-21", "updated_at": "2024-05-21", "created_by": "zhengnan", "updated_by": "zhengnan"}
#     {"title": "海贼王", "genre": "动画", "rating": 8.5, "actors": "路飞", "release_date": "2010-01-02", "created_at": "2024-05-21", "updated_at": "2024-05-21", "created_by": "zhengnan", "updated_by": "zhengnan"}
#     {"title": "色即是空", "genre": "喜剧", "rating": 8.4, "actors": "任昌丁", "release_date": "2010-01-02", "created_at": "2024-05-21", "updated_at": "2024-05-21", "created_by": "zhengnan", "updated_by": "zhengnan"}
#     {"title": "玩命速递", "genre": "动作", "rating": 8.0, "actors": "杰森斯坦森", "release_date": "2010-01-02", "created_at": "2024-05-21", "updated_at": "2024-05-21", "created_by": "zhengnan", "updated_by": "zhengnan"}
#     {"title": "惊声尖笑", "genre": "搞笑,恐怖", "rating": 9.5, "actors": "不知道", "release_date": "2010-01-02", "created_at": "2024-05-21", "updated_at": "2024-05-21", "created_by": "zhengnan", "updated_by": "zhengnan"}
#     {"title": "怒火攻心", "genre": "动作", "rating": 9.2, "actors": "杰森斯坦森", "release_date": "2010-01-02", "created_at": "2024-05-21", "updated_at": "2024-05-21", "created_by": "zhengnan", "updated_by": "zhengnan"}
#     {"title": "唐人街探案", "genre": "悬疑", "rating": 8.0, "actors": "王宝强", "release_date": "2010-01-02", "created_at": "2024-05-21", "updated_at": "2024-05-21", "created_by": "zhengnan", "updated_by": "zhengnan"}
#     {"title": "惊奇队长", "genre": "动作", "rating": 7.7, "actors": "不认识", "release_date": "2010-01-02", "created_at": "2024-05-21", "updated_at": "2024-05-21", "created_by": "zhengnan", "updated_by": "zhengnan"}

# 生成模拟电影数据
movies_data = generate_movie_data()

# 打印生成的模拟电影数据
for movie in movies_data:
    print(movie)
