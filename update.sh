#!/bin/sh
time_spot = 'date + %d%H%M'
git remote remove lclc
git remote add lclc https://github.com/zhucebuliaolongchuan/lclc.git
git pull lclc master --allow-unrelated-histories
git add *
git commit -m "updated myLeetcode on 'date + %d%H%M'"
git push lclc master
