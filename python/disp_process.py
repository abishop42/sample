import psutil
from time import sleep


class ProcessMonitor():
	def __init__(self):
		self.state = StateReader()

	def display_state(self):
		print self.state.read_values()

	def show(self):
		while True:
			self.display_state()
			sleep(1)


class StateReader():
	def __init__(self):
		self.ignore_keys = ['count','index', 'fromhex', 'hex', 'as_integer_ratio', 'conjugate', 'is_integer']

	def get_values(self, values):
		keys = [d for d in dir(values) if not d[0] == '_' and not d in self.ignore_keys]
		d = {k:getattr(values, k) for k in keys}
		return d

	def read_values(self):
		return [self.get_values(psutil.virtual_memory()),
		self.get_values(psutil.cpu_times()),
		self.get_values(psutil.cpu_percent())]
#
#	get_values(psutil.Process(307))	

if __name__ == "__main__":
	pm = ProcessMonitor()
	pm.show()
