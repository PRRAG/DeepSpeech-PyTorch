#!/bin/bash

for i in {1..47}
do
	fileid=40-$i-1
	python transcribe.py --model-path 30-6-2019/deepspeech.pth --audio-path 26-6-2019/records_feby/$fileid.wav --out_trans_path 26-6-2019/trans_40_out-1/$fileid.txt --decoder "beam" --lm-path lm
	#python transcribe.py --model-path 30-6-2019/deepspeech.pth --audio-path 26-6-2019/records_feby/$fileid.wav --out_trans_path 26-6-2019/trans_40_out/$fileid.txt
done
