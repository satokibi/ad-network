#!/usr/bin/python
# -*- Coding: utf-8 -*-

from models4 import *
import matplotlib.pyplot as plt

if __name__=='__main__':
	queue02 = QueueUdp('queue02')
	queue12 = QueueUdp('queue12')
	queue23 = QueueUdp('queue23')
	queue34 = QueueUdp('queue34')
	queue35 = QueueUdp('queue35')

	node0 = NodeUdp('node0')
	node1 = NodeUdp('node1')
	node2 = NodeUdp('node2')
	node3 = NodeUdp('node3')
	node4 = NodeUdp('node4')
	node5 = NodeUdp('node5')

	start_time = 0
	end_time = 0

	drop04packet = 0
	sum_loss_time = 0

	jitter = 0

	time_list = []
	through_put_list = []
	drop_num_list = []
	receive_packet_num = []
	loss_time_ave_list = []
	loss_time_list = []
	jitter_list = []

	line = raw_input()
	start_time = line.split()[1]

	while line:
		ls = line.split()
		end_time = ls[1]
		log = PacketLog(ls[0], ls[1], ls[2], ls[3], ls[4], int(ls[5]), ls[6], ls[7], ls[8], ls[9], ls[10], ls[11])

		time_list.append(log.time)
		if node4.get_packet() != 0 and (float(end_time) - float(start_time)) != 0:
			through_put_list.append(round((node4.get_packet() * 8) / (float(end_time) - float(start_time))/1000, 1))
		else:
			through_put_list.append(0)

		drop_num_list.append(drop04packet)
		if log.event == '+':
			if log.link_src == '0' and log.link_dst == '2':
				queue02.enqueue()
				queue02.add_log(log)
			elif log.link_src == '1' and log.link_dst == '2':
				queue12.enqueue()
			elif log.link_src == '2' and log.link_dst == '3':
				queue23.enqueue()
			elif log.link_src == '3' and log.link_dst == '4':
				queue34.enqueue()
			elif log.link_src == '3' and log.link_dst == '5':
				queue35.enqueue()

		if log.event == '-':
			if log.link_src == '0' and log.link_dst == '2':
				queue02.dequeue()
			elif log.link_src == '1' and log.link_dst == '2':
				queue12.dequeue()
			elif log.link_src == '2' and log.link_dst == '3':
				queue23.dequeue()
			elif log.link_src == '3' and log.link_dst == '4':
				queue34.dequeue()
			elif log.link_src == '3' and log.link_dst == '5':
				queue35.dequeue()

		if log.event == 'r':
			if log.link_src == '0' and log.link_dst == '2':
				node2.receive_p(log.pck_size)
			elif log.link_src == '1' and log.link_dst == '2':
				node2.receive_p(log.pck_size)
			elif log.link_src == '2' and log.link_dst == '3':
				node3.receive_p(log.pck_size)
			elif log.link_src == '3' and log.link_dst == '4':
				for l in queue02.logs:
					if l.pck_id == log.pck_id:
						loss_time = float(log.time) - float(l.time)
						sum_loss_time += loss_time

						jitter = jitter + ((abs(loss_time) - jitter) / 16)
						# receive_packet_num.append(node4.receive + 1)
						receive_packet_num.append(log.time)
						loss_time_ave_list.append(sum_loss_time / (node4.receive + 1) * 1000)
						loss_time_list.append(loss_time * 1000)
						jitter_list.append(jitter * 1000)
				node4.receive_p(log.pck_size)
			elif log.link_src == '3' and log.link_dst == '5':
				node5.receive_p(log.pck_size)

		if log.event == 'd':
			if log.dst_port == '4.0':
				drop04packet += 1

			if log.link_src == '0' and log.link_dst == '2':
				node2.drop_p(log.pck_size)
			elif log.link_src == '1' and log.link_dst == '2':
				node2.drop_p(log.pck_size)
			elif log.link_src == '2' and log.link_dst == '3':
				node3.drop_p(log.pck_size)
			elif log.link_src == '3' and log.link_dst == '4':
				node4.drop_p(log.pck_size)
			elif log.link_src == '3' and log.link_dst == '5':
				node5.drop_p(log.pck_size)

		try:
			line = raw_input()
		except EOFError:
			break


	through_put = (node4.get_packet() * 8) / (float(end_time) - float(start_time))
	print(' - - - - - - - - - - - - - - - - - ')
	print('start_time = ' + str(start_time))
	print('end_time = ' + str(end_time))
	print('time = ' + str(float(end_time) - float(start_time)))
	print(' - - - - - - - - - - - - - - - - - ')
	print('loss / get (num) = ' + str(drop04packet) + ' / ' + str(queue02.en))
	print('loss / get (%)   = ' + str(100 * round(float(drop04packet)/float(queue02.en),5)) + ' %')
	print(' - - - - - - - - - - - - - - - - - ')
	print('total loss time(sec)  = ' + str(sum_loss_time))
	print('node4 receive pck num = ' + str(node4.receive))
	print('ave loss time(sec)  = ' + str(sum_loss_time / node4.receive))
	print('ave loss time(msec) = ' + str((sum_loss_time / node4.receive)*1000))
	print(' - - - - - - - - - - - - - - - - - ')
	print('jitter(sec)  = ' + str(jitter))
	print('jitter(msec) = ' + str(jitter * 1000))
	print(' - - - - - - - - - - - - - - - - - ')
	print('get_packet(bit)  = ' + str(node4.get_packet() * 8) + ' bit')
	print('get_packet(byte) = ' + str(node4.get_packet()) + ' byte')
	print(' - - - - - - - - - - - - - - - - - ')

	print('through_put = node4.get_packet (byte) * 8 / (end_time - start_time)')
	print('through_put = ' + str(node4.get_packet()) + ' * 8 / (' + str(end_time) + ' - ' + str(start_time) + ')')
	print('through_put = ' + str(node4.get_packet() * 8) + ' / ' + str(float(end_time) - float(start_time)))


	print('through put = '+ str(through_put))
	print('through put = '+ str(round(through_put/1000, 1)) + 'kbps')
	print('through put = '+ str(round(through_put/1000000, 3))  + 'Mbps')
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

	axR.plot(receive_packet_num, loss_time_ave_list, label='ave loss time')

	axR.plot(receive_packet_num, loss_time_list, label='loss time')
	axR.plot(receive_packet_num, jitter_list, label='jitter')
	axR.set_xlabel('Time (sec)')
	axR.set_ylabel('msec')
	axR.legend(loc='best')

	plt.subplots_adjust(wspace=0.6)
	plt.savefig('kadai4.png')
	plt.show()

