'''
Created on 12 de oct. de 2016

@author: lagarto
'''
# -*- coding: utf-8 -*-
file=open("fichero1.csv",encoding="utf8") 
file2=open("fichero2.csv","w",encoding="utf8")
for i in file.readlines():
    line=i.split(";")
    if(line[5]!="NULL"):
        fechaantigua=line[5].replace('"','')
        date=fechaantigua.split("-")
        date2=[date[2],date[1],date[0]]
        fecha="-".join(str(v) for v in date2)
        line[5]=fecha
    else:
        line[5]="1990-1-1"
    linea=";".join(str(v) for v in line)
    file2.write(linea)
file.close()
file2.close()
print("terminado")
    