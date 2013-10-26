
equals_opertators = ["is", "==","equal","="]

opertators = ["is","not","greater","than","less","equal","to", "<", "<=", "==", ">", ">=", "!=", "like",  "contains","equal","="]
combines = ["and", "or"]

class QuerryString():

	def __init__(self,ops=[],com=[]):
		self.opertators = ops
		self.combines = com
		self.query = ""

	def parse(self, input_string, delim=' '):
		result = []
		initial = input_string.split(delim)

		split_pos = [i for i in range(len(initial)) if initial[i] in combines]

		temp = []

		opp = ["and","or"]

		part = query.split(' ')
		m = [i for i in range(len(part)) if part[i].lower() in opp]
		m.append(-1)
		pos = 0
		
		for i in m:
			if part[pos] in opp:
				temp.append(part[pos])
				pos = pos + 1

			if i == -1:
				temp.append(part[pos:])
			else:
				temp.append(part[pos:i])
			pos = i

		result = []
		for t in temp:
			result.append(self.combine_operators(t))		

		self.query = result
		return result

	def combine_operators(self, input_object):
		result = input_object
		if type([]) == type(input_object):
			result = []
			opp = []
			for i in range(len(input_object)):
				if input_object[i] in opertators: 
					opp.append(input_object[i])
				else:
					if len(opp) > 0:
						result.append(" ".join(opp))
						opp = []
					result.append(input_object[i])
		return result

	def check_object(self, obj):
		result = []
		
		for o in obj:
			status = []
			if type(o) == type({}):
				for q in self.query:
					if type(q) == type([]):
	  					if q[1] in ["is","equal","==", "="]:
	  						status.append("%s" % (o[q[0]] == q[2]))
	  					elif q[1] in ["is not","!="]:
	  						status.append("%s" % (not(o[q[0]] == q[2])))
	  					elif q[1] in ["greater than", ">"]:
	  						status.append("%s" % (float(o[q[0]]) > float(q[2])))
	  					elif q[1] in ["greater than equal to", ">="]:
	  						status.append("%s" % (float(o[q[0]]) >= float(q[2])))
	  					elif q[1] in ["less than", "<"]:
	  						status.append("%s" % (float(o[q[0]]) > float(q[2])))
	  					elif q[1] in ["less than equal to", "<="]:
	  						status.append("%s" % (float(o[q[0]]) <= float(q[2])))
					elif q in ["and", "or"]:
						status.append(q)

			print ("overall => " + " ".join(status))
			overall = eval(" ".join(status))
			print (overall)
			if overall == True:
				result.append(o)

		return result


if __name__ == "__main__":
	input_object = [
		{"input_key":"1111","name":"fred","address":"some street", "suburb":"aplace","postcode":"9999"},
		{"input_key":"1112","name":"fred","address":"some street", "suburb":"aplace","postcode":"9991"},
		{"input_key":"1112","name":"blah","address":"some street", "suburb":"donuts","postcode":"9991"},
		{"input_key":"2222","name":"fred","address":"some street", "suburb":"donuts","postcode":"9992"}
		]

	query = "postcode == 9992 and name == blah or suburb = donuts"

	for i in input_object:
		print (i)

	q = QuerryString(opertators, combines)
	print(q.parse(query))
	print ("*** RESULTS ***")
	for r in q.check_object(input_object):
		print (r)