f = open("input.txt","r")
num_of_ok = 0
for x in f:
	row = x.split()
	ind_str = row[0].split('-')
	ind_int = [int(i) for i in ind_str]
	letter = row[1][0]
	pw = row[2]

	if (pw[ind_int[0]-1] == letter) ^ (pw[ind_int[1]-1] == letter):
		num_of_ok +=1
		
print('Number of OK passwords: ', num_of_ok)