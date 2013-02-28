import string
import random 
from pprint import pprint

CHARS = string.ascii_letters + string.digits + '.' + '-' + '_' + '/'
class Randomizer():
	def __init__(self):
		self.data = {}

	def randomize(self, obj_type):
		test = self[obj_type]
		test_type = type(test['object_type'])
		result = None
		if test_type == type({}):
			result = {k : eval(test['generator'][k]) for k in test['object_type']}
		else:
			result = eval(test['generator'])

		return result

	def validate(self, obj_type, check):
		test = self[obj_type]
		test_type = type(test['object_type'])
		result = None
		if test_type == type({}):
			result = all([eval(test['validator'][k]) for k in test['object_type']])
		else:
			result = eval(test['validator'])

		return result

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

	rnd['dict_test'] = {
	'object_type':{'other': type(True), 'name': type(""), 'num': type(0)},
	'generator': {
		'num':"random.randint(0,100)",
		'other':"{1:True,0:False}[random.randint(0,1)]",
		'name':"''.join(random.choice(CHARS) for x in range(0,10))"
	},
	'validator':{
		'num':"check['num'] < 70",
		'other':"check['other'] == True",
		'name':"not any([c in ['.','/'] for c in check['name']])"
	}}

	rnd['string_test'] = {
		'object_type':type(""),
		'generator':"''.join(random.choice(CHARS) for x in range(0,20))",
		'validator':"not any([c in ['.','/'] for c in check])"
	}

	rnd['array_test'] = {
		'object_type':type([]),
		'generator':"[random.randint(0,i) for i in range(random.randint(0,20))]",
		'validator':"len(check) < 16 and all([i%2==0 for i in check])"
	}

	print rnd
	for t in ['dict_test','string_test', 'array_test']:
		for j in range(10):
			counts = {True:0.0, False:0.0}
			for i in range(100):
				check = rnd.randomize(t)
				valid = rnd.validate(t,check)
				counts[valid] = counts[valid] + 1
			print t, counts

