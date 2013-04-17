import system_monitor
import os
import sys
import threading
import time


#process monitor monitors the currec specifeid process

class ProcessMonitor(system_monitor.SystemThread):
	
	def __init__(self,name,folder,delay=1):
		threading.Thread.__init__(self)
		self.name = name
		self.delay = delay
		self.finished = False
		self.folder = folder
		self.values = {}
	
	def completed(self):
		return self.finished or os.path.exists(self.folder)
	
	def process_file(self, file_name):
		return file(file_name,'r').readlines()

	def process_data(self,t,data):
		for d in data:
			if t == 'stat':
				a = d.split(' ')
				self.values[a[0]] = a[1:]
			else:
				a = d.split(' ')
				self.values[a[0]] = a[1:]

	def run(self):
		while not(self.completed()):
			#read file(s)
			start = time.now()
			files = []
			if os.path.isdir(self.folder):
				files = os.listdir(self.folder)
			else:
				#folder contains a name
				files = [self.folder]
			for f in files:
				self.process_data(self.name,self.process_file(f))
			end = time.now()
								
	def stop(self):
		self.finished = True
	
	def __str__(self):
		return "%s %s"%(self.name,self.folder)



class ProcessReader(system_monitor.SystemThread):
	
	def __init__(self,name,delay=1,folder=system_monitor.SYS_FOLDER):
		threading.Thread.__init__(self)
		self.pids = []
		self.process_folder = folder
		self.name=name
		self.delay=delay
		self.finished=False
		self.children = []

	def display(self):

		sys.stderr.write(system_monitor.CLEAR_BUFFER)
		sys.stderr.flush()

		sys.stdout.write(self.name + "\n")
		sys.stdout.write("number children\t=>\t%s\nnumber of pids\t=>\t%s\n-----------\n"
			%(len(self.children),len(self.pids)))
		
		s = ""
		details = "    "
	
		for c in self.children:
			s = "%s , %s"%(c.name,s)
			if c.name == "stat":
				for k in self.values:
					details = "%s , %s -> %s"%(details,k,self.values[k])

		sys.stdout.write(s)	
		sys.stdout.write("\n")
	
		if len(details) > 0:
			sys.stdout.write("-----------\n%s\n"%details)
		sys.stdout.flush()

	def addchild(self,child):
		self.children.append(child)

	def completed(self):
		return self.finished

	def run(self):
		count = 10000
		stat = ProcessMonitor("stat",self.process_folder,1)
		stat.start()
		self.addchild(stat)
		while not(self.completed()):
			self.pids = self.get_contents(self.process_folder)
			active = [c.name for c in self.children]
			for p in self.pids:
				if not(p in active):
					pm = ProcessMonitor(p, self.process_folder + "/" + p,1)
					pm.start()
					self.addchild(pm)
			for c in self.children:
				if c.name not in self.pids:
					c.stop()
					self.children.remove(c)	
			time.sleep(1)
			if count == 0:
				self.stop()
			else:
				count = count - 1
			self.display()

	def stop(self):
		self.finished = True

	def get_contents(self,folder):
		result = []
		for r in os.listdir(folder):
			if r.isdigit() and os.path.isdir(folder + "/" + r):
				result.append(r)
		return result
	
	def __str__(self):
		s = ""
		for p in self.children:
			s = p + ", " + s
		return "%s\tnumber of pids %s\n%s"%(self.process_folder,len(self.children),s)



if __name__ == '__main__':
	top = ProcessReader("ProcessReader -> Master",1)
	top.start()
	top.finished()
	
