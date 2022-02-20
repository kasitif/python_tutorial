#initaialize my data variable
data = []

#read and parse the data
filename = "data\\wxobs20170821.txt"
with open(filename,'r') as datafile:

    #read the first three line
    for _ in range(3):
        datafile.readline()

# read and parse the rest of the file
    for line in datafile:
        datum = line.split()
        data.append(datum)


