import pandas as pd
data1= {'name';['ram','shyam','jack','steve'],'age':[28,34,65,78]}
data2={'name':'jack','age':34}
df1=pd.dataFrame(data1)
df2 =pd.dataFrame(data2,index=[4])
print(df1.append(df2))