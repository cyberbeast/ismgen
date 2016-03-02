import pandas as pd 
import numpy as np
import pprint
from collections import OrderedDict
cse = pd.read_csv('CSE.csv')
ece = pd.read_csv('ECE.csv')

cse_list = cse['CSE 3/4'].tolist() + cse['CSE 5/6'].tolist() + cse['CSE 7/8'].tolist()
ece_list = ece['ECE 3/4'].tolist() + ece['ECE 5/6'].tolist() + ece['ECE 7/8'].tolist()

col_count = 1
count_cse= 0
count_ece= 0

prev = "ece"

def get_next_six():
	global count_cse
	global count_ece
	global prev
	ret = []
	if prev is "ece":
		start = count_cse
		count_cse += 6
		ret = cse_list[start:start+6]
		prev = "cse"
	else:
		start = count_ece
		count_ece += 6
		ret = ece_list[start:start+6]
		prev = "ece"
	return(ret)

layout = OrderedDict()
for i in range(7):
	if i != 5:
		layout["20" + str(i)] = {col_num:get_next_six() for col_num in ["col" + str(num) for num in range(1,10)]}
		layout["30" + str(i)] = {col_num:get_next_six() for col_num in ["col" + str(num) for num in range(1,10)]}
		layout["40" + str(i)] = {col_num:get_next_six() for col_num in ["col" + str(num) for num in range(1,10)]}
		layout["50" + str(i)] = {col_num:get_next_six() for col_num in ["col" + str(num) for num in range(1,10)]}
		layout["60" + str(i)] = {col_num:get_next_six() for col_num in ["col" + str(num) for num in range(1,10)]}

pprint.pprint(layout, width=1)