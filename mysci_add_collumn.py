# ## Initaialize the data
# data = {'date' : [],
#         'time': [],
#         'tempout': []}


# # Read and Parse the data
# filename = 'data\\wxobs20170821.txt'
# with open(filename, 'r') as datafile:

#     ##read the firth three lines(headers)
#     for _ in range(3):
#         datafile.readline()


#     #read and parse the rest of the file
#     for line in datafile:
#         split_line = line.split()
#         data['date'].append(split_line[0])
#         data['time'].append(split_line[1])
#         #change the line to float
#         data['tempout'].append(float(split_line[2]))

# ## convert the data to float

# ##Debug
# print(data['tempout'])

## column names and column indices
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

# Data types for each column (only if non-string)
types = {'tempout': float, 'windspeed':float, 'windchill':float}

#inituialise my data variables
data = {}
for column in columns:
    data[column] = []



#Reand Parse the data
filename = 'data\\wxobs20170821.txt'
with open(filename,'r') as datafile:

    ##read the firth three lines(headers)
    for _ in range(3):
        datafile.readline()


    #Read and Parse the rest of the file
    for line in datafile:
        split_line =line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column,str)
            value =t(split_line[i])
            data[column].append(value)

# fucntion calculating wind chill factor
def compute_windchil(t,v):
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    v2 = v**2
    wci = a + (b * t) - (c * v2) + (d * t * v2)

    return wci


##comout wind chill
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchil(temp,windspeed))
    
    
#     #Debug
# for wc_data, wc_comp in zip(data['windchill'], windchill):
#     print (f'{wc_data:.5f} {wc_comp:.5f} {wc_data-wc_comp:.5f}')

## Output comparison
print ("                    Original Computed")
print('  dATE tIME wINDCHILL wIndschill Difference')
print (' --------------------------------------------')
zip_data = zip(data['date'],data['time'], data['windchill'],windchill)
for date, time, wr_org, wc_comp in zip_data:
    wc_diff = wr_org - wc_comp
    print (f'{date} {time :.6} {wr_org:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')