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
