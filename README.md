# Setting hyperlink with Elasticsearch Percolate Query

This project aims setting hyperlink to given input with Elasticsearch stored queries which means Elasticsearch Percolate query.

## Getting Started

### Prerequisites

* Unix-like operating system (macOS or Linux)
* `git` should be installed.
* `pip` should be installed.
* `flask` should be installed.
* `elasticsearch` should be installed.

What things you need to install the software and how to install them

- on Ubuntu
    * `git` To install `sudo apt-get install git-core`, to check `git --version`
    * `pip` To install `sudo apt-get install python-pip`, to check `pip -v`
    * `flask` To install, `pip install Flask`, to check `pip show flask`
    * `elasticsearch` To install, first you need to install `wget`. After that, The Oracle JDK 8 installed.
        * `sudo apt-get update` and `sudo apt install wget apt-transport-https`. To install java, `sudo add-apt-repository ppa:webupd8team/java`, to check `java -version`. Finally, we're ready to install elasticsearch.
        ```
        wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
        sudo apt-get update && sudo apt-get install elasticsearch
        ```

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
