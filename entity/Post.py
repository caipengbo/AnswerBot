# -*- UTF-8 -*-

from formula import relevance


class Post():

    def __init__(self, title_word_list, answer_list):
        self.title_word_list = title_word_list
        self.answer_list = answer_list
        self.score = 0

    def calculate_score(self, model, query_list, idf_metric_dict):
        self.score = relevance.calculate_symmetric(model, query_list, self.title_word_list, idf_metric_dict)

    def __lt__(self, other):
        return self.score < other.score
