file=open("f2.txt","w")
file.write("abc")
file.close()
file=open("f3.txt","w")
file.write("123")
file.close()
file=open("f2.txt","w")
t=file.write("abc")
file=open("f3.txt","r")
a=file.read()
file=open("f3.txt","w")
b=file.write("abc")

