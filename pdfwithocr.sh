#!/bin/bash

dir=${1:-~/recepten.ocr}
[[ -d ${dir} ]] || mkdir -pv ${dir}
language=nld

for i in *.pdf
do
	echo file=$i
	ocrmypdf -l $language $i ${dir}/$i
done
