from bs4 import BeautifulSoup
import requests
import re
import time
import random

then = time.time()


def links():
    print("The webpage's full address, please:")
    url = input()
    print('Working on it...')
    the_links = []
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'lxml')
    for each_link in soup.find_all('a'):
        current_link = each_link.get('href')
        if current_link.endswith('.pdf'):
            the_links.append(current_link)
    return the_links


def episode(link):
    candidates = re.split('/', link)
    final_candidates = []
    for each in candidates:
        if each.endswith('.pdf'):
            final_candidates = re.split('-', each)
            final_candidates.append(final_candidates)
    return re.findall(r'\d+', final_candidates[1])[0]


def download():
    print('Where do you want the PDFs to go?  Please specify the full filepath:')
    where_to_save = input()
    for each in links():
        num = episode(each)
        final_destination = where_to_save + f'\{num}.pdf'
        url = each
        my_file = requests.get(url)
        open(final_destination, 'wb').write(my_file.content)


download()

now = time.time()

print('It is finished.  Time elapsed (seconds):', round(now - then))
