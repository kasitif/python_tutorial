from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_heastindex

### column names
columns = {'date':0, 'time': 1, 'tempout':2, 'humout':5, 'heatindex':13}

#data types for each column 
types = {'tempout':float, 'humout':float, 'heatindex':float}

#readdata fromfile
data = read_data(columns, types=types)

#compute heat index
heatindex =[]
for temp, hum in zip(data['tempout'], data['humout']):
    heatindex.append(compute_heastindex(temp, hum))

#print out
print_comparison('Heat IDX', data['date'], data['time'],data['heatindex'], heatindex)
