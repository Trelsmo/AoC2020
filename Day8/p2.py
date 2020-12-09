# Advent of code Year 2020 Day 8 solution
# Author = Svante Trelsmo
# Date = December 2020


f = open("test.txt","r")
operation = []
accu = 0

for x in f:
	line = x.split()
	operation.append([line[0],int(line[1]),0,0])	# instruction, inc or jump val, has been used, times flipped

k=0
last_flip = -1

unchange_operation = operation

while 0 <= k < len(operation):
	print(operation[k])

	# FLIP INSTRUCTION
	if operation[k][3] < 1:	# Flip k once
		print('flip')
		if operation[k][0] == 'nop' and operation[k][1] != 0:
			operation[k][0] = 'jmp'
			last_flip=k
			operation[k][3] += 1
		elif operation[k][0] == 'jmp':
			operation[k][0] = 'nop'
			last_flip=k
			operation[k][3] += 1
		print(operation[k])
	# END FLIP INSTRUCTION

	# REVERSE FLIP
	if  operation[k][2] != 0 and last_flip != -1:	# If not executed([k][2] != 0) change back 
		operation = unchange_operation
		operation[last_flip][3] = 1
		k=0
		accu = 0
		last_flip = -1
	# END REVERSE FLIP

	# EXECUTE INSTRUCTION
	if operation[k][0] == 'nop':
		operation[k][2] = 1
		k += 1
	elif operation[k][0] == 'acc':
		accu += operation[k][1]
		print(accu,operation[k][1])
		operation[k][2] = 1
		k += 1
	elif operation[k][0] == 'jmp':
		operation[k][2] = 1
		k += operation[k][1]
	# END EXECTUE INSTRUCTION

print('Accu = ',accu)
