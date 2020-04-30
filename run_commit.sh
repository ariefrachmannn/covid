#!/bin/bash
. ~/.bash_profile
#

cd /home/redbit/crawling/covid/
git lfs track "*.csv"
git add .gitattributes
python /home/redbit/crawling/covid/committer.py
