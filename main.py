
import json
from bs4 import BeautifulSoup
from requests import get


myDect = []


page_num = 1

def scrap_data(page_num):
	

	base_url = f'https://quotes.toscrape.com/page/{page_num}/'
	no_msg = 'No quotes found!'

	page = BeautifulSoup(get(base_url).content, 'html.parser')

	
	all_text = page.find_all('span', {'class': 'text'})
	all_tags = page.find_all('div', {'class': 'tags'})

	for qoute, tag in zip(all_text, all_tags):
		myDect.append({'qoute': qoute.text, 'tag': tag.text.replace('\n', '|').strip()})

	print(f'data extracted from page {page_num}')

for i in range(20):
	scrap_data(i)




def convert_to_json(data):
	f = open('out.json', '+a')
	json.dump(data, f)

convert_to_json(myDect)
