# seek method allows you to move current position within a file to specific point.
#f.seek(10)
with open('myfile.txt','r') as f:
    print(type(f))
    # move to the 10th byte in the file
    f.seek(15)

    # read the next 5 bytes
    data= f.read(9)
    print(data)
