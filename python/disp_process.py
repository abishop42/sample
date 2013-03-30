import psutil
from time import sleep
import sys
import os

class ProcessMonitor():
	def __init__(self):
		self.state = StateReader()
		self.out = sys.stdout

	def show(self):
		first_time = False
		while True:
			values = self.state.read_values()
			if not first_time:
				self.out.write(",".join(values.keys()))
				self.out.write("\n")
				first_time = True
			self.out.write(",".join([str(values[key]) for key in values]))
			self.out.write("\n")
			sleep(1)


class StateReader():
	def __init__(self):
		self.ignore_keys = ['count','index', 'fromhex', 'hex', 'as_integer_ratio', 'conjugate', 'is_integer']
		self.functions = ['virtual_memory', 'cpu_times','cpu_percent']

	def get_values(self, values):
		keys = [d for d in dir(values) if not d[0] == '_' and not d in self.ignore_keys]
		return {k:getattr(values, k) for k in keys}

	def read_values(self):
		results = {}
		for f in self.functions:
			#What about same keys?
			new_values = self.get_values(getattr(psutil, f)())
			results.update({"%s_%s"%(f,k):new_values[k] for k in new_values.keys()})
		return results

if __name__ == "__main__":
	pm = ProcessMonitor()
	pm.show()
