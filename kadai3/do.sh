#!/bin/sh

echo "write q num: \c"
read num
python main_log_kadai3.py < data/q${num}/ad-kadai3-${num}.log > data/answer/q${num}/log3-${num}.txt
mv d_packet.png drop-packet3-${num}.png
mv drop-packet3-${num}.png data/answer/q${num}/

python main_tcp_kadai3.py < data/q${num}/ad-kadai3-${num}.tcp
mv tcp.png tcp3-${num}.png
mv tcp3-${num}.png data/answer/q${num}/
