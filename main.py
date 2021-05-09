import math
import openpyxl as pyxl
import pandas as pd

data = pd.read_excel(r"C:\Develop\WorkSpace\Aarya\Programming Files\Python Tree\database.xlsx")
name = pd.DataFrame(data, columns = ["name"])
send = pd.DataFrame(data, columns = ["send"])
receive = pd.DataFrame(data, columns = ["receive"])
#print(name) #printing dataframe
#print(send) #printing another dataframe

namedict = name.to_dict(orient="dict")
#print(type(namedict)) #<class 'dict'>
#print(namedict) #dataframe
senddict = send.to_dict(orient="dict")
#print(type(senddict)) #<class 'dict'>
#print(senddict) #dataframe
receivedict = receive.to_dict(orient="dict")

namelist = []
sendlist = []
receivelist = []

for key,value in namedict.items():
    print(key,value) #printing the key then the value
    for i in value.values():
        namelist.append(i)

for key,value in senddict.items():
    print(key,value) #printing the key then the value
    for i in value.values():
        
        sendlist.append(i) 

for key,value in receivedict.items():
    print(key,value) #printing the key then the value
    for i in value.values():
        
        receivelist.append(i) 
print(namelist) #printing the name list
print(sendlist) #printing the send
print(receivelist)

tree = []
treedict = {
    
}

def rec(index):
    return receivelist[index]

def sen(index):
    return sendlist[index]

def maketreedict():
    i = 0
    while i < len(namelist):
        j = 0
        temp = []
        while j < len(namelist):
            
            if (sen(i) == rec(j)):
                #make j a child of i
                temp.append(j)
            else:
                pass
            j += 1
        treedict[i] = temp
        i += 1
    print(treedict)
    print(namelist)

def getchildrenof(key):
    if (len(treedict.get(key)) > 0):
        return treedict.get(key)
    else:
        return "No children"
maketreedict()
