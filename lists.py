
#list can change after making
# if the list is of numbers we can add alphabets as well
marks =[10,4,6,8,9,90,64,908]
# print(type(marks))
# print(marks[0])
# # error will be occured when the element is not in the list
# # print(marks[5])

# print(marks[0:3])  # if we want marks from 0 to index 3 
# print(marks[1:8:2])  # if we want marks from index 1 to 8 with jump of 2
print(marks)


# marks.append(79)   # append is used to add element in the end of the list
# marks.sort()  # sort function will sort the list in ascending order 
# marks.sort(reverse=True)  # this will sort in decending order
marks.reverse()
print(marks)
