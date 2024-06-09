import sys
from dramacool import episode_scraper
from dramacool import link_scraper
from dramacool import final_link
from dramacool import ydl

def drama():
    if len(sys.argv) < 2:
        print("Warning: No website URL provided. Please provide a URL as an argument.")
        sys.exit(1)
        
    website_url = sys.argv[1]
    episodes_list = episode_scraper.episode_scraper(website_url)
    episode_counter = 1

    for episodes in episodes_list:
        download_links = link_scraper.extract_download_link(episodes)
        final_url = final_link.final_link(download_links)
        name = episodes.split('/')[-1]
        episode_name = name.replace('.html', '')
        episode_name = episode_name.capitalize()
        formatted_name = f"S01E{episode_counter:02d}"
        drama_name = episode_name.rsplit('-', 2)[0]
        drama_name = drama_name.capitalize()
        # print(drama_name)
        print("\n")
        print(episode_name)
        print("\n")
        # print(formatted_name)
        # print(final_url)
        ydl.download(final_url,formatted_name,drama_name)
        episode_counter += 1

