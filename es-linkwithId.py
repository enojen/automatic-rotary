#coding:utf8
#!/usr/bin/env python # -*- coding: latin-1 -*-
from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup
import webbrowser
import os


from flask import Flask, request, render_template
app = Flask(__name__)

arr = []


@app.route('/')
def my_form():
    return render_template('my-form.html')



@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    userdoc = text.replace(",", " , ")
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
        get_doc_id = str(hit['_source']['doc_id'])
        title = str(hit['highlight']['title'])
        title = title.replace("</a> <a href='hyperlinkvariable'>", " ")
       # soup = BeautifulSoup(title, 'html.parser')
        title = title.replace("hyperlinkvariable",
                              ("http://127.0.0.1/" + get_doc_id))
        soup1 = BeautifulSoup(title, 'html.parser')
        withhyperlink = soup1.a
        plaintext = soup1.a.string
        str_link = str(withhyperlink)
        str_text = str(plaintext)
        userdoc = userdoc.replace(str_text, str_link)
        userdoc = userdoc.replace(" , ", ", ")

        arr.append(userdoc)
    message = arr[len(arr)-1]

    return message
