from bs4 import BeautifulSoup
import requests
import re
import time
import random

then = time.time()


def urls():
    the_urls = []
    for i in range(2, 104):
        url = f'https://nakedbiblepodcast.com/page/{i}'
        the_urls.append(url)
    return the_urls


def links():
    the_links = []
    for each in urls():
        html_content = requests.get(each).text
        soup = BeautifulSoup(html_content, 'lxml')
        for each_link in soup.find_all('a'):
            current_link = each_link.get('href')
            if 'Transcript' in current_link:
                the_links.append(current_link)
    return the_links


def episode(link):
    candidates = re.split('/', link)
    final_candidates = []
    for each in candidates:
        if 'Transcript' in each:
            final_candidates = re.split('-', each)
            final_candidates.append(final_candidates)
    return re.findall(r'\d+', final_candidates[1])[0]


def download():
    print('please specifiy the filepath:')
    where_to_save = input()
    for each in links():
        num = episode(each)
        final_destination = where_to_save + f'\{num}.pdf'
        url = each
        my_file = requests.get(url)
        open(final_destination, 'wb').write(my_file.content)


download()

now = time.time()

print('done in ', now - then, ' seconds')
