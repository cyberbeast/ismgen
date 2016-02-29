import pandas as pd 

cse = pd.read_csv('CSE.csv')
ece = pd.read_csv('ECE.csv')

a1 = cse['CSE 3/4']
a2 = cse['CSE 5/6']
a3 = cse['CSE 7/8']

b1 = ece['ECE 3/4']
b2 = ece['ECE 5/6']
b3 = ece['ECE 7/8']

max_size = max(len(a1.index), len(a2.index), len(a3.index))
max_in_a_column = 6
max_from_one_dept_in_a_class = 30

temp_pd_headers = []
temp_pd_headers.append(cse.columns.values[0])
temp_pd_headers.append(ece.columns.values[0])
# print(temp_pd_headers)
temp_pd = pd.DataFrame(index=range(max_from_one_dept_in_a_class), columns=temp_pd_headers)
# print(temp_pd)


for i in range(0, max_size, max_from_one_dept_in_a_class):
	rows_list = []
	temp_dict = {}
	print("i value is {i}".format(**locals()))
	if (i+6)<=max_size:
		for j in range(i, i+6):
			temp_pd.loc[i] = np.array()
		temp_dict.update({str(temp_pd_headers[0]) : str(a1[i:i+max_from_one_dept_in_a_class])})
		# print(a1[i:i+max_from_one_dept_in_a_class])
	else:
		print(a1[i: i+max_from_one_dept_in_a_class-1])
	rows_list.append(temp_dict)
	print(rows_list)
	# print(pd.DataFrame(rows_list))
	print("STOP")


# print 
# print(len(a1.index))