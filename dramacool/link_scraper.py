import requests
from bs4 import BeautifulSoup

def extract_download_link(episode_url):
    cookies = {'auth': 'RVBXSam9KIobzTBoVRrsHYA1iG1SMGvLhfm79KYphvpJK87dWCBNdZ4nETvG5%2FQ26M7CLlAw241hdMtr7ZfNwg%3D%3D'}
    result = requests.get(episode_url, cookies=cookies)
    htmlcontent = result.content
    site = BeautifulSoup(htmlcontent, 'html.parser')
    download_link = site.find(class_="cf-download").find_all('a')[-1].get('href')
    return download_link
