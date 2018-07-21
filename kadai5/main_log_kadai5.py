#!/usr/bin/python
# -*- Coding: utf-8 -*-

from models5 import *
import matplotlib.pyplot as plt

def event_check_for_queue(queue, log):
	if log.event == '+':
			enqueue(queue, log)
	elif log.event == '-':
			dequeue(queue, log)

def enqueue(queue, log):
	if log.pck_type == 'tcp' and log.pck_size == 1040:
		queue.enqueue_tcp()
	elif log.pck_type == 'ack':
		queue.enqueue_ack()
	elif log.pck_type == 'tcp':
		queue.enqueue_tcp40()
	elif log.pck_type == 'cbr':
		queue.enqueue_cbr()
		queue.add_log(log)

def dequeue(queue, log):
	if log.pck_type == 'tcp' and log.pck_size == 1040:
		queue.dequeue_tcp()
	elif log.pck_type == 'ack':
		queue.dequeue_ack()
	elif log.pck_type == 'tcp':
		queue.dequeue_tcp40()
	elif log.pck_type == 'cbr':
		queue.dequeue_cbr()

def receive(node, log):
	if log.pck_type == 'tcp' and log.pck_size == 1040:
		node.receive_tcp(log.pck_size)
	elif log.pck_type == 'ack':
		node.receive_ack()
	elif log.pck_type == 'tcp':
		node.receive_tcp40()
	elif log.pck_type == 'cbr':
		node.receive_cbr(log.pck_size)

def drop(node, log):
	if log.pck_type == 'tcp' and log.pck_size == 1040:
		node.drop_tcp(log.pck_size)
	elif log.pck_type == 'ack':
		node.drop_ack()
	elif log.pck_type == 'tcp':
		node.drop_tcp40()
	elif log.pck_type == 'cbr':
		node.drop_cbr(log.pck_size)

if __name__=='__main__':
	queue02 = Queue('queue02')
	queue12 = Queue('queue12')
	queue23 = Queue('queue23')
	queue34 = Queue('queue34')
	queue35 = Queue('queue35')

	node0 = Node('node0')
	node1 = Node('node1')
	node2 = Node('node2')
	node3 = Node('node3')
	node4 = Node('node4')
	node5 = Node('node5')

	start_time = 0
	end_time = 0

	drop04packet = 0
	sum_loss_time = 0


	time_list = []
	through_put_list = []
	drop_num_list = []
	time_list_for_drop = []
	loss_time_ave_list = []
	loss_time_list = []

	line = raw_input()
	start_time = line.split()[1]

	while line:
		ls = line.split()
		end_time = ls[1]
		log = PacketLog(ls[0], ls[1], ls[2], ls[3], ls[4], int(ls[5]), ls[6], ls[7], ls[8], ls[9], ls[10], ls[11])

		time_list.append(log.time)
		if node4.get_udp_packet() != 0 and (float(end_time) - float(start_time)) != 0:
			through_put_list.append(round((node4.get_udp_packet() * 8) / (float(end_time) - float(start_time))/1000, 1))
		else:
			through_put_list.append(0)
		drop_num_list.append(drop04packet)

		if int(log.link_src) + int(log.link_dst) == 2:
			event_check_for_queue(queue02, log)
		elif int(log.link_src) +  int(log.link_dst) == 3:
			event_check_for_queue(queue12, log)
		elif int(log.link_src) +  int(log.link_dst) == 5:
			event_check_for_queue(queue23, log)
		elif int(log.link_src) +  int(log.link_dst) == 7:
			event_check_for_queue(queue34, log)
		elif int(log.link_src) +  int(log.link_dst) == 8:
			event_check_for_queue(queue35, log)


		if log.event == 'r':
			if log.link_dst == '0':
				receive(node0, log)
			elif log.link_dst == '1':
				receive(node1, log)
			elif log.link_dst == '2':
				receive(node2, log)
			elif log.link_dst == '3':
				receive(node3, log)
			elif log.link_dst == '4':
				for l in queue02.logs:
					if l.pck_id == log.pck_id:
						loss_time = float(log.time) - float(l.time)
						print(loss_time)
						sum_loss_time += loss_time

						time_list_for_drop.append(log.time)
						loss_time_ave_list.append(sum_loss_time / (node4.r_cbr + 1) * 1000)
						loss_time_list.append(loss_time * 1000)
				receive(node4, log)
			elif log.link_dst == '5':
				receive(node5, log)

		if log.event == 'd':
			if log.dst_port == '4.0':
				drop04packet += 1

			if log.link_src == '0':
				drop(node0, log)
			elif log.link_src == '1':
				drop(node1, log)
			elif log.link_src == '2':
				drop(node2, log)
			elif log.link_src == '3':
				drop(node3, log)

		try:
			line = raw_input()
		except EOFError:
			break


	through_put = (node4.get_udp_packet() * 8) / (float(end_time) - float(start_time))
	print(' - - - - - - - - - - - - - - - - - ')
	print('start_time = ' + str(start_time))
	print('end_time = ' + str(end_time))
	print('time = ' + str(float(end_time) - float(start_time)))
	print(' - - - - - - - - - - - - - - - - - ')
	print('loss / get (num) = ' + str(drop04packet) + ' / ' + str(queue02.cbr_en))
	print('loss / get (%)   = ' + str(100 * round(float(drop04packet)/float(queue02.cbr_en),5)) + ' %')
	print(' - - - - - - - - - - - - - - - - - ')
	print('total loss time(sec)  = ' + str(sum_loss_time))
	print('node4 receive pck num = ' + str(node4.r_cbr))
	print('ave loss time(sec)  = ' + str(sum_loss_time / node4.r_cbr))
	print('ave loss time(msec) = ' + str((sum_loss_time / node4.r_cbr)*1000))
	print(' - - - - - - - - - - - - - - - - - ')
	print(' - - - - - - - - - - - - - - - - - ')
	print('get_packet(bit)  = ' + str(node4.get_udp_packet() * 8) + ' bit')
	print('get_packet(byte) = ' + str(node4.get_udp_packet()) + ' byte')
	print(' - - - - - - - - - - - - - - - - - ')

	print('through_put = node4.get_packet (byte) * 8 / (end_time - start_time)')
	print('through_put = ' + str(node4.get_udp_packet()) + ' * 8 / (' + str(end_time) + ' - ' + str(start_time) + ')')
	print('through_put = ' + str(node4.get_udp_packet() * 8) + ' / ' + str(float(end_time) - float(start_time)))

	print('through put = '+ str(through_put))
	print('through put = '+ str(round(through_put/1000, 1)) + 'kbps')
	print('through put = '+ str(round(through_put/1000000, 3))  + 'Mbps')
	print(' - - - - - - - - - - - - - - - - - ')
	print(' - - - - - - - - - - - - - - - - - ')
	print(' - - - - - - - - - - - - - - - - - ')
	print(' - - - - - - - - - - - - - - - - - ')
	node0.print_udp_result()
	print(' - - - - - - - - - - - - - - - - - ')
	queue02.print_udp_result()
	print(' - - - - - - - - - - - - - - - - - ')
	node2.print_udp_result()
	print(' - - - - - - - - - - - - - - - - - ')
	queue23.print_udp_result()
	print(' - - - - - - - - - - - - - - - - - ')
	node3.print_udp_result()
	print(' - - - - - - - - - - - - - - - - - ')
	queue34.print_udp_result()
	print(' - - - - - - - - - - - - - - - - - ')
	node4.print_udp_result()
	print(' - - - - - - - - - - - - - - - - - ')


	fig = plt.figure(figsize=(12, 8))
	axL = fig.add_subplot(1,2,1)
	axR = fig.add_subplot(1,2,2)

	axL.plot(time_list, through_put_list, label='throughput', color='blue')
	axL2 = axL.twinx()
	axL2.plot(time_list, drop_num_list, label='total drop pck', color='red')
	axL2.axis(ymin=0,ymax=drop04packet + 5)

	axL.legend(bbox_to_anchor=(1, 0.2))
	axL2.legend(bbox_to_anchor=(1, 0.1))
	axL.set_xlabel('Time (sec)')
	axL.set_ylabel('kbps', color='blue')
	axL2.set_ylabel('num', color='red')

	axR.plot(time_list_for_drop, loss_time_ave_list, label='ave loss time', color='blue')
	axR.plot(time_list_for_drop, loss_time_list, label='loss time', color='red')
	axR.set_xlabel('Time (sec)')
	axR.set_ylabel('msec')
	axR.legend(loc='best')

	axR.axis(ymin=0)

	plt.subplots_adjust(wspace=0.6)

	#plt.savefig('kadai5.png')
	plt.show()

