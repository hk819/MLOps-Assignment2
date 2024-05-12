# import necessary libraries
from bs4 import BeautifulSoup
import requests
import json

# function to extract data from a webpage
def extract_data(url):
    # send a GET request to the URL
    response = requests.get(url)
    # parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # extract links, titles, and descriptions
    links = [link['href'] for link in soup.find_all('a')]
    titles = [title.get_text() for title in soup.find_all('h2')]
    descriptions = [description.get_text() for description in soup.find_all('p')]
    # return the extracted data
    return links, titles, descriptions

# URL of the websites to scrape
dawn_url = 'https://www.dawn.com/'
bbc_url = 'https://www.bbc.com/'

# extract data from dawn.com
dawn_links, dawn_titles, dawn_descriptions = extract_data(dawn_url)

# extract data from bbc.com
bbc_links, bbc_titles, bbc_descriptions = extract_data(bbc_url)

# combine the extracted data
extracted_data = {
    'dawn': {'links': dawn_links, 'titles': dawn_titles, 'descriptions': dawn_descriptions},
    'bbc': {'links': bbc_links, 'titles': bbc_titles, 'descriptions': bbc_descriptions}
}

# save the extracted data to a JSON file
with open('articles.json', 'w') as file:
    json.dump(extracted_data, file)