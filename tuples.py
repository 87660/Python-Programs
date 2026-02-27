# tuple cannot change after making
# t=(1,5,8)
# t[0]=9   #'tuple' object does not support item assignment
# print(t)
# print(type(t),t)   #type with the tuple element
# to add elemtnt in the tuple we convert it to list then change as per the requirement and then we convert it to new tuple 
# temp = list(t)
# temp.append(9)   # added 9 in the end of list
# temp[0]=3   # index 0 element is changed to 3
# t=tuple(temp)
# print(t)

# tup=("Shreya","Swara","Shraddha")
# tuple=("Sakshi","Aditi")
# tnew=tup + tuple  #concatination of 2 tuples
# print(tnew)
