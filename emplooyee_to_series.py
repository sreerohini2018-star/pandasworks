
import pandas as pd
emplooyee={"e1":12000,"e2":2500000,"e3":50000,"e4":100000}
series=pd.Series(emplooyee)
print(series)#e1      12000
             #e2    2500000
             #e3      50000
             #e4     100000
print(series["e3"])#50000
print(series.sum())#2662000
print(series.max())#2500000
print(series.min())#12000
print(series.median())#75000.0



"""
aggregate fun():-
sum()
max()
min()
mean()
"""
