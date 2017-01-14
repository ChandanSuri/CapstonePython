import re
fname = raw_input("Enter the File Name")
fhandle = open(fname)
nums = list()
summ = 0
for line in fhandle:
	nums = re.findall('[0-9]+',line)
	for val in nums:
		summ = summ + int(val)
print summ