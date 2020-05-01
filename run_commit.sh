#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
export DISPLAY=:0.0
. ~/.bash_profile
#

cd /home/redbit/crawling/covid/
git lfs track "*.csv"
git add .gitattributes
git add .
git commit -m "Update repository"
git push

echo DONE
