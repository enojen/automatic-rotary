# Setting hyperlink with Elasticsearch Percolate Query

This project aims setting hyperlink to given input with Elasticsearch stored queries which means Elasticsearch Percolate query.

## Getting Started

### Prerequisites

* Unix-like operating system (macOS or Linux)
* `git` should be installed.
* `pip` should be installed.
* `elasticsearch` should be installed.

What things you need to install the software and how to install them

- on Ubuntu
    * `git` To install `$ sudo apt-get install git-core`, to check `$ git --version`
    * `pip` To install `$ sudo apt-get install python-pip`, to check `$ pip -v`    
    * `elasticsearch` To install, first you need to install `wget`. After that, The Oracle JDK 8 installed.
        * `$ sudo apt-get update` and `$ sudo apt install wget apt-transport-https`. To install java, `$ sudo add-apt-repository ppa:webupd8team/java` and `$ sudo apt install oracle-java8-installer`, to check `$ java -version`. Finally, we're ready to install elasticsearch.
        `$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -`
        `$ sudo apt-get update && sudo apt-get install elasticsearch`, to check `$ elasticsearch --version` and , to check `$ curl localhost:9200`
- on macOS
    * You need to install first, `brew` package manager. `$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` to check `$ brew --version`
    * `git` To install `$ brew install git`, to check `$ git --version`
    * `pip` To install `$ brew install python`, to check `$ python --version`
    * `elasticsearch` To install `$ brew install elasticsearch`, to check `$ elasticsearch --version` and , to check `$ curl localhost:9200`


### Installing

First, clone the project and go to the project directory

```
git clone https://github.com/keremcankabadayi/research-python.git && cd research-python
```

Install project dependencies

```
pip install -r requirements.txt 
```

Finally, most important step is to start `elasticsearch`

* on macOS (If you used `brew` to install)

```
elasticsearch
```

* on Ubuntu
```
cd elasticsearch/bin
./elasticsearch
```

Great! We're ready to go!

## Usage

* Please make sure, `elasticsearch` is working fine and at `/research-python` directory.
* First, you need to add mapping and create all queries.
    - `titles.json` file should be located at `/research-python` directory and json schema should be like this:
        ```
        {
            "responseHeader":{
                "status":0,
                "QTime":95,
                "params":{
                "q":"*:*",
                "indent":"on",
                "fl":"CourseId, UnitId, title, CourseName, id, FieldId, field",
                "rows":"170109",
                "wt":"json"}},
            "response":{"numFound":170109,"start":0,"docs":[
                {
                 "CourseId":...,
                 "UnitId":...,
                 "title":"...",
                 "id":"...",
                 "CourseName":"...",
                 "FieldId":...,
                 "field":"..."},
                 {
                 "CourseId":...,
                 "UnitId":...,
                 "title":"...",
                 "id":"...",
                 "CourseName":"...",
                 "FieldId":...,
                 "field":"..."},
                 ...
                 ]
        }}
        ```
    - Just run `python addindex.py` and sit back. This process depends on your setup(approximately ~10 min). To check process is working fine,
    `$ curl -X GET "localhost:9200/_cat/indices?v"` and you should see `doc.count` is counting.
* After adding all indexes, you have two options, you can set hyperlink with `name` or `id`
    * To work with `name`
        * run `flask`
        ```
        FLASK_APP=es-linkwithName.py flask run
        ```
        * Go to `http://localhost:5000/`
        * Paste your document
        * See the magic!

    * To work with `id`
         * run `flask`
        ```
        FLASK_APP=es-linkwithId.py flask run
        ```
        * Go to `http://localhost:5000/`
        * Paste your document
        * See the magic!
