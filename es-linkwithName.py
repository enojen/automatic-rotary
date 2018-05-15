from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup
import webbrowser, os

userdoc = ""
arr = []


def ask_input():
    global userdoc    
    f = open("text.txt", "r")
    userdoc = f.read()          
    userdoc = userdoc.replace(",", " , ")


def elastic():
    global userdoc
    client = Elasticsearch()
    response = client.search(
        index="my-index",
        body={
            "query": {
              "percolate": {
                  "field": "query",
                  "document": {
                      "title": userdoc
                  }
              }
            },
            "highlight": {
                "pre_tags": ["<a href='hyperlinkvariable'>"],
                "post_tags": ["</a>"],
                "fields": {
                    "title": {
                        "number_of_fragments": 0,
                        "no_match_size": -1,
                        "fragment_size": -1

                    }
                }
            }
        }
    )
    for hit in response['hits']['hits']:
        title = str(hit['highlight']['title'])
        title = title.replace("</a> <a href='hyperlinkvariable'>", " ")
        soup = BeautifulSoup(title, 'html.parser')
        hyperlink = soup.a.string
        t = hyperlink.replace("ş", "s").replace("ç", "c").replace(" ", "-").replace("ı", "i").replace("ğ", "g").replace(" ", "-").replace("ö", "o").replace(
            "ü", "u").replace("Ş", "ş").replace("Ç", "ç").replace("İ", "i").replace("Ü", "ü").replace("Ö", "ö").replace("(", "").replace(")", "").replace("â", "a")
        title = title.replace("hyperlinkvariable", ("http://127.0.0.1/" + t))
        f(title)


def f(title):
    global arr
    global userdoc
    soup1 = BeautifulSoup(title, 'html.parser')
    withhyperlink = soup1.a
    plaintext = soup1.a.string
    str_link = str(withhyperlink)
    str_text = str(plaintext)
    userdoc = userdoc.replace(str_text, str_link)
    userdoc = userdoc.replace(" , ", ", ")
    return arr.append(userdoc)


def write_html():
    global arr
    try:
        f = open('index.html', 'w')
        message = arr[len(arr)-1]
        f.write(message)
        f.close()
        filename = 'file://' + os.getcwd() + '/index.html'
        webbrowser.open_new_tab(filename)
    except:
        print("No result!")


try:
    ask_input()
    elastic()
    write_html()
except:
    print("Error! Possible errors:")
    print("- File may not be exist. Make sure text.txt exists in this directory")
    print("- If text.txt exists, make sure there are some text in it.")
    print("- May be no result for this search") 
