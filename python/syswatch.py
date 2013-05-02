import psutil

for p in psutil.get_pid_list():
	try:
		prc = psutil.Process(p)
		print '-'*6, '\n', prc, '\n', prc.cmdline, '\n', prc.get_memory_info()
	except:
		print "pid no more", p
