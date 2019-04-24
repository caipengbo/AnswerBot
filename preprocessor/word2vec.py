# -*- UTF-8 -*-
from multiprocessing import Pool

import pymongo

from preprocessor.preprocessing import PreprocessPostContent


def getItefromMongoDB():
    client = pymongo.MongoClient(host='10.1.1.9', port=50000)
    javaposts_db = client.javaposts
    posts_collection = javaposts_db.posts
    posts = posts_collection.find()
    return posts

# 将 Body和 Title 变成paragraph 列表放入word2vec
def process(post_bulk):
    para_list = []
    for post in post_bulk:
        para_list.extend(PreprocessPostContent().getPlainTxt(post['Title']))
        para_list.extend(PreprocessPostContent().getPlainTxt(post['Body']))

    return para_list

# 并行处理
def parallel_process(posts):
    bulk = []
    block_list = []
    count = 0
    pool = Pool(50)
    for post in posts:
        bulk.append(post)
        count += 1
        if not count % 1000:
            block_list.append(bulk)
            bulk = []

    block_list.append(bulk)
    # 返回每个并行函数的结果列表
    return_list = pool.map(process, block_list)

    pool.close()
    pool.join()

    para_list = []
    for ls in return_list:
        para_list.extend(ls)

    return para_list


if __name__ == '__main__':
    posts = getItefromMongoDB()
    print(posts.count())


    return_list = parallel_process(posts)
    para_list = []

    for ls in return_list:
        para_list.extend(ls)
