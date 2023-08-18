# import the "pandas" library
import pandas as pd

# Create pandas series
my_array = [0,1,2,3,4,5,6,7,8,9]
print(my_array)
pandas_series = pd.Series(my_array)
print(pandas_series)

# Create pandas DataFrame
my_array = [0,1,2,3,4,5,6,7,8,9]
print(my_array)
pandas_dataframe = pd.DataFrame(my_array)
print(pandas_dataframe)

# Reading CSV File (Note: Thanks to this function, we can read the data sets on the internet as well as the data sets on our computer.)
data = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
print(data)

# View the first 5 of the data
print(pandas_dataframe.head())

# It shows how many rows and how many columns our dataset consists of.(row,column)
print(data.shape)

# Returns the data size
print(data.size)

# It is used to get information about data.
print(data.info())

#
print(data.loc['John Adams'])

# Show data by index value
print(data.iloc[40])

# Show desired columns
print(data[['order','height']])

# Analyze data that is numerical.
print(data.describe())





