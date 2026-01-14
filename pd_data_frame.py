
"""
Dataframe is like 2d array in numpy with rows and coloums
"""
import pandas as pd
students={
    "name":["adhnan","adhil","risen","rafi","jibin"],
    "age":[23,21,25,26,25],
    "course":["ds","ds","dj","st","ds"]
}
df=pd.DataFrame(students)
print(df)#     name    age   course
          #0  adhnan   23     ds
          #1   adhil   21     ds
          #2   risen   25     dj
          #3    rafi   26     st
          #4   jibin   25     ds
print(df[1:2])   #   name   age   course
                #1  adhil   21     ds       
print(df["course"])
print(df[["name","age"]])                