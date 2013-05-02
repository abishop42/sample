import requests
import re
  
from BeautifulSoup import BeautifulSoup, Tag,  NavigableString 


def remove_formating(source, invalid_tags):
	for i in invalid_tags:
		source = source.replace(i['tag'], i['replace'])
	return source


MAIN_DATA_KEYS = {"data-runner-name":"name", "data-runner-url":"url",
		"data-runner-number":"number","data-weight-kg":"weight","data-barrier":"barrier",
		"data-horse-age":"age", "data-detail-winprate":"win_rate","data-detail-placerate":"place_rate",
		"data-detail-winrange":"win_range","data-detail-earnings":"earnings",
		"data-detail-weight":"weight_detail","data-detail-trainername":"trainer", 
		"data-detail-jockeyname":"jockey","data-detail-age":"age","data-detail-sex":"sex",
		"data-detail-color":"colors","data-detail-barrier":"barrier"}

SPLIT_PROCESS_DATA_KEYS = {"data-detail-track":"track_runs", "data-detail-dead":"dead_track","data-detail-heavy":"heavy_track",
			"data-detail-synthetic": "synthetic_track","data-detail-turf":"turf_track:","data-detail-1stup":"First_up",
			"data-detail-jumps":"jumps_track","data-detail-career":"career_runs","data-detail-2ndup":"Second_up",
			"data-detail-slow":"slow_track","data-detail-fast":"fast_track","data-detail-jockey":"jockey_rides",
			"data-detail-trackanddistance":"track_distance_runs","data-detail-12months":"runs_last_12_months",
			"data-detail-good":"good_track","data-detail-distance":"distance_runs"}

MAIN_DATA_KEYS.update(SPLIT_PROCESS_DATA_KEYS)

INVALID_HTML_TAGS  = [{'tag':'</b>','replace':''}, 
	{'tag':'<b>','replace':''},
	{'tag':'&nbsp;', 'replace': ' '}]


class Form:
	def __init__(self):
		self.data = {}

	def generate_from_html(self, html_data):
		cols = html_data.findAll('td')		
		split_keys = [b.text for b in cols[1].findAll('b')]
		split_keys[0] = "track"
		split = cols[1].text

		self.data = {} #clear record and start again

		start_pos = 0
					
		for i in range(len(split_keys)):
			
			end_pos = split.find(split_keys[i+1]) if i + 1 < len(split_keys) else len(split)
			value =  split[start_pos: end_pos]
			start_pos = end_pos + len(split_keys[i+1]) if i + 1 < len(split_keys) else end_pos			
			self[split_keys[i]] = value

		self[split_keys[-1]] = split[start_pos:-1]
		self['finish_position'] = cols[0].text


	def keys(self):
		return self.__dict__['data'].keys()

	def __getitem__(self, key):
		result = None
		if key in self.keys():
			result = self.data[key]
		return result

	def __setitem__(self, key, value):
		self.data[key] = value

	def __str__(self):
		keys = ['finish_position', 'track', 'Sectional', 'In-Running']
		return "\t".join(["%s"%self[k] for k in keys])


		

class Runner:
	def __init__(self, name="", url=""):

		self.data = {}
		self.form_data = []

	def process_data(self,html):

		for k in MAIN_DATA_KEYS:
			if html.has_key(k):
				if k in SPLIT_PROCESS_DATA_KEYS.keys():
					t = re.split(' |-',remove_formating(html[k], INVALID_HTML_TAGS))
					self.data[SPLIT_PROCESS_DATA_KEYS[k]] = {'runs':int(t[0]),'first':int(t[1]),'second':int(t[2]),'third':int(t[3])}
				else:
					self.data[MAIN_DATA_KEYS[k]] = remove_formating(html[k], INVALID_HTML_TAGS)
		
		
		rows = html.findAll('tr')

		for r in rows:
			if r.has_key('class'):
				if r['class'] == 'formSummary'	or r['class'] == 'formSummary zebra'  or r['class'] == 'formSummary runnerLast zebra':
					

					form = Form()
					form.generate_from_html(r)
					self.form_data.append(form)



	def print_all(self):
		print '-'*10
		for k in self.data.keys():
			print k,'->', self.data[k]

		print "\n".join(['*'*10, 'form_data', '*'*10])
		for f in self.form_data:
			print f

	def to_string(self):
		keys = ['barrier', 'name', 'weight', 'career_runs']
		return "\t".join(['%s'%self.data[k] for k in keys])

	def __str__(self):
		return self.to_string()


class Race:
	def __init__(self, name=""):
		self.name = name
		self.horses = []

	def add_runner(self, r):
		self.horses.append(r)

	def process_html(self, html_data):
		for table in html_data.findAll('table',{'class':'formGuide'}):

			keys = ['data-runner-name', 'data-runner-url']
			if all([table.has_key(k) for k in keys]):
				runner = Runner()
				runner.process_data(table)
				self.add_runner(runner)

	def __str__(self):
		return "\n".join(['-'*10, self.name, '-'*10] + [r.to_string() for r in self.horses])

class RaceMeeting:
	def __init__(self):
		self.track_details = None
		self.races = []


	def __str__(self):
		return "\n".join(["%s : %s"%(k,self.track_details[k]) for k in self.track_details.keys()])

	def process_track_details(self, html_data):
		self.track_details = {}
		modules = soup.findAll('div', {'class':'Module'})
		for mod in modules:
				if mod.findChild('h3').text == 'Track Details':

					self.track_details['track_conditon'] = mod.find('span').text

					split_keys = [item.text for item in mod.find('div',{'class':'moduleItem'}).findAll('b')]
					split_text = mod.find('div',{'class':'moduleItem'}).text
					#move this into global function?
					for i in range(len(split_keys)):
						start_pos = split_text.find(split_keys[i]) + len(split_keys[i])
						end_pos = split_text.find(split_keys[i + 1]) if i + 1 < len(split_keys) else len(split_text)
						self.track_details[split_keys[i].strip(':')] = split_text[start_pos:end_pos]

					weather = mod.find('div', {'class':'weatherInfo'})
					
					if not weather ==  None:
						temp_cel = weather.find('div', {'id':'tempCel'}).text.replace('&deg;',' degrees ')
						temp_feels_like = temp_cel[temp_cel.find('(')+1:temp_cel.find(')')]
						temp_cel = temp_cel[0:temp_cel.find('|')]

						r = [i.strip('\r\n').replace('&nbsp;', ' ') for i in weather.contents if isinstance(i, NavigableString)]                                                                                                                        
						r = [i for i in r if len(i) > 2]
						self.track_details['weather_details'] = {'current_temp':temp_cel,'feels_like':temp_feels_like, 'details:':r[0]}
						weather_info = r[1].strip().split('  ')
						for i in weather_info:
							split = i.split(':')
							self.track_details['weather_details'][split[0]] = " ".join(split[1:])
		
	

def get_page(url):
	r = requests.get(url)
	return BeautifulSoup(r.content)



if __name__ == "__main__":
	
	#need to add arguments here at some point

	race_meet = RaceMeeting() 
	single_race = True
	test_run = True
	base_url = "http://www.puntersparadise.com.au"
	next_race = "/form-guide/Bendigo_21604/Bendigo-Property-Services-SV-3YO-Fillies-Maiden-Plate_152390/"
	soup = get_page(base_url  + next_race) if test_run == False else BeautifulSoup(open('race_1.html'))

	while True:
	
		next_race = soup.find('a',{'class':'nextRace hoverTrigger'})

		if race_meet.track_details == None:
			race_meet.process_track_details(soup)

		race = Race(soup.find('h2').text)
		race.process_html(soup)

		race_meet.races.append(race)

		if next_race == None or single_race == True:
			break
		else:
			soup = get_page(base_url + next_race['href'])
		
	print race_meet
	for r in race_meet.races:
		print r

