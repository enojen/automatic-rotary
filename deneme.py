from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections

es = connections.create_connection(hosts=['localhost'], timeout=20)
# conntect es
#es = Elasticsearch([{'host': config.elastic_host, 'port': config.elastic_port}])
# delete index if exists

# index settings
settings = {
    "settings": {
    "analysis": {
      "analyzer": {
        "standard_lowercase_example": {
          "type": "custom",
          "tokenizer": "whitespace",
          "filter": ["lowercase"]
        },
        "turkish_lowercase_example": {
          "type": "custom",
          "tokenizer": "whitespace",
          "filter": ["turkish_lowercase"]
        }
      },
      "filter": {
        "turkish_lowercase": {
          "type": "lowercase",
          "language": "turkish"
        }
      }
    }
  },
  "mappings": {
        "_doc": {
            "properties": {
                "title": {
                    "type": "text",
                    "analyzer": "standard_lowercase_example"
                },
                "query": {
                    "type": "percolator"
                }
            }
        }
    }
}
# create index
es.indices.create(index='my-index', ignore=400, body=settings)