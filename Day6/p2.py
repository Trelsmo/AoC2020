# Advent of code Year 2020 Day 6 solution
# Author = Svante Trelsmo
# Date = December 2020


f = open("input.txt","r")

nbr_of_yes = 0
intersec = set()
new_set = True
for x in f:
	line = x.split()
	if line==[]:	# New group
		print(intersec)
		nbr_of_yes += len(intersec)
		intersec = set()
		new_set = True
		
	else:
		if new_set:
			intersec = intersec.union(line[0])
			print(intersec)
		else:
			intersec = intersec.intersection(line[0])
			print(intersec)
		new_set = False

print('Sum of count', nbr_of_yes)