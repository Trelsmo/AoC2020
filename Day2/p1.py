f = open("input.txt","r")
num_of_ok = 0

for x in f:
	row = x.split()
	min_max_str = row[0].split('-')
	min_max_int = [int(i) for i in min_max_str]
	letter = row[1][0]
	num_occur = row[2].count(letter)
	if num_occur >= min_max_int[0] and num_occur <= min_max_int[1]:
		num_of_ok += 1

print('Number of OK passwords: ', num_of_ok)
	