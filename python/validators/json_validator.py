import copy

def convert_json(data,key_layout):
	result = copy.copy(key_layout)
	for k in key_layout.keys():
		result[k] = data[k] if k in data.keys() else convert_json(data,key_layout[k])
	return result

if __name__ == "__main__":
	base = {"a":1,"b":2,"c":3, "d":[1,2,3,4,5,6,7,8]}
	markup = {"a":"a","details":{"b":"b","c":"c"}}
	result = {"a":1,"details":{"b":2,"c":3}}
	conv = convert_json(base,markup)
	print (conv)
	print (result)
	print (conv == result)
