BAD_CHARS = [';', '\t', ':', '  ',' , ', ' . ']

def write_file(file_name, lines):
	writer = open(file_name,'w')
	for l in lines:
		writer.write(l)
		writer.write('\n')
	writer.flush()
	writer.close()

def test_line(line, delim='~'):
	tests = {
	}


	results = {}
	elements = line.split(delim)
	pos = 0
	for element in elements:
		results[pos] = {
		'has_leading_space': element[0] == ' ',
		'has_ending_space': element[-1] == ' ',
		'has_bad_chars': any([b in element for b in BAD_CHARS])
		}
		pos = pos + 1

	return elements[0], results



if __name__ == "__main__":
	results = {}
	pos = 0
	for sample_line in open("test_file",'r').readlines():
		k,r = test_line(sample_line)
		
		if not k in results.keys():
			results[k] = []
		
		if not r in results[k]:
			#need to add pos or some way to track which record belongs to which set of lines
			results[k].append(r)

		pos = pos + 1
	#write_file('results.out',results)

	print (results)






