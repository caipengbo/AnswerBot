import unittest

class Test():
    def __init__(self, score):
        self.score = score

    def __gt__(self, other):
        return self.score > other.score

    def __repr__(self):
        return "score:"+str(self.score)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_cal_semantic_pattern(self):
        pattern = ['please check', 'pls check', 'you should',
                   'you can try', 'you could try', 'check out',
                   'in short', 'the most important', 'i\'d recommend',
                   'in summary', 'keep in mind', 'i suggest']

        raw = "pls check, what you like , and wfk, You could try, i\'d recommend and the most important and The most important"

        lowcase = raw.lower()

        for p in pattern:
            if lowcase.find(p) != -1:
                print(p)

    def test_sort(self):
        ls = [Test(2), Test(90), Test(11), Test(21)]
        print(ls)
        ls.sort(reverse=True)
        print(ls)

    def test_cal_mmr(self, n=10):
        for i in range(n):
            for j in range(i + 1, n):
                # sym_relevance = relevance.calculate_symmetric(model, top_n_paragraph_word_list[i], top_n_paragraph_word_list[j], idf_metric_dict)
                print(str(i) + ', ' + str(j))


if __name__ == '__main__':
    unittest.main()
