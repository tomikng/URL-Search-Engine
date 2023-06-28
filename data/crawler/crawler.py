import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
    urls = set()
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue

        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

        if not is_valid(href):
            continue
        if href in urls:
            continue
        if domain_name not in href:
            continue

        urls.add(href)
        if len(urls) >= 100:
            break

    return urls

if __name__ == "__main__":
    url = input("Enter website url: ")
    links = get_all_website_links(url)

    filename = "../urls/" + urlparse(url).netloc + "_urls.txt"
    with open(filename, "w") as f:
        for url in links:
            f.write(url + "\n")
