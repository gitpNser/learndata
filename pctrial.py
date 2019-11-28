from multiprocessing import Process, Queue
import os, time, random

# write data processing
def write(q):
	print('Process to write： %s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())
		
# read data processing
def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)

if __name__=='__main__':
	# parent procss to creat queue and pass to children processes
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	# initiate child process pw
	pw.start()
	# initiate child process pr
	pr.start()
	# wait pw to close
	pw.join()
	# pr is a endless loop, need terminate mannually
	pr.terminate()