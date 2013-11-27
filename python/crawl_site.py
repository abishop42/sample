import requests
import re
  
from bs4 import BeautifulSoup, Tag,  NavigableString 


base_url = "http://www.puntersparadise.com.au/form-guide/"

if __name__ == "__main__":
	r = requests.get(base_url)
	soup = BeautifulSoup(r.content)
	todays_races = soup.findAll("table", {"class":"formList"})[0]
	
	print (todays_races)
