#!/bin/sh
echo "Exporting data..."
cqlsh -f scripts/3-export-data2csv.sql
echo "Spliting file"
split -l100000 data/person-out.csv split_person_
mv split_person* data/
rm data/person-out.csv