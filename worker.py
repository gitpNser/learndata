# task_worker.py

import time, sys, queue
from multiprocessing.managers import BaseManager

# create similar queue manager
class QueueManager(BaseManager):
	pass
	
# since this queuemanager is got from network, only need to provide name when register
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# connect to server, that is the machine running taskmaster.py
server_addr = '127.0.0.1'
print('connect to server %s...' % server_addr)

# keep the socket number and authkey as same as taskmaster.py
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')

# connect through network
m.connect()

# get queue
task = m.get_task_queue()
result = m.get_result_queue()

# get task from queue and return reult to result queue
for i in range(10):
	try:
		# print('this is get:>>>',task.get)
		n = task.get(timeout=1)
		print('run task %d * %d...' % (n ,n))
		r = '%d * %d = %d' % (n, n, n*n)
		time.sleep(1)
		result.put(r)
	except queue.Empty:
		print('task queue is empty.')

# procss result
print('worker exit.')