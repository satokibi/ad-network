
#!/usr/bin/python
# -*- Coding: utf-8 -*-

from lib2 import Queue, Node

def enqueue(queue):
	if log[5] != '40':
		queue.enqueue_tcp()
	elif log[4] == 'ack':
		queue.enqueue_ack()
	elif log[4] == 'tcp':
		queue.enqueue_tcp40()

def dequeue(queue):
	if log[5] != '40':
		queue.dequeue_tcp()
	elif log[4] == 'ack':
		queue.dequeue_ack()
	elif log[4] == 'tcp':
		queue.dequeue_tcp40()

def receive(node):
	if log[5] != '40':
		node.receive_tcp(int(log[5]))
	elif log[4] == 'ack':
		node.receive_ack()
	elif log[4] == 'tcp':
		node.receive_tcp40()

def drop(node):
	if log[5] != '40':
		node.drop_tcp(int(log[5]))
	elif log[4] == 'ack':
		node.drop_ack()
	elif log[4] == 'tcp':
		node.drop_tcp40()

if __name__=='__main__':
	link_a = Queue('link_a')
	link_b = Queue('link_b')
	link_c = Queue('link_c')
	node0 = Node('node0')
	node1 = Node('node1')
	node2 = Node('node2')
	node3 = Node('node3')
	start_time = 0
	end_time = 0

	line = raw_input()
	start_time = line.split()[1]
	while line:
		log = line.split()
		end_time = log[1]
		if log[0] == '+':
			if int(log[2]) + int(log[3]) == 1:
				enqueue(link_a)	
			elif int(log[2]) +  int(log[3]) == 3:
				enqueue(link_b)	
			elif int(log[2]) +  int(log[3]) == 5:
				enqueue(link_c)	

		if log[0] == '-':
			if int(log[2]) + int(log[3]) == 1:
				dequeue(link_a)	
			elif int(log[2]) +  int(log[3]) == 3:
				dequeue(link_b)	
			elif int(log[2]) +  int(log[3]) == 5:
				dequeue(link_c)	

		if log[0] == 'r':
			if log[3] == '0':
				receive(node0)
			elif log[3] == '1':
				receive(node1)
			elif log[3] == '2':
				receive(node2)
			elif log[3] == '3':
				receive(node3)

		if log[0] == 'd':
			if log[2] == '0':
				drop(node0)
			elif log[2] == '1':
				drop(node1)
			elif log[2] == '2':
				drop(node2)
			elif log[2] == '3':
				drop(node3)
		try:
			line = raw_input()
		except EOFError:
			break

	through_put = node3.get_packet() * 8 / (float(end_time) - float(start_time))
	print(' - - - - - - - - - - - - - - - - - ')
	print('start_time = ' + start_time)
	print('end_time = ' + end_time)
	print('time = ' + str(float(end_time) - float(start_time)))
	print(' - - - - - - - - - - - - - - - - - ')
	node0.print_result()
	print(' - - - - - - - - - - - - - - - - - ')
	link_a.print_result()
	print(' - - - - - - - - - - - - - - - - - ')
	node1.print_result()
	print(' - - - - - - - - - - - - - - - - - ')
	link_b.print_result()
	print(' - - - - - - - - - - - - - - - - - ')
	node2.print_result()
	print(' - - - - - - - - - - - - - - - - - ')
	link_c.print_result()
	print(' - - - - - - - - - - - - - - - - - ')
	node3.print_result()
	print(' - - - - - - - - - - - - - - - - - ')
	print(node3.name + '.get_packet(bit) = ' + str(node3.get_packet() * 8))
	print('through put = '+ str(through_put))
	print(' - - - - - - - - - - - - - - - - - ')
