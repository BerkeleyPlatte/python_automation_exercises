from bs4 import BeautifulSoup
import requests

url='https://www.sbnation.com/nfl/2015/2/20/8077097/2015-nfl-combine-wide-receivers-bench-press'

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, 'lxml')
table = soup.find('table')
rows = table.tbody.find_all('tr')

data_i_want = []
for each in rows:
    cell = each.find_all('td')
    for each in cell:
        data_i_want.append(each.text)
        
nums = []
for each in data_i_want:
    if 0 < len(each) and len(each) < 3:
        nums.append(int(each))
        
print(int(sum(nums)) / int(len(nums)))   
