import pandas as pd

df = pd.read_excel('students.xlsx', header=0)
print(df)

#operations on Dataframe can be performed here -- e.g., filtering, grouping, etc.
#1. Basic Exploration
print(df.head())        # Pehle 5 rows dikhaega
print(df.tail())        # Last 5 rows
print(df.shape)         # rows, columns
df.info()               # Column names, datatypes
print(df.describe(include='all'))    # Numerical columns ka summary (mean, std, etc.)

#2. Filtering Data
print(df['Name'])   #only Name Column
print(df['Mobile Number'])