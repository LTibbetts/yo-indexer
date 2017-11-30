# Project Title

A test project for in depth python programing

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

#### pip

``` bash
sudo apt-get install python3-pip
```

#### virtualenv

``` bash
sudo pip install virtualenv
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

1. Clone the repository
2. `cd index_analyzer`
3. Run the following:

``` bash
virtualenv env &&
source env/bin/activate &&
pip install -e .
```

4. Run with `python index_analyzer`

## Development

All code installation and running should be done in the isolated virtualenv environment.

In order to access the env after the terminal has closed enter `source env/bin/activate`

If you would like to leave the virtual environmen then enter `deactivate`

Simple change the code and run
`python index_analyzer`

`pip install -e` allows for the code changes to automatically be reflected withing the virtualenv environment. 

## Running the tests

Currently no tests

### Break down into end to end tests

N/A

## Coding Style

Use PEP-8

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

Python3

## Contributing

How to contribute

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **Logan Tibbetts**

See also the list of [contributors](https://github.com/) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
