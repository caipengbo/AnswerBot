# -*- UTF-8 -*-

# 辅助类，
from formula import relevance


class Element():
    def __init__(self, val, pos_i, pos_j):
        self.val = 0
        self.pos_i = pos_i
        self.pos_j = pos_j

    def __gt__(self, other):
        return self.val > other.val


def cal_mmr(n, top_n_paragraph_word_list, model, idf_metric_dict):
    element_obj_list = []
    for i in range(n):
        for j in range(i + 1, n):
            sym_relevance = relevance.calculate_symmetric(model, top_n_paragraph_word_list[i].word_list,
                                                          top_n_paragraph_word_list[j].word_list, idf_metric_dict)
            element_obj_list.append(Element(sym_relevance, i, j))

    return element_obj_list


def get_top_k_position(k, element_obj_list):
    mmr_return_set = set()
    for i in range(len(element_obj_list)):
        mmr_return_set.add(element_obj_list[i].pos_i)
        mmr_return_set.add(element_obj_list[i].pos_j)
        if len(mmr_return_set) >= k:
            break

    return mmr_return_set
