# task_master.py

import random, time, queue
from multiprocessing.managers import BaseManager

# send task queue
task_queue = queue.Queue()
# receive task result
result_queue = queue.Queue()

# inherited QueueManagers from BaseManager
class QueueManager(BaseManager):
	pass

# no pickle in windows, and no lambda in it too
def return_task_queue():
	global task_queue
	return task_queue

def return_result_queue():
	global result_queue
	return result_queue

# def a main process
if __name__== '__main__':

	# register 2 queues to network, link callable parameters to queue object
	QueueManager.register('get_task_queue', callable=return_task_queue)
	QueueManager.register('get_result_queue', callable=return_result_queue)

	# set socket number to 5000 and authkey to 'abc'
	manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

	# initiate Queue
	manager.start()

	# get queue object through network
	task = manager.get_task_queue()
	result = manager.get_result_queue()

	# put some tasks
	for i in range(10):
		n = random.randint(0,10000)
		print('put task %d...' % n)
		task.put(n)

	# get result from result_queue
	print('Try to get results...')

	for i in range(10):
		r = result.get(timeout=10)
		print('Result: %s' % r)

	# close
	manager.shutdown()
	print('master exit.')
