#!/bin/sh
time_spot = date
git remote remove lclc
git remote add lclc https://github.com/zhucebuliaolongchuan/lclc.git
git pull lclc master --allow-unrelated-histories
git add *
git commit -m "updated myLeetcode on $date"
git push lclc master
