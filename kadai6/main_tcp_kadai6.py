#!/usr/bin/python
# -*- Coding: utf-8 -*-

import sys
from models6 import *
import matplotlib.pyplot as plt


class Flow():
    def __init__(self, port):
        self.x_time = []
        self.y_cwnd = []
        self.y_ssthresh = []
        self.y_seqno = []

        self.logs = []

    def append_log(self, log):
        self.x_time.append(float(log.time))
        self.y_cwnd.append(float(log.cwnd))
        self.y_ssthresh.append(int(log.ssthresh))
        self.y_seqno.append(int(log.seqno))

        self.logs.append(log)


if __name__ == '__main__':

    line = raw_input()
    x_time = []
    y_cwnd = []
    y_ssthresh = []
    y_seqno = []

    flows = []
    args = sys.argv

    for i in range(int(args[1])):
        flows.append(Flow(i))

    while line:
        ls = line.split()
        log = TcpLog(ls[1], ls[3], ls[5], ls[7], ls[9], ls[11], ls[13], ls[15], ls[17], ls[19], ls[21], ls[23], ls[25], ls[27], ls[29])

        for i in range(len(flows)):
            if log.sport == str(i):
                flows[i].append_log(log)

            x_time.append(float(log.time))
            y_cwnd.append(float(log.cwnd))
            y_ssthresh.append(int(log.ssthresh))
            y_seqno.append(int(log.seqno))
        try:
            line = raw_input()
        except EOFError:
            break

    fig = plt.figure(figsize=(12, 12))
    axs = []
    axs2 = []

    for i in range(len(flows)):
        print(' - - - - - - - - - - - - - - -')
        if str(i) == flows[i].logs[0].sport:
            for l in flows[i].logs:
                print('port: ' + l.sport + ', time: ' + l.time + ', seqno: ' + l.seqno)

    for i in range(len(flows)):
        axs.append(fig.add_subplot((len(flows)+1)/2, 2, i+1))
        axs[i].plot(flows[i].x_time, flows[i].y_cwnd, label='cwnd')
        axs[i].plot(flows[i].x_time, flows[i].y_ssthresh, label='ssthresh')
        axs[i].set_xlabel('Time (sec)')
        axs[i].set_ylabel('cwnd, ssthresh')

        ax2 = axs[i].twinx()

        ax2.plot(flows[i].x_time, flows[i].y_seqno, color='red', label='seqno')
        ax2.set_ylabel('Sequence Number', color='red')
        ax2.axis(xmin=0, xmax=25)

        # axs2.append(axs[i].twinx())

        # axs2[i].plot(flows[i].x_time, flows[i].y_seqno, color='red', label='seqno')
        # axs2[i].set_ylabel('Sequence Number', color='red')
        # axs2[i].axis(xmin=0, xmax=25)

        # ax1.legend(bbox_to_anchor=(0,1),loc='upper left')
        # ax2.legend(bbox_to_anchor=(0,0.85),loc='upper left')

    plt.savefig('kadai6t.png')
    plt.show()
