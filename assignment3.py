name = "emily"
print("The original variable is :", name)
size = len(name)-1
i = len(name)-1
rev = ""
for i in range(size,-1,-1):
    rev += name[i]
  
print("The reverse variable is: ",rev)

