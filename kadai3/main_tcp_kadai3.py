#!/usr/bin/python
# -*- Coding: utf-8 -*-

from models3 import Queue, Node, Log
import matplotlib.pyplot as plt

if __name__=='__main__':

	line = raw_input()
	x_time = []
	y_cwnd = []
	y_ssthresh = []
	y_seqno = []
	while line:
		ls = line.split()
		log = Log(ls[1], ls[3], ls[5], ls[7], ls[9], ls[11], ls[13], ls[15], ls[17], ls[19], ls[21], ls[23], ls[25], ls[27], ls[29])

		log.print_me()
		print('- - - - - - - - - -')
		x_time.append(float(log.time))
		y_cwnd.append(float(log.cwnd))
		y_ssthresh.append(int(log.ssthresh))
		y_seqno.append(int(log.seqno))
		try:
			line = raw_input()
		except EOFError:
			break

	fig, ax1 = plt.subplots()
	ax1.plot(x_time, y_cwnd, label='cwnd')
	ax1.plot(x_time, y_ssthresh, label='ssthresh')
	ax1.set_xlabel('Time (sec)')
	ax1.set_ylabel('cwnd, ssthresh')

	ax2 = ax1.twinx()

	ax2.plot(x_time, y_seqno, color='red', label='seqno')
	ax2.set_ylabel('Sequence Number')

	ax1.legend(bbox_to_anchor=(0,1),loc='upper left')
	ax2.legend(bbox_to_anchor=(0,0.85),loc='upper left')
	plt.show()
