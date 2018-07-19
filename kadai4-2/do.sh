#!/bin/sh

echo "write q num: \c"
read num
python main_log_kadai4_2.py < data/q${num}/ad-kadai4-2-${num}.log > data/answer/q${num}/kadai4-2-${num}.txt
mv kadai4.png kadai4-2-${num}.png
mv kadai4-2-${num}.png data/answer/q${num}/

python main_tcp_kadai4_2.py < data/q${num}/ad-kadai4-2-${num}.tcp
mv tcp.png tcp4-2-${num}.png
mv tcp4-2-${num}.png data/answer/q${num}/
