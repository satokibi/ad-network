#!/usr/bin/python
# -*- Coding: utf-8 -*-

class Queue():
	def __init__(self, name):
		self.name = name
		self.en = 0
		self.de = 0

	def enqueue(self):
		self.en += 1

	def dequeue(self):
		self.de += 1

	def print_result(self):
		print(self.name + '.enqueue = ' + str(self.en))
		print(self.name + '.dequeue = ' + str(self.de))



class Node():
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
