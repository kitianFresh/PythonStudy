#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager

# ��������Ķ���:
task_queue = queue.Queue()
# ���ս���Ķ���:
result_queue = queue.Queue()
def return_task_queue():
	global task_queue
	return task_queue

def return_result_queue():
	global result_queue
	return result_queue
# ��BaseManager�̳е�QueueManager:
class QueueManager(BaseManager):
    pass

def master():
	# ������Queue��ע�ᵽ������, callable����������Queue����:
	QueueManager.register('get_task_queue', callable=return_task_queue)
	QueueManager.register('get_result_queue', callable=return_result_queue)
	# �󶨶˿�5000, ������֤��'abc':
	manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
	# ����Queue:
	manager.start()
	# ���ͨ��������ʵ�Queue����:
	task = manager.get_task_queue()
	result = manager.get_result_queue()
	# �ż��������ȥ:
	for i in range(10):
		n = random.randint(0, 10000)
		print('Put task %d...' % n)
		task.put(n)
	# ��result���ж�ȡ���:
	print('Try get results...')
	for i in range(10):
		r = result.get(timeout=10)
		print('Result: %s' % r)
	# �ر�:
	manager.shutdown()
	print('master exit.')
if __name__ == '__main__':
	#freeze_support()
	master()