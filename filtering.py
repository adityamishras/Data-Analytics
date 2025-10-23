import pandas as pd
df = pd.read_excel('students.xlsx', header=0)
result = df[df['Age']>20] # filter students older than 20
if result.empty:
    print("No students older than 20 found.")
else:
    print(result)



programStatus = df[df['ProgramStatus'] == "Dropped"]
print(programStatus)
print("Mail Candidates: ")
Male = df[df['Gender'] == 'M']  # this will show only Male Data
print(Male)

age22NotDropped = df[(df['Age'] == 22) & (df['ProgramStatus'] != "Dropped")]
print(age22NotDropped)

age22NotDropped = df[(df['Age'] == 22) & (df['ProgramStatus'] == "Dropped")]
print(age22NotDropped)

marksabove90 = df[(df['Marks (Python)'] > 90) & (df['Marks (SQL)'] > 90)]
print(marksabove90)
print("--------------------------------------------------")
locationDelhi = df[(df['City'] == "Delhi") & (df['ProgramStatus'] != "Dropped")]
print(locationDelhi)