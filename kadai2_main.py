#!/usr/bin/python
# -*- Coding: utf-8 -*-

from lib import Queue, Node

if __name__=='__main__':
	link_a = Queue()
	link_b = Queue()
	link_c = Queue()

	node1 = Node()
	node2 = Node()
	node3 = Node()

	start_time = 0
	end_time = 0

	line = raw_input()
	start_time = line.split()[1]
	while line:
		line_split = line.split()
		end_time = line_split[1]
		if line_split[0] == '+':
			if line_split[2] == '0' and line_split[3] == '1':
				link_a.enqueue()
			elif line_split[2] == '1' and line_split[3] == '2':
				link_b.enqueue()
			elif line_split[2] == '2' and line_split[3] == '3':
				link_c.enqueue()

		if line_split[0] == '-':
			if line_split[2] == '0' and line_split[3] == '1':
				queue01.dequeue()
			elif line_split[2] == '1' and line_split[3] == '2':
				queue12.dequeue()

		if line_split[0] == 'r':
			if line_split[2] == '0' and line_split[3] == '1':
				node1.receive_p(int(line_split[5]))
			elif line_split[2] == '1' and line_split[3] == '2':
				node2.receive_p(int(line_split[5]))

		if line_split[0] == 'd':
			if line_split[2] == '0' and line_split[3] == '1':
				node1.drop()
			elif line_split[2] == '1' and line_split[3] == '2':
				node2.drop()
		try:
			line = raw_input()
		except EOFError:
			break

	through_put = node2.get_packet() / (float(end_time) - float(start_time))

	print('queue{0}.enqueue = {1}'.format('01', queue01.get_en()))
	print('queue{0}.dequeue = {1}'.format('01', queue01.get_de()))
	print('Node{0}.receive = {1}'.format('1', node1.get_receive()))
	print('Node{0}.drop = {1}'.format('1', node1.get_drop()))

	print('queue{0}.enqueue = {1}'.format('12', queue12.get_en()))
	print('queue{0}.dequeue = {1}'.format('12', queue12.get_de()))
	print('Node{0}.receive = {1}'.format('2', node2.get_receive()))
	print('Node{0}.drop = {1}'.format('2', node2.get_drop()))

	print('through put = {0:,}'.format(through_put))
