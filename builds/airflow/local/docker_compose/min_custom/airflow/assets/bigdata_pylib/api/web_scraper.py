
"""
Multi Threaded Web Scrapper
"""
import threading
import requests
from bs4 import BeautifulSoup

__all__ = ["scrape_urls"]

# This is the function that will be run in a separate thread
def scrape_website(url):
    # Make a request to the website
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the data you want to scrape
    data = soup.find('div', class_='data')
    
    # Print the data
    print(data)

def scrape_urls(urls=[], db=None):
    # Create a thread for each URL
    threads = []
    for url in urls:
        thread = threading.Thread(target=scrape_website, args=(url,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("Scraping completed!")
