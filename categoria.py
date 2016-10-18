'''
Created on 13 de oct. de 2016

@author: lagarto
'''
file=open("ps_category.csv",encoding="utf8")
cuenta=0
for i in file.readlines():
    cuenta+=1
    line=i.split(";")
    if(len(line)>4):
        if(line[2]==line[3]):
            print(line[0])
            print (cuenta)
    else:
        print (cuenta)
print("final")