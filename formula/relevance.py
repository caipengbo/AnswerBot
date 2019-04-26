# -*- UTF-8 -*-

# formula (1) in III.A  rel(q->Q)
def calculate_asymmetric(model, q_word_list, Q_word_list, idf_metric_dict):
    rel_idf_list = [0]
    idf_list = [0]
    for q_word in q_word_list:
        rel_list = [0]
        for Q_word in Q_word_list:
            try:
                val = model.wv.similarity(q_word, Q_word)
            except:
                val = 0
            rel_list.append(val)

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


# rel(q, Q)
def calculate_symmetric(model, q_word_list, Q_word_list, idf_metric_dict):
    rel_q2Q = calculate_asymmetric(model, q_word_list, Q_word_list, idf_metric_dict)
    rel_Q2q = calculate_asymmetric(model, Q_word_list, q_word_list, idf_metric_dict)
    return (rel_q2Q + rel_Q2q) / 2
