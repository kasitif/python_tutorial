from readdata import read_data
from printing import print_comparison
from computation import  compute_windchill

#column name and indices
columns = {'date': 0, 'time': 1, 'tempout':2,'windspeed':7, 'windchill':12 }

#data types for ach cilumn
types = {'tempout':float, 'windspeed':float, 'windchill':float}

#read data fro file
data = read_data(columns, types=types)

#comoute the will chill factor
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))

##output comparison
print_comparison('WINDCHILL', data['date'], data['time'], data['windchill'], windchill)