def read_data(columns, types = {}, filename = 'data\\wxobs20170821.txt'):
    """
         
        Read data from CU Boulder Weather Station data file

        Parameters:
            columns: A dictionary of column names mapping to column indices
            types: A dictionary of column names mapping to types to which
                to convert each column of data
            filename: The string path pointing to the CU Boulder Weather
                    Station data file
        
    """

    #initialize the variable
    data = {}
    for column in columns:
        data[column] = []

    #read and Parse data
    with open(filename, "r") as datafile:

        #read the first three lines (headers)
        for _ in range(3):
            datafile.readline()


        #Read and Parse he rest of teh file
        for line in datafile:
            split_line = line.split()
            for column in columns:
                i = columns [column]
                t = types.get(column, str)
                value = t(split_line[i])
                data[column].append(value)

    return data