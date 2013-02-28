import string
import random 
import os

from sys import stdout
from time import sleep

CHARS = string.ascii_letters + string.digits + '.' + '-' + '_' + '/'

def pprint(data):
	#os.system('clear')
	#stdout.write("%s\r"%data)
	#stdout.flush()
	#sleep(1)
	print "\r%s,"%data, 
	sleep(1)
	


class Randomizer():
	def __init__(self):
		self.data = {}

	def randomize(self, obj_type,**kwargs):
		return self[obj_type]['generate'](**kwargs)

	def validate(self, obj_type, **kwargs):
		return self[obj_type]['validate'](**kwargs)

	def keys(self):
		return self.data.keys()

	def __contains__(self, key):
		return key in self.data.keys()
	
	def __str__(self):
		result = ['-'*10]
		for k in self.keys():
			result.append("%s"%k)
			for i in self[k].keys():
				result.append('\t%s : %s'%(i,self[k][i]))
		result.append('-'*10)
		return '\n'.join(result)

	def __getitem__(self, key):
		return self.data[key]

	def __setitem__(self, key, value):
		self.data[key] = value

if __name__ == "__main__":
	rnd = Randomizer()

	def random_int(min,max): 
		return random.randint(min,max)
	
	def random_int_valid(value): 
		return value > 10 and value < 30

	rnd['int'] = {
		'generate':random_int,
		'validate':random_int_valid
	}

	for k in rnd.keys():
		for i in range(100):
			value = rnd.randomize(obj_type=k,min=1,max=40)
			pprint("%s is valid?' %s"%(value, rnd.validate(obj_type=k,value=value)))
		
