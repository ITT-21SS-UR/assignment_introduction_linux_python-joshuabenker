#!/usr/bin/python3

"""
**stats.py**: Reads in a list of *floating point numbers*
either from a textfile passed as an argument to the script
or via *stdin*. Numbers are separated by space characters
and may contain either `,` or `.` as decimal separator.
Prints out the mean, median, and standard deviation for these on *stdout*
"""

import sys
import math

# check if input comes from file or stdin
if len(sys.argv) > 1:
    # input via file
    filename = sys.argv[1]
    data = open(filename).read()
else:
    # input via stdn
    print("insert floating numbers:")
    data = sys.stdin.readline()

# replace "," with "."
data = (str(data).replace(",", ".")).split()
data_list_float = list()

for i in data:
    data_list_float.append(float(i))

# calulate mean
sum_of_nums = 0
for i in data_list_float:
    sum_of_nums = sum_of_nums + i

length = len(data_list_float)
mean = sum_of_nums / length

# calculate median
data_list_float.sort()
index = (length -1) // 2

if(length % 2):
    median = data_list_float[index]
else:
    median = (data_list_float[index] + data_list_float[index +1]) /2

# calculate standard deviation
var = 0
for i in data_list_float:
    # calculate variance
    var += ((i - mean) ** 2) / (length -1)
st_dv = math.sqrt(var)

# print out to stdout
sys.stdout.write(
    "The Mean is " + str(mean) +
    "\nThe Median is " + str(median) +
    "\nThe Standard deviation is " + str(st_dv))
