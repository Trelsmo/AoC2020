# Advent of code Year 2020 Day 4 solution
# Author = Svante Trelsmo
# Date = December 2020

import numpy as np
f = open("input.txt","r")
ok_passports=0
entries = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

tmp = []
for x in f:
	line = x.split()
	if line!=[]:	# Same passport
		for entry in line:
			split_2 = entry.split(':')
			tmp.append(split_2[0])
	else:
		if set(entries).issubset(set(tmp)):
			ok_passports +=1
			#print('OK Passport')
		tmp = []

print('Number of approved passports ', ok_passports)