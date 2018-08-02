#!/bin/sh

echo "write q num"
read num
python main_log_kadai6.py ${num} < data/q2/sub_flow${num}/ad-kadai6_2_${num}.tcp > data/answer/q2/sub_f${num}/kadai6t${num}.txt
mv kadai6t{,$num}.png
mv kadai6t${num}.* data/answer/q2/sub_f${num}/
