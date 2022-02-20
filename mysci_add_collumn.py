## Initaialize the data
data = {'date' : [],
        'time': [],
        'tempout': []}


# Read and Parse the data
filename = 'data\\wxobs20170821.txt'
with open(filename, 'r') as datafile:

    ##read the firth three lines(headers)
    for _ in range(3):
        datafile.readline()


    #read and parse the rest of the file
    for line in datafile:
        split_line = line.split()
        data['date'].append(split_line[0])
        data['time'].append(split_line[1])
        #change the line to float
        data['tempout'].append(float(split_line[2]))

## convert the data to float

##Debug
print(data['tempout'])

    