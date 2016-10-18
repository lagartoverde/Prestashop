'''
Created on 14 de oct. de 2016

@author: lagarto
'''
# -*- coding: utf-8 -*-
import shutil
file= open("fichero.csv", encoding="utf8")
for i in file.readlines():
    linea=i.split(",")
    id_image=linea[0]
    id_producto=linea[1]
    id_producto=id_producto[:-1]
    rutaorigen="img/p/"
    rutadestino=""
    rutaorigen=rutaorigen+id_producto+"-"+id_image+".jpg"
    for i in id_image:
        rutadestino+=i+"/"
    rutadestino=rutadestino+id_image+".jpg"
    print(rutaorigen)
    print(rutadestino)
    try:
        shutil.move(rutaorigen, rutadestino)
        print("hecho")
    except:
        rutaorigen=rutaorigen+id_producto+"-"+id_image+"-large.jpg"
        try:
            shutil.move(rutaorigen, rutadestino)
        except:
            rutaorigen=rutaorigen+id_producto+"-"+id_image+"-home.jpg"
            try:
                shutil.move(rutaorigen, rutadestino)
            except:
                rutaorigen=rutaorigen+id_producto+"-"+id_image+"-medium.jpg"
                try:
                    shutil.move(rutaorigen, rutadestino)
                except:
                    pass