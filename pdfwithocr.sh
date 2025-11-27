#!/bin/bash

pdffile=${1:-input.pdf}
dir=${2:-output}
src=${src:-src}
[[ -d ${dir} ]] || mkdir -pv ${dir}
language=nld
[[ -d $src]] || mkdir -pv $src
pdftk $pdffile burst
mv $pdffile $src/

for i in *.pdf
do
	echo file=$i
	ocrmypdf -l $language --deskew --clean --rotate-pages $i ${dir}/$i
done
