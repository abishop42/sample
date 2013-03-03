import psutil

ignore_keys = ['count','index', 'fromhex', 'hex', 'as_integer_ratio', 'conjugate', 'is_integer']

def get_values(values):

	keys = [d for d in dir(values) if not d[0] == '_' and not d in ignore_keys]
	d = {k:getattr(values, k) for k in keys}
	print d

if __name__ == "__main__":
	get_values(psutil.virtual_memory())
	get_values(psutil.cpu_times())
	get_values(psutil.cpu_percent())

	get_values(psutil.Process(307))	
	
