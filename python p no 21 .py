
with open("myfile.txt", "w") as file:
  file.write("India is a South Asian country,\
  the world's seventh-largest in land area and \
  second-most populous, with a rich and diverse culture")

fileptr = open("myfile.txt","r")
if fileptr:
  print("file is opened successfully")
  content1 = fileptr.read()  #read all characters
  print("The first read of the file is:",content1)
  content2 = fileptr.read(10)  #read 10 characters
  print("The second read of the file is:",content2)
  content3 = fileptr.read(5)  #read 5 characters
  print("The third read of the file is:",content3)
else:
  print("file not opened ")
fileptr.close();