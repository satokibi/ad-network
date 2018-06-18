#!/usr/bin/python
# -*- Coding: utf-8 -*-

class Queue():
	def __init__(self):
		self.en = 0
		self.de = 0

	def enqueue(self):
		self.en += 1

	def dequeue(self):
		self.de += 1

	def get_en(self):
		return self.en

	def get_de(self):
		return self.de


class Node():
	def __init__(self):
		self.receive = 0
		self.drop = 0
		self.receive_packet = 0

	def receive_p(self, packet):
		self.receive += 1
		self.receive_packet += packet

	def drop(self):
		self.drop += 1

	def get_receive(self):
		return self.receive

	def get_drop(self):
		return self.drop

	def get_packet(self):
		return self.receive_packet

