# -*- UTF-8 -*-
from formula import relevance
from preprocessor.preprocessing import PreprocessPostContent


class Paragraph():
    def __init__(self, raw_text, word_list, vote_score, position):
        self.raw_text = raw_text # 带标签的，只经过<p>分段的数据
        self.word_list = word_list
        self.position = position # 第几段
        self.vote_score = vote_score
        self.relevance_score = 0
        self.entity_score = 0
        self.infor_entropy = 0
        self.semantic_pattern = 0
        self.format_pattern = 0
        self.pos_score = 0
        self.overall_score = 0

    def cal_relevance(self, model, query_word_list, idf_metric_dict):
        self.relevance_score = relevance.calculate_symmetric(model, query_word_list, self.word_list, idf_metric_dict)

    def cal_entropy(self, idf_metric_dict):
        idf_list = []
        for word in self.word_list:
            try:
                idf = idf_metric_dict[word]
            except:
                idf = 0

            idf_list.append(idf)

        self.infor_entropy = sum(idf_list)

    def cal_semantic_pattern(self):
        pattern = ['please check', 'pls check', 'you should',
                   'you can try', 'you could try', 'check out',
                   'in short', 'the most important', 'i\'d recommend',
                   'in summary', 'keep in mind', 'i suggest']

        lower_plain_text = self.raw_text.lower()

        for p in pattern:
            if lower_plain_text.find(p) != -1:
                self.semantic_pattern = 1
                break

    def cal_format_pattern(self):
        pattern = ['<strong>', '<strike>']

        lower_plain_text = self.raw_text.lower()

        for p in pattern:
            if lower_plain_text.find(p) != -1:
                self.format_pattern = 1
                break

    def cal_pos_score(self):
        if self.position >= 1 and self.position <= 3:
            self.pos_score = 1 / self.position
        else:
            self.pos_score = 0

    def normalized(self, relevance_min, relevance_max, entropy_min, entropy_max, vote_min, vote_max):
        self.relevance_score = (self.relevance_score - relevance_min) / (relevance_max - relevance_min)
        self.infor_entropy = (self.infor_entropy - entropy_min) / (entropy_max - entropy_min)
        self.vote_score = (self.vote_score - vote_min) / (vote_max - vote_min)

    def cal_overall_score(self):
        self.overall_score += self.vote_score
        self.overall_score += self.relevance_score
        self.overall_score += self.entity_score
        self.overall_score += self.infor_entropy
        self.overall_score += self.semantic_pattern
        self.overall_score += self.format_pattern
        self.overall_score += self.pos_score

    def __gt__(self, other):
        return self.overall_score > other.overall_score