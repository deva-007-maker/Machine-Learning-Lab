import pandas as pd
#print(pd.__version__)
'''a=[10,20,30]
s=pd.Series(a)
print(s)'''

#create label with index arguments
'''a=[10,20,30]
s=pd.Series(a,index=['x','y','z'])
print(s['z'])'''

#creating a series with key,value objects
'''d={"d1":200,"d2":300,"d3":400}
s=pd.Series(d)
print(s)'''

#create a series with only data from d1 and d2
'''k=pd.Series(d,index=["d1","d2"])
print(k)'''

#Dataframes
#create a dictionary named as data
'''data={"a":[10,20,30],"b":[40,50,60]}
df=pd.DataFrame(data)
print(df)'''

#locating the rows using loc attribute it return one or more specified 
'''print(df.loc[0])
print(df.loc[0:2])
df=pd.DataFrame(data,index=["x","y","z"])
print(df)
print(df.loc[::2]["b"])'''

