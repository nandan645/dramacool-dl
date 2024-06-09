import requests
from bs4 import BeautifulSoup

def episode_scraper(website_url):
    result = requests.get(website_url)
    htmlcontent = result.content

    domain = (website_url).split('/')[2]
    site = BeautifulSoup(htmlcontent, 'html.parser')

    episodes = []

    for a in site.find(class_="list-episode-item-2 all-episode").find_all('a', href=True):
        episode = ("https://"+domain+a['href'])
        episodes.append(episode)

    episodes = episodes[::-1]
    return episodes
