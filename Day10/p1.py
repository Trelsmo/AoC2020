# Advent of code Year 2020 Day 10 solution
# Author = Svante Trelsmo
# Date = December 2020

import numpy as np

f = open("input.txt","r")
tmp = []
for x in f:
	tmp.append(int(x.split('\n')[0]))
tmp.append(0) # add first "dead" outlet
tmp = np.sort(tmp)
diffs = [0,1]	# 1 step diffs, 3 step diffs with the last diff added

for k in range(0,len(tmp)-1):
	diff = tmp[k+1]-tmp[k]

	if diff == 1:
		diffs[0] += 1
	elif diff == 3:
		diffs[1] += 1

print('Ans = 'diffs[0]*diffs[1])