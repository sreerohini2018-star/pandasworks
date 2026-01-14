
import pandas as pd
salary=[30000,34000,35000,36000]
#series=pd.Series(salary)
#print(series[0])#30000
#print(series[1])#34000
#print(series[1:3])#1    34000
                  #2    35000
series=pd.Series(salary,index=["e1","e2","e3","e4"])#by default index 0,1.. customized index kodkn index=
print(series["e3"])#35000
print(series["e1":"e4"])#e1    30000
                        #e2    34000
                        #e3    35000
                        #e4    36000