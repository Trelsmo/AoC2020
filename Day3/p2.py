# Advent of code Year 2020 Day 3 solution
# Author = Svante Trelsmo
# Date = December 2020


down = [1,1,1,1,2]
steps_right = [1,3,5,7,1]
mult = 1
for ind_a in range(len(steps_right)):

	steps = steps_right[ind_a]
	steps_down = down[ind_a]
	nbr_of_trees = 0
	f = open("input.txt","r")
	i=0
	mod_var = 1

	for x in f:
		if steps_down == 2 and (mod_var % 2) == 0:
			pass	
		else:
			ind = i % (len(x)-1)
			if x[ind] == "#":
				nbr_of_trees +=1
			i += steps
		mod_var += 1
	mult *= nbr_of_trees
	print(nbr_of_trees)

print("Multiplied trees = ", mult)