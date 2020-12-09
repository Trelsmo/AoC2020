# Advent of code Year 2020 Day 9 solution
# Author = Svante Trelsmo
# Date = December 2020


f = open("input.txt","r")
pre_len = 26
i = pre_len
tmp = []

for x in f:
	tmp.append(int(x))

diff = [tmp[i]-a for a in tmp[i-pre_len:i]]

while any([k in tmp[i-pre_len:i-1] for k in diff]):
	i+=1
	diff = [tmp[i]-a for a in tmp[i-pre_len:i]]

print('Missing = ',tmp[i])

k=0
summ = tmp[0]
j = 0
while True:
	if summ < tmp[i]:
		summ += tmp[k]
		k += 1
	elif summ > tmp[i]:
		j += 1
		k = j+1
		summ = tmp[j]
	else:
		break

print('Continous set ',tmp[j:k])
print('Weakness = ', (min(tmp[j:k])+max(tmp[j:k])))