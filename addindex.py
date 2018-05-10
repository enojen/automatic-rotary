import json

from elasticsearch_dsl import (
    connections,
    DocType,
    Mapping,
    Percolator,
    Text,
    analyzer
)
from elasticsearch_dsl.query import (
    SpanNear,
    SpanTerm
)
from elasticsearch import Elasticsearch

# Read the json File
json_data = open('titles.json').read()
data = json.loads(json_data)

docs = data['response']['docs']

analizer = analyzer('standard_lowercase',
                tokenizer="whitespace", filter=["lowercase"])

# creating a new default elasticsearch connection
es = connections.create_connection(hosts=['localhost'], timeout=20)


class Document(DocType):
    title = Text(analyzer=analizer)
    query = Percolator()
    doc_id = Text()

    class Meta:
        index = 'my-index'
        doc_type = '_doc'

    def save(self, **kwargs):
        return super(Document, self).save(**kwargs)


# create the mappings in elasticsearch
Document.init()

# index the query
for doc in docs:
    terms = doc['title'].split(" ")
    get_id = doc['id']
    clauses = []
    for term in terms:
        term = term.replace("İ", "i").replace(
            ",", "").replace("î", "i").replace("I", "ı")
        term = term.lower()
        field = SpanTerm(title=term)
        clauses.append(field)
    query = SpanNear(clauses=clauses, slop=0, in_order=True)
    item = Document(query=query, doc_id=get_id)
    item.save()
