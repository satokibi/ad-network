#!/usr/bin/python
# -*- Coding: utf-8 -*-

class Queue():
	def __init__(self, name):
		self.name = name
		self.tcp_en = 0
		self.tcp_de = 0
		self.tcp40_en = 0
		self.tcp40_de = 0
		self.ack_en = 0
		self.ack_de = 0

	def enqueue_tcp(self):
		self.tcp_en += 1

	def dequeue_tcp(self):
		self.tcp_de += 1

	def enqueue_tcp40(self):
		self.tcp40_en += 1

	def dequeue_tcp40(self):
		self.tcp40_de += 1

	def enqueue_ack(self):
		self.ack_en += 1

	def dequeue_ack(self):
		self.ack_de += 1

	def print_result(self):
		print(self.name + '.tcp40(+) = ' + str(self.tcp40_en))
		print(self.name + '.tcp40(-) = ' + str(self.tcp40_de))
		print(self.name + '.ack(+) = ' + str(self.ack_en))
		print(self.name + '.ack(-) = ' + str(self.ack_de))
		print(self.name + '.tcp(+) = ' + str(self.tcp_en))
		print(self.name + '.tcp(-) = ' + str(self.tcp_de))


class Node():
	def __init__(self, name):
		self.name = name
		self.r_tcp = 0
		self.r_tcp40 = 0
		self.r_ack = 0
		self.d_tcp = 0
		self.d_tcp40 = 0
		self.d_ack = 0
		self.receive_packet = 0
		self.drop_packet = 0

	def receive_tcp(self, packet):
		self.r_tcp += 1
		self.receive_packet += packet

	def receive_tcp40(self):
		self.r_tcp40 += 1

	def receive_ack(self):
		self.r_ack += 1

	def drop_tcp(self, packet):
		self.d_tcp += 1
		self.drop_packet += packet

	def drop_tcp40(self):
		self.d_tcp40 += 1

	def drop_ack(self):
		self.d_ack += 1

	def get_packet(self):
		return self.receive_packet

	def print_result(self):
		print(self.name + '.r_tcp40 = ' + str(self.r_tcp40))
		print(self.name + '.r_ack = ' + str(self.r_ack))
		print(self.name + '.r_tcp = ' + str(self.r_tcp))
		print(self.name + '.d_tcp40 = ' + str(self.d_tcp40))
		print(self.name + '.d_ack = ' + str(self.d_ack))
		print(self.name + '.d_tcp = ' + str(self.d_tcp))
		print(self.name + '.r_packet = ' + str(self.receive_packet))
		print(self.name + '.d_packet = ' + str(self.drop_packet))

class Log():
	def __init__(self, time, saddr, sport, daddr, dport, maxseq, hiack, seqno, cwnd, ssthresh, dupacks, rtt, srtt, rttvar, bkoff):
		self.time = time
		self.saddr = saddr
		self.sport = sport
		self.daddr = daddr
		self.dport = dport
		self.maxseq = maxseq
		self.hiack = hiack
		self.seqno = seqno
		self.cwnd = cwnd
		self.ssthresh = ssthresh
		self.dupacks = dupacks
		self.rtt = rtt
		self.srtt = srtt
		self.rttvar = rttvar
		self.bkoff = bkoff

	def print_me(self):
		print('time: ' + self.time)
		print('saddr: ' + self.saddr)
		print('sport: ' + self.sport)
		print('daddr: ' + self.daddr)
		print('dport: ' + self.dport)
		print('maxseq: ' + self.maxseq)
		print('hiack: ' + self.hiack)
		print('seqno: ' + self.seqno)
		print('cwnd: ' + self.cwnd)
		print('ssthresh: ' + self.ssthresh)
		print('dupacks: ' + self.dupacks)
		print('rtt: ' + self.rtt)
		print('srtt: ' + self.srtt)
		print('rttvar: ' + self.rttvar)
		print('bkoff: ' + self.bkoff)


