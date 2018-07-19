#!/bin/sh

echo "write q num: \c"
read num
python main_log_kadai4.py < data/q${num}/ad-kadai4-1-${num}.log > data/answer/q${num}/kadai4-1-${num}.txt
mv kadai4.png kadai4-1-${num}.png
mv kadai4-1-${num}.png data/answer/q${num}/

