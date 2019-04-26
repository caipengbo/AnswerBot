# -*- UTF-8 -*-
from elasticsearch import Elasticsearch


# I use ES to shrink the query space

def search(title="", body="", size=1000):
    # replace your url
    url = "http://10.1.1.9:9266"
    es = Elasticsearch([url])
    doc = {
        "query": {
            "bool": {
                "should": [
                    {"match": {"Title": title}},
                    {"match": {"Body": body}}
                ]
            }
        }
    }
    results = es.search(index="java", doc_type="posts", body=doc, size=size)
    return_list = []
    for res in results['hits']['hits']:
        return_list.append(res['_source'])

    return return_list
