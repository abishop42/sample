import requests
from bs4 import BeautifulSoup, SoupStrainer

visited_urls = []

results = []

def check_site(urls):
	#TODO: make sure that base url is tht base of the current url being looked at
	#      as just setting base url could end up with some bad stuff happening
	results = []
	new_urls = []
	for url in urls:
		r = requests.get(url)
		ok = r.status_code == requests.codes.ok
		results.append({'url': url, 'ok':ok, 'reason':r.reason, 'conent-type':r.headers['content-type']})
		print (results[-1])
		visited_urls.append(url)
		if ok == True:
			soup = BeautifulSoup(r.text)
			for link in soup.find_all('a'):
				if link.has_attr('href'):
					u = link.get('href')	
					if u.find('tel:') < 0:
						if u == '#':
							u = url + u
	
						elif not u[0:4] == 'http':
							u = url + u

						if not u in visited_urls and not u in new_urls and not u == None:
							new_urls.append(u)
	
	for r in results:
		print (r)

	if new_urls:
		check_site(new_urls)


if __name__ == '__main__':
	test_urls = ['http://www.messagemedia.com.au']
	
	print (check_site(test_urls))

	

