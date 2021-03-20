import os
import sys
import math
from collections import OrderedDict 
map1 = {}
Rintermediate = 1
Sintermediate = 1
rcount = 0
scount = 0
fpp = "ranjan"
fpp1 = "ranjan"
Rhash = []
Shash = []
splitsofR = 0
splitsofS = 0

def my_sort1(line):
    line_fields = line.strip().split(' ')
    return line_fields[1]

def my_sort0(line):
    line_fields = line.strip().split(' ')
    return line_fields[0]

def sortfile1(file1):
    reversefile = file1[::-1]
    filename = reversefile.split("/")[0]
    fp = open(file1)
    values = fp.readlines()
    values.sort(key = my_sort1)
    fp1 = open(filename,'w+')
    count = 0
    for lines in values:
        fp1.write(lines)
        count += 1
    #print("R",count)
    fp1.close()
    return filename

def sortfile2(file2):
    global splitsofS
    reversefile = file2[::-1]
    filename = reversefile.split("/")[0]
    fp = open(file2)
    values = fp.readlines()
    values.sort(key = my_sort0)
    fp1 = open(filename,'w+')
    count = 0
    for lines in values:
        fp1.write(lines)
        count += 1
    
    #print("S", count)
    fp1.close() 
    return filename

def opensort1(filename1,mainmemory):
    global splitsofR
    mainmemory = mainmemory*100
    intermediatefiles = 0
    count = 0
    fp = open(filename1,'r')
    fpp = open("R"+str(intermediatefiles)+".txt",'w+')
    for line in fp:
        fpp.write(line)
        count += 1
        if count == mainmemory:
            intermediatefiles += 1
            fpp.close() 
            fpp = open("R"+str(intermediatefiles)+".txt",'w+')
            count = 0

    fp.close()
    splitsofR = intermediatefiles + 1
    #print("No of inter R", splitsofR) 

def opensort2(filename2,mainmemory):
    global splitsofS
    mainmemory = mainmemory*100
    intermediatefiles = 0
    count = 0
    fp = open(filename2,'r')
    fpp = open("S" + str(intermediatefiles)+".txt",'w+')
    for line in fp:
        fpp.write(line)
        count += 1
        if count == mainmemory:
            intermediatefiles += 1
            fpp.close()
            fpp = open("S"+str(intermediatefiles)+".txt",'w+')
            count = 0
    fp.close()
    splitsofS = intermediatefiles + 1
    #print("No of inter S", splitsofS)

def getnext(finalOutputFile, mainmemory):
    global map1 
    global Rintermediate 
    global Sintermediate 
    global rcount 
    global scount 
    global Rindex 
    global Sindex
    global splitsofR
    global splitsofS
    global fpp
    global fpp1
    
    #print(map1)  
    if(len(map1) == 0):
        return 0
    dict1 = OrderedDict(sorted(map1.items()))
    map1 = dict1
    tot =  list(map1.keys())[0]
    Rpart = []
    Spart = []
    Rcounter  = 0
    Scounter = 0

    while(True):
        #print("AG")
        if(len(map1) == 0):
            #print("size break")
            break
        tot1 = list(map1.keys())[0]
        if(tot1 != tot):
            #print("tot break")
            break
        temp = map1[tot1]
        #print(temp)
        i = 0

        while(i<len(temp)):
            val = temp[i]
            #print("Val", val)
            val1 = val[0]
            val2 = val[1]
            #print("Val1", val1)
            if val2 == "R":
                Rpart.append([val1,tot])
                Rcounter = Rcounter+1
            if val2 == "S":
                Spart.append([tot,val1])
                Scounter = Scounter+1
            i = i+1
        
        #print(len(Rpart), len(Spart))
        del map1[tot] 
        if (Rintermediate == 0):
            Rintermediate = Rintermediate+1
        if (Sintermediate == 0):
            Sintermediate = Sintermediate+1
        #print("len Spart====================>", Spart)     
        count = 0
        if len(Rpart) and Rintermediate < splitsofR:
            while True:
                lines = fpp.readline()
                #print(len(lines))
                if len(lines) == 0:
                    Rintermediate += 1
                    fpp.close()
                    if Rintermediate == splitsofR:
                        break
                    fpp = open("R"+str(Rintermediate)+".txt",'r')
                    break

                
                pairs = lines.strip().split(' ')
                key = pairs[1]
                value = pairs[0]
                if key not in map1.keys():
                    map1[key] = []
                map1[key].append([value,"R"])

                count = count+1

                if count == Rcounter:
                    break
      
        
        count = 0

        
        if len(Spart) and Sintermediate < splitsofS:
            while True:
                lines = fpp1.readline()
                if len(lines) == 0:
                    Sintermediate += 1
                    fpp1.close()
                    if Sintermediate == splitsofS:
                        break
                    fpp1 = open("S"+str(Sintermediate)+".txt",'r')
                    break


                
                pairs = lines.strip().split(' ')
                key = pairs[0]
                value = pairs[1]
                if key not in map1.keys():
                    map1[key] = []
                map1[key].append([value,"S"])
                count = count+1

                if(count == Scounter):
                    break
        #print("R inter", Rintermediate, "S inter", Sintermediate)
    #(len(Rpart), len(Spart))

    for r in Rpart:
        for s in Spart:
            #print(r[0]+ " " + s[1])
            finalOutputFile.write(str(r[0]) + " " + str(r[1]) + " " + str(s[1]))
            finalOutputFile.write("\n")
    return 1                 
def memorycheck(file1,file2,mainmemory):
    reversefile = file2[::-1]
    filename2 = reversefile.split("/")[0]
    reversefile = file1[::-1]
    filename1 = reversefile.split("/")[0]
    fp = open(file1,'r')
    count1 = 0
    for lines in fp:
        count1 = count1+1
    count2 = 0
    fpp = open(file2,'r')
    for lines in fpp:
        count2 = count2+1
    if (count1 + count2 > (mainmemory*100)*(mainmemory-1)*100 ):
        print("Insufficient main memory")
        sys.exit(0)
def memorycheckhash(file1,file2,mainmemory):
    reversefile = file2[::-1]
    filename2 = reversefile.split("/")[0]
    reversefile = file1[::-1]
    filename1 = reversefile.split("/")[0]
    fp = open(file1,'r')
    count1 = 0
    for lines in fp:
        count1 = count1+1
    count2 = 0
    fpp = open(file2,'r')
    for lines in fpp:
        count2 = count2+1
    #if (min(count1,count2) > (mainmemory*100)):
        #print("Insufficient main memory")
        #sys.exit(0)
    return filename1,filename2 
              
def openhash1(file1,mainmemory):
    global Rhash
    tot = mainmemory-1
    hashlist = []
    for i in range(0,mainmemory):
        hashlist.append([])
        Rhash.append(0)
    fp = open(file1,'r')
    for lines in fp:
        pair = lines.strip().split(' ')
        key = pair[1]
        value = pair[0]
        hashval = 0
        for c in str(key):
           hashval = 31*hashval + ord(c)
        hashval = hashval%int(tot)
        #print(str(hashval)+" hashvalueofR")
        Rhash[hashval] = Rhash[hashval]+1
        if len(hashlist[hashval]) == tot:
            #print(len(hashlist[hashval]))
            fpp = open("R"+str(hashval)+".txt","a")
            for values in hashlist[hashval]:   #[[],[],[]]
                #print(values)
                val1 = values[0]
                val2 = values[1]
                fpp.write(str(val1)+" "+str(val2))
                fpp.write("\n")
            hashlist[hashval] = []
        hashlist[hashval].append([value,key])  
    for i in range(0,len(hashlist)):
        if len(hashlist[i]) != 0:
            fpp = open("R"+str(i)+".txt","a")
            for values in hashlist[i]:
                val1 = values[0]
                val2 = values[1]
                fpp.write(str(val1)+" "+str(val2))
                fpp.write("\n")    
    #print(hashlist[0])      
def openhash2(file2,mainmemory):
    global Shash
    tot = mainmemory-1
    hashlist = []
    for i in range(0,mainmemory):
        hashlist.append([])
        Shash.append(0)
    fp = open(file2,'r')
    for lines in fp:
        pair = lines.strip().split(' ')
        key = pair[0]
        value = pair[1]
        hashval = 0
        for c in str(key):
            hashval = 31*hashval + ord(c)
        hashval = hashval%int(tot)
        #print(str(hashval)+" hashvalueofs")
        Shash[hashval] = Shash[hashval]+1
        if len(hashlist[hashval]) == tot:
            fpp = open("S"+str(hashval)+".txt","a")
            for values in hashlist[hashval]:
                val1 = values[0]
                val2 = values[1]
                fpp.write(str(val1)+" "+str(val2))
                fpp.write("\n")
            hashlist[hashval] = []
        hashlist[hashval].append([key,value])
    for i in range(0,len(hashlist)):
        if len(hashlist[i]) != 0:
            fpp = open("S"+str(i)+".txt","a")
            for values in hashlist[i]:
                val1 = values[0]
                val2 = values[1]
                fpp.write(str(val1)+" "+str(val2))
                fpp.write("\n")
            
        
    
def getnexthash(i,mainmemory,filename1,filename2):
    global Rhash
    global Shash
    val1 = Rhash[i]
    val2 = Shash[i]
    flag = 0
    if (val1 == 0 or val2 == 0):
        return
    small = ""
    large = ""
    if val1<=val2:
        small = "R"
        large = "S"
    else:
        small = "S"
        large = "R"
        flag = 1
    #print(small)
    #print(large) 
    if (min(val1,val2)> (int(mainmemory)*100)*(int(mainmemory-1)*100)):
      print("Insufficient main memory")
      sys.exit(0)   
    hashlist = []
    tot = int( mainmemory - 2)
    fp = open(small+str(i)+".txt",'r')
    for lines in fp:
        pair = lines.strip().split(' ')
        key = ""
        value = ""
        #print("aaya")
        if flag == 1:
            key = pair[1]
            value = pair[0]  
            hashlist.append([value,key])         
        else:
            key = pair[0]
            value = pair[1]
            hashlist.append([key,value])
        
    fp.close()
    #print("small file" + str(hashlist[0]))
    fpp = open(large+str(i)+".txt",'r')
    for lines in fpp:
        #print("dobara")
        pair = lines.strip().split(' ')
        key = ""
        value = ""
        if flag == 0:
            key = pair[0]
            value = pair[1]
        else:
            key = pair[1]
            value = pair[0]
        for cot in hashlist:
            #print(cot)  
            #print("aa raha hoon")  
            if flag == 0:
                #print("flag 1")
                val1 = cot[0]
                val2 = cot[1]
                if key == val2:
                    #print("write")
                    tpp = open(filename1+"_"+filename2+"_"+"join"+".txt",'a')
                    tpp.write(str(val1)+" "+str(val2)+" "+str(value))
                    tpp.write("\n")
            else:
                #print("flag 0")
                val1 = cot[0]
                val2 = cot[1]
                if key == val1:
                    #print("write")
                    tpp = open(filename1+"_"+filename2+"_"+"join"+".txt",'a')
                    tpp.write(str(value)+" "+str(key)+" "+str(val2))
                    tpp.write("\n")   
    return

def main():
    arguments = sys.argv[1:] 
    #print(arguments)
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    #print(file1, file2)
    sort = sys.argv[3]
    mainmemory = int(sys.argv[4])
    if sort =="sort":
        memorycheck(file1,file2,mainmemory)
        filename1 = sortfile1(file1)
        filename2 = sortfile2(file2)
        opensort1(filename1,mainmemory)
        opensort2(filename2,mainmemory)
        f1 = open("R0.txt",'r+')
        for line in f1:
            pairs = line.strip().split(' ')
            key = pairs[1]
            value = pairs[0]
            if key not in map1.keys():
                map1[key] = []
            map1[key].append([value,"R"])
        f1.close()
        f1 = open("S0.txt",'r+')
        for line in f1:
            pairs = line.strip().split(' ')
            key = pairs[0]
            value = pairs[1]
            if key not in map1.keys():
                map1[key] = []
            map1[key].append([value,"S"])
        f1.close()
        firstfile = filename1[::-1]
        secondfile = filename2[::-1]
        finalOutputFile = open(firstfile+"_"+secondfile+"_"+"join"+".txt", "w")

        global fpp
        global fpp1

        if splitsofR > 1:
            fpp = open("R"+str(1)+".txt",'r')
        
        if splitsofS > 1:
            fpp1 = open("S"+str(1)+".txt",'r')
        
        while(getnext(finalOutputFile, mainmemory*100)):
            pass
    elif(sort == "hash"):
        filename1,filename2 = memorycheckhash(file1,file2,mainmemory)
        filename1 = filename1[::-1]
        filename2 = filename2[::-1]
        openhash1(file1,mainmemory)
        openhash2(file2,mainmemory)
        global Rhash
        global Shash
        #print(Rhash)
        #print(Shash)
        for i in range(mainmemory):
            getnexthash(i,mainmemory,filename1,filename2)
    
        for i in range(mainmemory):
         if Rhash[i] != 0:
           os.remove("R"+str(i)+".txt")
 
         if Shash[i] != 0: 
           os.remove("S"+str(i)+".txt")    

main()
