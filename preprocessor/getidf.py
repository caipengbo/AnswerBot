# -*- UTF-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer

def cal_idf(para_list):
    vectorizer = TfidfVectorizer(
        use_idf=True,  # utiliza o idf como peso, fazendo tf*idf
        norm=None,  # normaliza os vetores
        smooth_idf=False,  # soma 1 ao N e ao ni => idf = ln(N+1 / ni+1)
        sublinear_tf=False,  # tf = 1+ln(tf)
        binary=False,
        min_df=1, max_df=1.0, max_features=None,
        ngram_range=(1, 1), preprocessor=None,
        stop_words=None,
        tokenizer=None,
        vocabulary=None
    )
    X = vectorizer.fit_transform(para_list)
    idf = vectorizer.idf_
    idf_dict = dict(zip(vectorizer.get_feature_names(), idf))
    return idf_dict