from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import  compute_dewpoint

#column name and indices
columns = {'date': 0, 'time': 1, 'tempout':2,'humout':5, 'dewpt':6 }

#data types for ach cilumn
types = {'tempout':float, 'humout':float, 'dewpt':float}

#read data fro file
data = read_data(columns, types=types)

#comoute the will chill factor
# windchill = []
# for temp, windspeed in zip(data['tempout'], data['windspeed']):
#     windchill.append(compute_windchill(temp, windspeed))

dewpointtemp = [compute_dewpoint(t,h) for t, h in zip(data['tempout'], data['humout'])]
##output comparison
print_comparison('DEW PT', data['date'], data['time'], data['dewpt'], dewpointtemp)