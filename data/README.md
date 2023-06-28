# Simple Python Crawler

This is a simple Python crawler built using Scrapy. It takes a domain as input and crawls the domain until it has found 100 URLs. The URLs are then written to a text file named after the domain.

## Installation

First, you need to install Scrapy. You can do this using pip:

```shell
pip install Scrapy
```

## Usage

Firstly direct to the correct directory

```shell
cd crawler
```

To run the spider, use the following command:

```shell
scrapy runspider crawler.py -a start_url=http://www.example.com -a allowed_domains=example.com
```

Replace `'http://www.example.com'` and `'example.com'` with the URL and domain you want to crawl. 

The spider will start crawling from the URL you've provided. It will follow links on each page to find more pages in the same domain. It will stop when it has found 100 URLs. 

The URLs will be written to a file named after the domain, with `_urls.txt` appended to the domain name. For example, if you crawled 'example.com', the URLs would be written to a file called `example.com_urls.txt`.

## Notes

Always respect the terms of service and privacy policy of the website you're crawling. Some websites explicitly disallow certain types of web crawling, so always make sure to check these policies before you begin.

Also, keep in mind that this is a simple crawler and doesn't include features like delay between requests, respect for `robots.txt`, or handling of different types of URLs leading to the same page. Use it as a starting point for building a more sophisticated crawler.

---

You can customize this README to suit your project's requirements, add more details about the installation process or usage, and include any other important information users of your script might need to know.