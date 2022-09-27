file = open("/usercode/files/books.txt", "r")
Lines = file.readlines()
for line in Lines:
    if line.endswith("\n"):
        print(line[0]+str(len(line)-1))  
    else:
        print(line[0]+str(len(line)))  
  

file.close()