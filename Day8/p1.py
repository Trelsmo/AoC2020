# Advent of code Year 2020 Day 8 solution
# Author = Svante Trelsmo
# Date = December 2020


f = open("input.txt","r")
operation = []
accu = 0

for x in f:
	line = x.split()
	operation.append([line[0],int(line[1]),0])


k=0
while True:
	if operation[k][2] != 0:
		break
	else:
		if operation[k][0] == 'nop':
			operation[k][2] = 1
			k += 1
		elif operation[k][0] == 'acc':
			operation[k][2] = 1
			accu += operation[k][1]
			k += 1
		elif operation[k][0] == 'jmp':
			operation[k][2] = 1
			k += operation[k][1]

print('Accu = ',accu)