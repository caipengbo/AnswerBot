# -*- UTF-8 -*-
from multiprocessing import Pool

import pymongo

from preprocessor.preprocessing import PreprocessPostContent


def process(post_bulk):
    wordlist_list = []
    for post in post_bulk:
        wordlist_list.append(PreprocessPostContent().get_single_para_word_list(post['Title']))
        wordlist_list.extend(PreprocessPostContent().get_mul_para_wordlist_list(post['Body']))

    return wordlist_list


def parallel_process(posts):
    bulk = []
    block_list = []
    count = 0
    pool = Pool(50)
    for post in posts:
        bulk.append(post)
        count += 1
        if not count % 2:
            block_list.append(bulk)
            bulk = []
        if count == 4:
            break

    block_list.append(bulk)
    return_list = pool.map(process, block_list)
    pool.close()
    pool.join()
    return return_list
