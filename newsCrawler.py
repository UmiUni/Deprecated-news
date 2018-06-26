import requests
from bs4 import BeautifulSoup as bs
import pdb

def parse(newsURLFileName, newsURL):
	for newURL in newsL:
		response = requests.get(newURL)
		plainText = response.text 
		soup = bs(plainText)
		for item in soup.findAll('div', {'class' : 'clus'}):
			pass



def getNewsURL(newsURLFileName, linksURL):
	file = open(newsURLFileName, 'w')
	ls = []
	response = requests.get(linksURL)
	plainText = response.text 
	soup = bs(plainText)
	for item in soup.findAll('a', {'class' : 'tlink'}):	
		href = item.get('href')
		ls.append(href)
	pdb.set_trace()
	for url in ls:
		file.write(url + '\n')
	file.close()
	return ls


if __name__ == '__main__':
	# https://blog.feedspot.com/technology_blogs/  top 100 tech blogs
	newsURLS = getNewsURL('newsURLs.txt', 'https://blog.feedspot.com/technology_blogs/')
	# parse(newsURLS)
