#!/bin/bash

cd /home/yutaka/research/NPBOS
sh run.sh

# ファイルを１行ずつ読み込む
FILE="./out1.dat"
COL=$(wc -l < "$FILE")

while read LINE ; do
    COL=$(($COL - 1))
    if [ ${COL} -lt 9 ] ; then
        LINE_SUB=$(echo "$LINE" | cut -c7-16)
        if [ "$LINE_SUB" = "2  +  ( 1)" ] ; then
            f_t=$(echo "$LINE" | cut -c23-28)
        elif [ "$LINE_SUB" = "4  +  ( 1)" ] ; then
            f_f=$(echo "$LINE" | cut -c23-28)
        elif [ "$LINE_SUB" = "6  +  ( 1)" ] ; then
            f_s=$(echo "$LINE" | cut -c23-28)
        elif [ "$LINE_SUB" = "0  +  ( 2)" ] ; then
            s_z=$(echo "$LINE" | cut -c23-28)
        fi
    fi
done < "$FILE"

echo ${f_t}
echo ${f_f}
echo ${f_s}
echo ${s_z}

cd ..
