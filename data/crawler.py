from bs4 import BeautifulSoup
import requests

# The URL you wish to crawl
url = 'http://example.com'

# Send a GET request to the webpage
response = requests.get(url)

# If the GET request is successful, the status code will be 200
if response.status_code == 200:
    # Get the content of the response
    webpage_text = response.text

    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(webpage_text, 'html.parser')

    # Extract the text from the webpage
    text = soup.get_text()

    # Store the text in a .txt file
    with open('webpage_text.txt', 'w') as file:
        file.write(text)
