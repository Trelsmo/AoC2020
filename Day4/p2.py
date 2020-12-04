# Advent of code Year 2020 Day 4 solution
# Author = Svante Trelsmo
# Date = December 2020

import numpy as np
f = open("input.txt","r")
ok_passports=0
ok_field=0
entries = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
byr = [1920,2002]
iyr = [2010,2020]
eyr = [2020,2030]
hgt_cm = [150,193]
hgt_in = [59,76]
ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
hcl = "0123456789abcdef"

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""


tmp = []
tmp2 = []

for x in f:
	line = x.split()
	if line!=[]:	# Same passport
		for entry in line:
			split_2 = entry.split(':')
			tmp.append(split_2[0])
			tmp.append(split_2[1])
	else:
		if set(entries).issubset(set(tmp)):
			for i in range(0,len(tmp),2):

				if (tmp[i] == 'byr') and (len(tmp[i+1])==4): 
					# In interval and consist of Int
					if (int(tmp[i+1]) <= byr[1]) and (int(tmp[i+1]) >= byr[0]):	
						ok_field += 1
						#print('OK BYR')

				elif (tmp[i] == 'iyr') and (len(tmp[i+1])==4): 
					if (int(tmp[i+1]) <= iyr[1]) and (int(tmp[i+1]) >= iyr[0]):
						ok_field += 1
						#print('OK IYR')

				elif (tmp[i] == 'eyr') and (len(tmp[i+1])==4): 
					if (int(tmp[i+1]) <= eyr[1]) and (int(tmp[i+1]) >= eyr[0]):
						ok_field += 1
						#print('OK EYR')

				elif (tmp[i] == 'hgt'): 
					if 'cm' in tmp[i+1]:
						height = tmp[i+1].split('cm')[0]
						if (int(height) <= hgt_cm[1]) and (int(height) >= hgt_cm[0]):
							ok_field += 1
							#print('OK HGT-cm')
					elif 'in' in tmp[i+1]:
						height = tmp[i+1].split('in')[0]
						if (int(height) <= hgt_in[1]) and (int(height) >= hgt_in[0]):
							ok_field += 1
							#print('OK HGT-in')

				elif (tmp[i] == 'hcl') and (tmp[i+1][0] == '#') and (len(tmp[i+1])==7):
						# Check 0-9 or a-f
					hcl_str = tmp[i+1][1:len(tmp[i+1])]
					if hcl.find(hcl_str):
						ok_field += 1
						#print('OK HCL')

				elif (tmp[i] == 'ecl') and (tmp[i+1] in ecl):
					ok_field += 1
					#print('OK ECL')

				elif (tmp[i] == 'pid') and (len(tmp[i+1])==9):
					ok_field += 1
					#print('OK PID')
	
			if ok_field == 7:
				ok_passports +=1
			ok_field=0
		tmp = []
		
print('Number of approved passports ', ok_passports)






