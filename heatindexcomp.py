from readdata import read_data
from printing import print_comparison 


# column names and column indices
columns = {'date':0, 'time':1, 'tempout':2, 'humout':5, 'heatindex':13}

# Data types for each column (only if non-string)
types = {'tempout': float, 'humout':float, 'heatindex':float}

#inituialise my data variables
data = {}
for column in columns:
    data[column] = []

##read data from fileread = rea
data = read_data(columns, types=types)


# fucntion calculating wind chill factor
def compute_heatindex(t,rh_pct):
    a = -42.379
    b = 2.04901523
    c = 10.14333127
    d = -0.22475541
    e = -0.00683783
    f = -0.05481717
    g = 0.00122874
    h = 0.00085282
    i = -0.0000019

    rh =rh_pct / 100

    hi = a + (b * t) + (c * rh) + (d * t * rh)
    + (e * t**2) + (f * rh**2) + (g * t**2 * rh)
    + (h * t * rh**2) + (i * t**2 * rh**2)


    return hi


##comout wind chill
heatindex = []
for temp, hum in zip(data['tempout'], data['humout']):
    heatindex.append(compute_heatindex(temp,hum))
    
    
#     #Debug
# for wc_data, wc_comp in zip(data['windchill'], windchill):
#     print (f'{wc_data:.5f} {wc_comp:.5f} {wc_data-wc_comp:.5f}')

## Output comparison
print_comparison('Heat IDX', data['date'], data['time'], data['heatindex'], heatindex)