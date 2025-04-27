import requests
from bs4 import BeautifulSoup
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
# print(&quot;)
def scrape_linkedin_profile(url: str = "", mock: bool = False ):
    if mock:
        linkedin_url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
        scraped_content = requests.get(linkedin_url, timeout = 10)
    
    else:
        headers = {'Authorization': 'Bearer ' + os.getenv('PROXYCURL_API_KEY')}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        scraped_content = requests.get(api_endpoint,
                                params={'url': url},
                                headers=headers)
    content = scraped_content.json()
    processed_content = {
        k: v
        for k,v in content.items() if v not in ["", [], None]
    }

    return processed_content


# content = scrape_linkedin_profile(mock = True)
# content = scrape_linkedin_profile(url='https://www.linkedin.com/in/atishay-jain-b209961b2/', mock = False)
# pprint(content)



# url = "https://www.linkedin.com/in/atishay-jain-b209961b2/"

# x = requests.get('https://w3schools.com')
# print(x.status_code)
# print(BeautifulSoup(x.content, 'html.parser').prettify())


# x.json()
# headers = {
#     "\"User-Agent\"": "\"Guest\"",  # Access as Guest
# }

# response = requests.get(url, headers=headers)
# if response.status_code == 200:
#     BeautifulSoup(response.content, 'html.parser').prettify()

# else:
#     print("Error: Unable to retrieve the LinkedIn company profile. Status code: {status_code}".format(status_code = response.status_code))