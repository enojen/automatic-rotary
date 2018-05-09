from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup

client = Elasticsearch()


#abc = "Anasayfa, seçkin maddelerden birinin giriş bölümünün sergilendiği bir bölüme sahiptir. Bu bölümde, okuyuculara Vikipedi'nin ürettiği en başarılı içerik örnekleri sergilenmektedir. Bu ayın anasayfaya çıkan seçkin madde listesi buradan görülebilir. Maddenin anasayfaya çıkabilmesi için seçkin madde statüsünde olması gerekmektedir (herhangi bir maddeyi aday göstermek için bkz: Vikipedi:Seçkin madde adayları). Seçkin madde statüsü alan maddeler, seçilme sıralarına göre kronolojik olarak anasayfaya çıkarlar. Seçkin içerik sorumluları, anasayfaya çıkacak olan maddelerin düzeninden ve sistemin sağlıklı işleyişinden sorumludur. Konuyla ilgili bilgi almak veya herhangi bir sorun bildirmek için lütfen sorumluların sayfasına mesaj bırakın maddelerden."
userdoc = input('Please enter your document: ')
response = client.search(
    index="my-index",
    body={
      "query" : {
        "percolate" : {
            "field": "query",
            "document" : {
                "message" : userdoc
            }
        }
    },
    "highlight": {
      "pre_tags" : ["<a href='hyperlinkvariable'>"],
      "post_tags" : ["</a>"],
      "fields": {
        "message": {
          "number_of_fragments" : 3,
          "fragment_size" : 1500
          
        }
      }
    }
    }
)

for hit in response['hits']['hits']:
    a = str(hit['highlight']['message'])
    y = a.replace("</a> <a href='hyperlinkvariable'>", " ")
    soup = BeautifulSoup(y, 'html.parser')
    hyperlink = soup.a.string
    t = hyperlink.replace("ş", "s").replace("ç", "c").replace(" ", "-")
    k = y.replace("hyperlinkvariable", ("http://127.0.0.1/" + t))
    print(k)