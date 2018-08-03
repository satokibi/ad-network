#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from models6 import Queue, Node, PacketLog
import matplotlib.pyplot as plt

class Pacloss():
    def __init__(self):
        self.num = 0
        self.num_list = []
        self.time_list = []


if __name__ == '__main__':

    args = sys.argv
    line = raw_input()
    los4_num = 0
    los5_num = 0
    r4_num = 0
    r5_num = 0

    s = []
    for i in range(int(args[1])):
        s.append(Pacloss())

    while line:
        ls = line.split()
        log = PacketLog(ls[0], ls[1], ls[2], ls[3], ls[4], int(ls[5]), ls[6], ls[7], ls[8], ls[9], ls[10], ls[11])

        if log.event == 'd':
            src = log.src_port.split('.')[0]
            port = int(log.src_port.split('.')[1])
            if src == '0':
                los4_num += 1
            elif src == '1':
                los5_num += 1
                s[port].num += 1
                s[port].num_list.append(s[port].num)
                s[port].time_list.append(log.time)

        if log.event == 'r':
            if log.link_dst == '4':
                r4_num += 1
            elif log.link_dst == '5':
                r5_num += 1

        try:
            line = raw_input()
        except EOFError:
            break

    print('node4宛のパケットロス : ' + str(los4_num))
    print('node5宛のパケットロス : ' + str(los5_num))
    print('node4が受け取ったパケット数 : ' + str(r4_num))
    print('node5が受け取ったパケット数 : ' + str(r5_num))

    fig = plt.figure(figsize=(12, 12))
    axs = []
    axs2 = []

    for i in range(len(s)):
        axs.append(fig.add_subplot((len(s)+1)/2, 2, i+1))
        axs[i].plot(s[i].time_list, s[i].num_list, label='loss num')
        axs[i].set_xlabel('Time (sec)')
        axs[i].set_ylabel('packet loss num')

    plt.savefig('kadai6t.png')
    plt.show()
