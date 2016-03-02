import pandas as pd 
pd.set_option('display.expand_frame_repr', False)
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

floor_list = [str(flr) + "0" for flr in range(2, 7)]
room_list = []
for floor in floor_list:
	for i in range(7):
		if i !=5:
			room_list.append(floor + str(i))

layout = OrderedDict()

for room in room_list:
	layout[room] = {col_num:get_next_six() for col_num in ["col" + str(num) for num in range(1,10)]}

pprint.pprint(layout, width=1)

# layout_frames = []

# df = pd.DataFrame.from_dict(layout["200"])

# for class_num, column_num in layout.iteritems():
# 	layout_frames.append(pd.DataFrame.from_dict(class_num, orient='index'))
# pprint.pprint(layout)