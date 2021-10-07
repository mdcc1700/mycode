#!/usr/bin/env python3
# for-loop
import os

forloop = [1,2,3]
for x in forloop:
    print("x: {}".format(x))

for counter in range(3):
    os.system("date")

# while-loop
y = 0
while y < 5:
    print("y: {}".format(y))
    y += 1 # same as y = y+1
