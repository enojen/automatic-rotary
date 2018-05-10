from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup
import webbrowser

userdoc = ""
arr = []
def ask_input(a):
  global userdoc
  while(not userdoc):
    userdoc = input(a)
  #userdoc = userdoc.replace(",", " , ")
  print(userdoc)
  return

def elastic():
  global userdoc
  client = Elasticsearch()
  response = client.search(
    index="my-index",
    body={
      "query" : {
        "percolate" : {
            "field": "query",
            "document" : {
                "title" : userdoc
            }
        }
    },
    "highlight": {
      "pre_tags" : ["<a href='hyperlinkvariable'>"],
      "post_tags" : ["</a>"],
      "fields": {
        "title": {
          "number_of_fragments" : 20,
          "no_match_size": 2000,
          "fragment_size" : 2000
          
        }
      }
    }
    }
  )
  for hit in response['hits']['hits']:
    a = str(hit['highlight']['title'])
    y = a.replace("</a> <a href='hyperlinkvariable'>", " ")
    soup = BeautifulSoup(y, 'html.parser')
    hyperlink = soup.a.string
    t = hyperlink.replace("ş", "s").replace("ç", "c").replace(" ", "-").replace("ı", "i").replace("ğ", "g").replace(" ", "-").replace("ö", "o").replace("ü", "u").replace("Ş", "ş").replace("Ç", "ç").replace("İ", "i").replace("Ü", "ü").replace("Ö", "ö").replace("(", "").replace(")", "")
    k = y.replace("hyperlinkvariable", ("http://127.0.0.1/" + t))
    f(k)
def f(k):
    global arr
    soup1 = BeautifulSoup(k, 'html.parser')
    withhyperlink = soup1.a
    plaintext = soup1.a.string
    str_link = str(withhyperlink)
    str_text = str(plaintext)
    global userdoc
    userdoc = userdoc.replace(str_text, str_link)
    userdoc = userdoc.replace(" , ", ", ")
    return arr.append(userdoc)

def write_html():
    global arr
    try:
      f = open('index.html','w')
      message = arr[len(arr)-1]
      f.write(message)
      f.close()
      filename = 'file:///Users/kerem/Desktop/es/index.html'
      webbrowser.open_new_tab(filename)
    except:
      print("No result!")

ask_input("Please enter your document: ")
elastic()
write_html()