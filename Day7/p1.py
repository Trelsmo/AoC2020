# Advent of code Year 2020 Day 7 solution
# Author = Svante Trelsmo
# Date = December 2020

import re
import math

f = open("input.txt","r")
my_bag = ["shiny gold"]
bags = []

for x in f:
	line = x.split(' ')

	for k in range(0,len(line)-3,4):
		if k == 0:
			bags.append(':'+line[k]+' '+line[k+1])
		else:
			bags.append(line[k+1]+' '+line[k+2])
	for tmp in range(2):
		for bag in bags:
			if bag[0] == ':':
				top_bag = bag
			else:
				if bag in my_bag:
					my_bag.append(top_bag[1:])
					
print(len(set(my_bag)))

