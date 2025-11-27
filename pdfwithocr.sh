#!/bin/bash

pdffile=${1:-input.pdf}
dir=${2:-output}
[[ -d ${dir} ]] || mkdir -pv ${dir}
language=nld
[[ -d source ]] || mkdir -pv source
pdftk $pdffile burst
mv $pdffile source/

for i in *.pdf
do
	echo file=$i
	ocrmypdf -l $language $i ${dir}/$i
done
