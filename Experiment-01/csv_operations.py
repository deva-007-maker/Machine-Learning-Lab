import pandas as pd
#load csv datset
df=pd.read_csv("students.csv")
#print(df)

#data inspection
'''print(df.head())
print(df.tail())
print(df.info())
print(df.shape)'''

#checking missing values
'''print(df.isnull().sum())'''

#handling missing values using mean imputation
'''df["Maths"].fillna(df["Maths"].mean(),inplace=True)
df["Science"].fillna(df["Science"].mean(),inplace=True)
df["English"].fillna(df["English"].mean(),inplace=True)
print(df.isnull().sum())'''

#adding extra columns total and avg
'''df["Total"]=df["Maths"]+df["Science"]+df["English"]
df["Average"]=df["Total"]/3'''

#add result columns which will consists of either pass or fail basd on average if avg>=50 then add pass otherwise fail
#df["Result"]=df["Average"].apply(lambda x:"Pass" if x>=50 else "Fail")
#print(df.head())

#filter students whose attendance is greater than 90
#print(df[df["Attendance"]>90])

#display names of students whose attendance is greater than 90
#print(df["Name"][df["Attendance"]>90])

#display student ids who are passed
#print(df["Student_ID"][df["Result"]=="Pass"])

#display student ids whose maths marks are greater than english marks
#print(df[       

#find the student ids whose names ends with letter "a"
#print(df["Student_ID"]
#GroupBy
#Calculate avg marks for each student
df["Average"]=df[["Maths", "Science", "English"]].mean(axis=1)
grouped = df.groupby("Average")["Name"].apply(list)
print(grouped)
#Count the no.of students in each subject


