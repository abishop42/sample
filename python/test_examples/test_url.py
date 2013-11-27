import requests
from bs4 import BeautifulSoup, SoupStrainer



class CrawlSite:

	def __init__(self, url, ingore_elements=[]):
		self.visited_urls = []
		self.to_visit = [url]
		self.results = []
		self.ingore_elements = ingore_elements

	def start(self, break_after=10):

		for url in self.to_visit:
			self.check_site(url)

		if break_after > 0 and len(self.visited_urls) > break_after:
			break

	def check_site(self, url):
		r = requests.get(url)
		ok = r.status_code == requests.codes.ok
		self.results.append({'url': url, 'ok':ok, 'reason':r.reason, 'conent-type':r.headers['content-type']})
		print (self.results[-1])
		
		self.visited_urls.append(url)

		if ok == True:
			self.parse_page(r.text)

	def parse_page(self, text):
		soup = BeautifulSoup(text)
		for link in soup.find_all('a'):
			
			if link.has_attr('href'):
				u = link.get('href')	

			if u.find('tel:') < 0:
				if u == '#':
					u = url + u
	
				elif not u[0:4] == 'http':
					u = url + u

				if not u in self.visited_urls and not u in self.to_visit and not u == None:
					self.to_visit(u)
	


if __name__ == '__main__':
	crawl = CrawlSite('http://www.messagemedia.com.au'. ['tel:', 'mailto:'])
	crawl.start()

	

