# -*- UTF-8 -*-

# 辅助类，
from formula import relevance


class element():
    def __init__(self, val, pos_i, pos_j):
        self.val = 0
        self.pos_i = pos_i
        self.pos_j =pos_j


def cal_mmr(n, top_n_paragraph_word_list, model, idf_metric_dict):
    for i in range(n):
        for j in range(i+1, n):
            sym_relevance = relevance.calculate_symmetric(model, top_n_paragraph_word_list[i], top_n_paragraph_word_list[j], idf_metric_dict)



    # print(mmr_matrix)


if __name__ == '__main__':
    cal_mmr(4, [])