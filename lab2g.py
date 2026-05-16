#!/usr/bin/env python3

#Author: Lazuli Barba Reancont
#Author ID: 105983225
#Date Created: 2026/05/16

import sys


if(len(sys.argv)) == 2:
    timer = int(sys.argv[1])
else: 
    timer = 3

while timer != 0:
    print(timer)
    timer = timer - 1
print("blast off!")

