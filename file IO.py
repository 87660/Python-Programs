# file IO will open another file in this program
f=open('myfile.txt','r')
# print(f)
text= f.read()
print(text)
f.close()