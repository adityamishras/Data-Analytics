import pandas as pd

student = {
 'Name': ['Alice', 'Bob', 'Charlie', 'David'],
 'Age' : [24, 23, 27, 22], 
 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(student)
print(df)