import json

from elasticsearch_dsl import (
    connections,
    DocType,
    Mapping,
    Percolator,
    Text
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

# creating a new default elasticsearch connection
connections.configure(
    default={'hosts': 'localhost:9200'},
)


class Document(DocType):
    title = Text()
   
    query = Percolator()

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
   
    clauses = []
    for abcd in terms:
        term = abcd.lower()
        print(term)
        field = SpanTerm(title=term)
        clauses.append(field)
    query = SpanNear(clauses=clauses)
    item = Document(query=query)
    item.save()