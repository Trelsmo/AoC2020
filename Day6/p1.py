# Advent of code Year 2020 Day 6 solution
# Author = Svante Trelsmo
# Date = December 2020


f = open("input.txt","r")

nbr_of_yes = 0
intersec = set()
for x in f:
	line = x.split()
	if line==[]:	# New group
		nbr_of_yes += len(intersec)
		intersec = set()
	else:
		intersec = intersec.union(line[0])

print('Sum of count', nbr_of_yes)