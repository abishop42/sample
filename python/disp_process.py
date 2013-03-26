import psutil
from time import sleep
import sys
import os

class ProcessMonitor():
	def __init__(self):
		self.state = StateReader()
		self.out = sys.stdout

	def display_state(self):
		self.out.write(str(self.state.read_values()) + '\n')

	def show(self):
		while True:
			self.display_state()
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
			results.update(self.get_values(getattr(psutil, f)()))
		return results

if __name__ == "__main__":
	pm = ProcessMonitor()
	pm.show()
