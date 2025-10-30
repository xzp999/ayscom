#!/bin/bash
cut -d',' -f1,3 copia/sales.csv
echo ""
awk -F',' '{print $1, $3}' copia/sales.csv
echo ""
grep "Shoes" copia/sales.csv