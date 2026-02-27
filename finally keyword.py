try:
    l=[1,2,3,4,5]
    i=int(input("Enter the index:"))
    print(l[i])

except:
    print("Error occured!")

finally:
    print("Code executed")