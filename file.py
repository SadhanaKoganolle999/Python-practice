#File handleling in python

#python file handling is used to store the data in a file and retrieve it whenever required.
#types of files
# text files:.txt, .docx, .pdf
# binary files:.exe, .jpg, .mp3, .mp4

#file handling in python is done using built in functions
#open() function is used to open a file
#close() function is used to close a file
#read() function is used to read a file
#write()
#delete()

#Note : all types of files are stored as bits in computer memory. 
# f = open("demo.txt","r") #open a file in read mode
# data= f.read() #read the file
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","r") 
# data=f.read(5)      #read the first 5 characters of the file
# print(data)
# f.close()#open a file in write mode
# f.close() 

# f=open("demo.txt", "r")
# line1 =f.readline() #read the first line of the file
# print(line1)

# line2=f.readline()
# print(line2)

# f.close()

file=open("demo.txt","w")
file.write("hello world")
print("file written successfully")


file =open("demo.txt", "a")
file.write("\n to python ")
file.close()