#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, time, queue
from multiprocessing.managers import BaseManager

# ��BaseManager�̳е�QueueManager:
class QueueManager(BaseManager):
	pass
	
# ���QueueManagerֻ�������ϻ�ȡQueue������ע����ֻ�ṩ����:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# ���ӵ�������:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# �˿ں���֤��ע�Ᵽ����task_master.py���õ���ȫһ�£�
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# ���������ӣ�
m.connect()
# ͨ�������ȡQueue�Ķ���:
task = m.get_task_queue()
result = m.get_result_queue()
# ��task����ȡ���񣬲��Ѵ�����д��result���У�
for i in range(10):
	try:
		n = task.get(timeout=1)
		print('run task %d * %d...' % (n,n))
		r = '%d * %d = %d' % (n, n, n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty.')
# ���������
print('worker exit.')