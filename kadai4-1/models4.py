#!/usr/bin/python
# -*- Coding: utf-8 -*-

class QueueTcp():
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


class NodeTcp():
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

class QueueUdp():
	def __init__(self, name):
		self.name = name
		self.en = 0
		self.de = 0
		self.logs = []

	def enqueue(self):
		self.en += 1

	def dequeue(self):
		self.de += 1

	def add_log(self, log):
		self.logs.append(log)

	def print_result(self):
		print(self.name + '.enqueue = ' + str(self.en))
		print(self.name + '.dequeue = ' + str(self.de))

class NodeUdp():
	def __init__(self, name):
		self.name = name
		self.receive = 0
		self.drop = 0
		self.receive_packet = 0
		self.drop_packet = 0

	def receive_p(self, packet):
		self.receive += 1
		self.receive_packet += packet

	def drop_p(self, packet):
		self.drop += 1
		self.drop_packet += packet

	def get_packet(self):
		return self.receive_packet

	def print_result(self):
		print(self.name + '.receive = ' + str(self.receive))
		print(self.name + '.drop = ' + str(self.drop))
		print(self.name + '.receive_packet(byte) = ' + str(self.receive_packet))
		print(self.name + '.drop_packet(byte) = ' + str(self.drop_packet))

class PacketLog():
	def __init__(self, event, time, link_src, link_dst, pck_type, pck_size, flag, flow_id, src_port, dst_port, seq, pck_id):
		self.event = event
		self.time = time
		self.link_src = link_src
		self.link_dst = link_dst
		self.pck_type = pck_type
		self.pck_size = pck_size
		self.flag = flag
		self.flow_id = flow_id
		self.src_port = src_port
		self.dst_port = dst_port
		self.seq = seq
		self.pck_id = pck_id

	def print_me(self):
		print('event: ' + self.event)
		print('time:' + self.time)
		print('link_src: ' + self.link_src)
		print('link_dst: ' + self.link_dst)
		print('pck_type: ' + self.pck_type)
		print('pck_size: ' + str(self.pck_size))
 		print('flag: ' + self.flag)
		print('flow_id: ' + self.flow_id)
		print('src_port: ' + self.src_port)
		print('dst_port: ' + self.dst_port)
		print('seq: ' + self.seq)
		print('pck_id: ' + self.pck_id)


class TcpLog():
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


