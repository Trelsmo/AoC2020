# Advent of code Year 2020 Day 3 solution
# Author = Svante Trelsmo
# Date = December 2020


f = open("input.txt","r")

nbr_of_trees = 0
i=0

for x in f:
	ind = i % (len(x)-1)
	if x[ind] == ".":
		x = x[: ind] + "O" + x[ind + 1:] 
	elif x[ind] == "#":
		nbr_of_trees +=1
		x = x[: ind] + "X" + x[ind + 1:] 
	i+=3


print("Number of trees = ", nbr_of_trees)
	
	