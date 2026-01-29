import pandas as pd
#load csv datset
df=pd.read_csv("students.csv")
#GroupBy
#Calculate avg marks for each student
avg_marks = df.groupby("Name")[["Maths", "Science", "English"]].mean()
print(avg_marks)
