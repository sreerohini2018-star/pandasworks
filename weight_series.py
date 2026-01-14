
import pandas as pd
data=[35,40,55,75,90,15,25,40,62,45]
weight=pd.Series(data)
print(weight)
#0    35
#1    40
#2    55
#3    75
#4    90
#5    15
#6    25
#7    40
#8    62
#9    45
#dtype: int64

print(weight.tail())
#5    15
#6    25
#7    40
#8    62
#9    45
#dtype: int64

print(weight.head())
#0    35
#1    40
#2    55
#3    75
#4    90
#dtype: int64

print(weight.shape)#(10,) shape is an attribute

"""
if we have 100 records we use
methods:-
head()-list top 5 records
tail()-list last 5 records
"""