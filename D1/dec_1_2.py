import pandas as pd
import numpy as np

data = pd.read_csv('expense_report.csv', sep=',',header=None)

data = data.values
data = data[:,0]

sorted_data = np.sort(data)
ans = 0
for i in range(len(sorted_data)):
	n = len(sorted_data)
	j=0
	while(j<n):
		summ = sorted_data[i]+sorted_data[j+1]+sorted_data[n-1]
		if summ < 2020:
			j += 1
		elif summ > 2020:
			n -= 1
		else:
			ans = sorted_data[i]*sorted_data[j+1]*sorted_data[n-1]
			break
	if ans != 0:
		break
print(ans)