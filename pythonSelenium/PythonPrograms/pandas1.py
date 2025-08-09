import pandas as pd

data = [10,20,30,40]
s = pd.Series(data)
print(s)
print(type(s))

print("\n")

data = {'Name' : ["Ram", "Shyam", "Mohan", "Rohan"],
        'Age' : [25,30,40,55],
        'City': ["pune", "hyderabad", "bihar", "Maharashtra"]}

df = pd.DataFrame(data)
print(df)

print("\n")

"""Printing CSV"""

df1 = pd.read_csv("C:/Users/hp/Downloads/testing.csv")
print(df1)

print("\n")

# df1.to_csv("C:/Users/hp/Downloads/testing1.csv", index=False)

"""Printing JSON"""

df2 = pd.read_json("C:/Users/hp/Downloads/abc.json")
print(df2.to_string(),"\n")
print(df2)

print("\n")

"""Printing EXCEL"""

df4 = pd.read_excel("C:/Users/hp/Downloads/testing.xlsx")
print(df4)

print("\n")

print(df4["Name"])

print("\n")

print(df4["Name"][2])
print(df4["Name"][1])

print("\n")

print(df.iloc[1])

print("\n")

print(df[df["Age"]!=30])