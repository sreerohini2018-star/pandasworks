"""

"""
import pandas as pd
sales_report = [
    {"date": "2026-01-01", "product": "Laptop", "category": "Electronics", "quantity": 2, "price": 55000, "salesperson": "Anil"},
    {"date": "2026-01-01", "product": "Mouse", "category": "Electronics", "quantity": 5, "price": 500, "salesperson": "Meera"},
    {"date": "2026-01-02", "product": "Chair", "category": "Furniture", "quantity": None, "price": 3500, "salesperson": "Rahul"},
    {"date": "2026-01-02", "product": "Desk", "category": "Furniture", "quantity": 1, "price": None, "salesperson": "Rahul"},
    {"date": "2026-01-03", "product": "Pen", "category": "Stationery", "quantity": 20, "price": 10, "salesperson": None},
    {"date": "2026-01-03", "product": "Notebook", "category": "Stationery", "quantity": 10, "price": 50, "salesperson": "Anil"},
    {"date": None, "product": "Printer", "category": "Electronics", "quantity": 1, "price": 12000, "salesperson": "Meera"},
    {"date": "2026-01-04", "product": "Monitor", "category": "Electronics", "quantity": 2, "price": None, "salesperson": "Anil"},
    {"date": "2026-01-05", "product": None, "category": "Furniture", "quantity": 1, "price": 8000, "salesperson": "Rahul"},
    {"date": "2026-01-05", "product": "Table Lamp", "category": None, "quantity": 3, "price": 1500, "salesperson": "Meera"}
]
df=pd.DataFrame(sales_report)
print(df.shape)
print(df.columns)
print(df.head())
print(df.tail())
print(df.info())
print(df.isnull().sum())#is null gives the boolean table and the count of the missing values is given by the sum()
most_frequent_date=df["date"].mode()[0]
df["date"].fillna(most_frequent_date,inplace=True)#fillna-eth value vch fill chynm inplace-illa df thannano modify chyande new vngi false
print(df)
print("===================================")
df["product"].fillna("unknown",inplace=True)
print(df)
print("===================================")
most_frequent_category=df["category"].mode()[0]
df["category"].fillna(most_frequent_category,inplace=True)
print(df)
print(df.isnull().sum())
print("===================================")
average_quantity=df["quantity"].mean()
df["quantity"].fillna(average_quantity,inplace=True)
print(df)
print(df.isnull().sum())
print("===================================")
df["price"].fillna(df["price"].mean(),inplace=True)
print(df)
print(df.isnull().sum())
print("===================================")
#df.dropna(subset=["category"],inplace=True)#to delete the null category row
df["salesperson"].fillna("sree",inplace=True)
print(df)
print(df["category"].value_counts())#salecount by category valuecount-unique count of values 
print("===================================")
print(df["salesperson"].value_counts())#salescount by salesperson
print("===================================")
print(df[(df["category"]=="Electronics") & (df["quantity"]>2)])#category electronics and quantity>2
print("===================================")
print(df.groupby("category")["price"].sum())#category wise revenue of products
print("===================================")
print(df.groupby("category")["quantity"].sum())#category wise etra products sale aayi
print("===================================")
#fillna()-fill null values
#dropna(subset=["coloumname"])-drop rows
#isnull()-chk that column is null or not
#isnull().sum()-null count
#groupby()-group by
#values_count()-return count of unique values
#sort_values()-sorting values
#loc-used to get rows
print(df.sort_values(by="price",ascending=False))
print("===================================")
print(df.loc[2])#or
print("===================================")
print(df.iloc[2])
print("===================================")
#costly product
print(df.iloc[df["price"].idxmax()])
print("===================================")
#cheapest product
print(df.iloc[df["price"].idxmin()])
print("===================================")
#adding new coloumn
df["revenue"]=df["price"]*df["quantity"]
print(df)
print(df.loc[0,["product","category"]])
