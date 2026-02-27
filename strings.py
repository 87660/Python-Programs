# strings are immuatable means we cant change the string
#  but we can make the copy of it and then change its
a="Shreya/>!!"
# full string is converted in upper case
print(a.upper())
# full string is converted in lower case
print(a.lower())
# strip is used to delete all the symbols which are
#  after the name not before the name
print(a.rstrip("!/>"))
# replace will replaces  the charecters with other
#  but keep the symbols as it is
print(a.replace("Shreya","Pathak"))
blogHeading ="introductiOn"
# capitalize method turns the first letter of the string to 
# uppercase and the others letters to uppercase and if it
#  is already in upeercase it will not change
print(blogHeading.capitalize())
str="welcome"
print(len(str))
# center is used to add the space before string
print(str.center(20))
print(len(str.center(20)))
# count counts the letter or word in the given string
print(str.count("e"))
# endswith checks is the string ending with the given symbol or 
# letter and it will give you the boolean output (true or false)
print(a.endswith("!"))
# find will return the index of the letter or word which you 
# want to find and also it starts with 0
print(str.find("o"))