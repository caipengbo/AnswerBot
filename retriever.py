# -*- UTF-8 -*-

class Post():

    def __init__(self, title_word_list, answer_list):
        self.title_word_list = title_word_list
        self.answer_list = answer_list
        self.score = 0

    def formula(self, model, q_word_list, Q_word_list, idf_metric_dict):
        rel_idf_list = []
        idf_list = []
        for q_word in q_word_list:
            rel_list = []
            for Q_word in Q_word_list:
                try:
                    val = model.similarity(q_word, Q_word)
                except:
                    val = 0
                rel_list.append(val)

            idf = 0
            try:
                idf = idf_metric_dict[q_word]
            except:
                idf = 0

            rel_idf_list.append(max(rel_list) * idf)
            idf_list.append(idf)

        sum_idf = sum(idf_list)
        if not sum_idf:
            rel_q2Q = 0
        else:
            rel_q2Q = sum(rel_idf_list) / sum_idf

        return rel_q2Q

    def calculate_score(self, model, query_list, idf_metric_dict):
        rel_q2Q = self.formula(model, query_list, self.title_word_list, idf_metric_dict)
        rel_Q2q = self.formula(model, self.title_word_list, query_list, idf_metric_dict)
        self.score = (rel_q2Q + rel_Q2q) / 2