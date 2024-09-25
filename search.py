from headers import headers
import re
from bs4 import BeautifulSoup
import requests
    
def search(link):
    response = requests.get(link, headers = headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser") # Parse the HTML   
        text = re.sub(r'\s+', ' ', soup.get_text().replace('\n', ' '))
        start_useful_index = text.find("Prepared Remarks:")
        end_useful_index = text.find("Call participants:")
        return text[start_useful_index:end_useful_index]
    return "There was an error with the fetch operation"