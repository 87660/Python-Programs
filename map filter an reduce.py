def cube(x):
    return x*x*x

print(cube(2))
 
 # created a list and taken the cube of all elements from list at same time
l=[2,3,4,5]
# newl=[]
# for item in l:
#     newl.append(cube(item))
# print(newl)


#map
newl =list(map(cube , l))
print(newl)
