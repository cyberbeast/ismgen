import pandas as pd 
pd.set_option('display.expand_frame_repr', False)
import math
import pprint
from collections import OrderedDict
import sys, getopt
import openpyxl

def get_next_six():
	global count_host
	global count_guest
	global prev
	ret = []
	if prev is "guest":
		start = count_host
		count_host += 6
		ret = host_list[start:start+7]
		if not ret:
			return([float('nan') for i in range(7)])
		prev = "host"
	else:
		start = count_guest
		count_guest += 6
		ret = guest_list[start:start+7]
		if not ret:
			return([float('nan') for i in range(7)])
		prev = "guest"
	return(ret)

try:
	opts, args = getopt.getopt(sys.argv[1:],"h:g:", ["hostfile=","guestfile="])
except getopt.GetoptError:
	print('ismgen.py -h <hostfile> -g <guestfile>')
	sys.exit(2)

for opt, arg in opts:
	if opt in ("-h", "--hostfile"):
		host = pd.read_csv(arg)
	elif opt in ("-g", "--guestfile"):
		guest = pd.read_csv(arg)

host_list = host['3/4'].tolist() + host['5/6'].tolist() + host['7/8'].tolist()
guest_list = guest['3/4'].tolist() + guest['5/6'].tolist() + guest['7/8'].tolist()

prev="guest"
col_count = 1
count_host= 0
count_guest= 0

floor_list = [str(flr) + "0" for flr in range(2, 7)]
room_list = []
for floor in floor_list:
	for i in range(7):
		if i !=5:
			room_list.append(floor + str(i))

layout = OrderedDict()
layout_frames = []

for room in room_list:
	layout[room] = {col_num:get_next_six() for col_num in ["col" + str(num) for num in range(1,10)]}
	layout_frames.append(pd.DataFrame({k : pd.Series(v) for k, v in layout[room].items()}).fillna('----------'))
	layout_frames[-1].index.name = str(room)
	
pprint.pprint(layout_frames)

pprint.pprint(layout_frames[0].values.tolist())

wb = openpyxl.load_workbook('generated.xlsx')
wb.create_sheet("200")
sheet = wb.get_sheet_by_name('200')
sheet['B7'] = '1PE11CS200'

