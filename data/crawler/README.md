# Simple Python Crawler

This is a simple Python crawler built using Scrapy. It takes a domain as input and crawls the domain until it has found 100 URLs. The URLs are then written to a text file named after the domain.

## Installation

Firstly install all required packages

```shell
pip install -r requirements.txt
```

## Usage

```shell
python crawler.py
```

The program will take as an input starting URL and the output would be stored in directory `urls` 