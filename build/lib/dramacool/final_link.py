from dramacool import link_scraper
import requests
from bs4 import BeautifulSoup

def final_link(download_link):
    result = requests.get(download_link, allow_redirects=True)
    htmlcontent = result.content
    site = BeautifulSoup(htmlcontent, 'html.parser')
    final = site.find('script', type='text/javascript')
    if final:
        location_value = final.string.strip()
        url_start_index = location_value.find('"') + 1
        url_end_index = location_value.rfind('"')
        final_url = location_value[url_start_index:url_end_index]
        return final_url
    else:
        return None

