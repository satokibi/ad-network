#!/bin/sh

echo "write q num: \c"
read num
python main_log_kadai5.py < data/q2/sub_flow${num}/ad-kadai5_2_${num}.log > data/answer/q2/sub_flow${num}/kadai5_2_${num}.txt
mv kadai5.png kadai5_2_${num}.png
mv kadai5_2_${num}.png data/answer/q2/sub_flow${num}/
