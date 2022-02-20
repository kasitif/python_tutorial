import sys, types, os;
# read the data
#filename = "data\\wxobs20170821.txt"
#datafile = open(filename,'r')


# print(datafile.readline())
# print(datafile.readline())
# print(datafile.readline())
# print(datafile.readline())

# data = datafile.read()
# datafile.close()

# #Debug
# print(data)
# print ("data")

## clean way of reading data
filename = "data\\wxobs20170821.txt"
with open(filename,'r') as datafile:
    data =datafile.read()

#Debug
print(type(data))