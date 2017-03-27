#!/bin/sh
time_spot=`date "+%Y-%m-%d %H:%M:%S"`
git remote remove lclc
git remote add lclc https://github.com/zhucebuliaolongchuan/lclc.git
git pull lclc master --allow-unrelated-histories
git add *
git commit -m "updated on ${time_spot}"
git push lclc master
