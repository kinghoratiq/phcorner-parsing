from bs4 import BeautifulSoup
import urllib
import json

def parseIt(wepage):
	webpage = urllib.request.urlopen('https://www.phcorner.net/threads/558641/')
	soup = BeautifulSoup(webpage, 'html.parser')
	data = []

	for words in soup.find_all('li', attrs={'class':'message'}):
		post = {}
		post['user_id'] = words.find('span', attrs={'class':'style9'}).text
		post['message'] = words.find('blockquote', attrs={'class':'messageText'}).text
		quotes = []
		post['quotes'] = quotes
		for comments in words.find_all('div', attrs={'class':'bbCodeBlock'}):
			quote = {}
			tempUserID = comments.find('div', attrs={'class':'attribution'}).text.split()
			quote['user_id'] = tempUserID[0]
			quote['message'] = comments.find('div', attrs={'class':'quote'}).text
			quotes.append(quote)
		post['date_posted'] = words.find('a', attrs={'class':'datePermalink'}).text
		data.append(post)
	newData = json.dumps(data)
	return newData