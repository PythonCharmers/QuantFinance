#!/bin/bash
source activate quant-2.7
for filename in *.ipynb; do
	echo $filename
    jupyter nbconvert --ExecutePreprocessor.kernel_name=python2 --execute --ExecutePreprocessor.timeout=600 "$filename" --output-dir="output" || echo "$filename" >> errors.txt
done
