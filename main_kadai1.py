#!/usr/bin/python
# -*- Coding: utf-8 -*-

from lib1 import Queue, Node

if __name__=='__main__':
	queue01 = Queue('queue01')
	queue12 = Queue('queue12')
	node1 = Node('node1')
	node2 = Node('node2')
	start_time = 0
	end_time = 0

	line = raw_input()
	start_time = line.split()[1]
	while line:
		log = line.split()
		end_time = log[1]
		if log[0] == '+':
			if log[2] == '0' and log[3] == '1':
				queue01.enqueue()
			elif log[2] == '1' and log[3] == '2':
				queue12.enqueue()

		if log[0] == '-':
			if log[2] == '0' and log[3] == '1':
				queue01.dequeue()
			elif log[2] == '1' and log[3] == '2':
				queue12.dequeue()

		if log[0] == 'r':
			if log[2] == '0' and log[3] == '1':
				node1.receive_p(int(log[5]))
			elif log[2] == '1' and log[3] == '2':
				node2.receive_p(int(log[5]))

		if log[0] == 'd':
			if log[2] == '1':
				node1.drop_p(int(log[5]))
			elif log[2] == '2':
				node2.drop_p(int(log[5]))
		try:
			line = raw_input()
		except EOFError:
			break

	through_put = (node2.get_packet() * 8) / (float(end_time) - float(start_time))
	print(' - - - - - - - - - - - - - - - - - ')
	print('start_time = ' + start_time)
	print('end_time = ' + end_time)
	print('time = ' + str(float(end_time) - float(start_time)))
	print(' - - - - - - - - - - - - - - - - - ')
	queue01.print_result()
	node1.print_result()
	print(' - - - - - - - - - - - - - - - - - ')
	queue12.print_result()
	node2.print_result()
	print('get_packet(bit) = ' + str(node2.get_packet() * 8))
	print('through put = '+ str(through_put))
	print(' - - - - - - - - - - - - - - - - - ')
