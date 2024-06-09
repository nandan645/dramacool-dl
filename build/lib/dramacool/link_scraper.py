import requests
from bs4 import BeautifulSoup

def extract_download_link(episode_url):
    cookies = {'auth': 'cS21kWWy4B8k5KPf2FBD8okFfdk%2B4C8NXTIW1zN%2BSN%2Fy6KvpHi%2FcYR0dM8mUSsXSfb8BJdnKglVwpTbGXQoI8g%3D%3D'}
    result = requests.get(episode_url, cookies=cookies)
    htmlcontent = result.content
    site = BeautifulSoup(htmlcontent, 'html.parser')
    download_link = site.find(class_="cf-download").find_all('a')[-1].get('href')
    return download_link
