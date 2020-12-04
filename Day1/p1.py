# Advent of code Year 2020 Day 1 solution
# Author = Svante Trelsmo
# Date = December 2020

import pandas as pd
import numpy as np

data = pd.read_csv('expense_report.csv', sep=',',header=None)
data = data.values
data = data[:,0]

sorted_data = np.sort(data)

done = False
i = 1
j = len(sorted_data)-1
print(sorted_data)
while i<j:
	summ = sorted_data[i]+sorted_data[j]
	if(summ==2020):
		break
	elif(summ<2020):
		i+=1
	j-=1	
print(sorted_data[i],sorted_data[j])
print('Multiplied value = ', sorted_data[i]*sorted_data[j])


