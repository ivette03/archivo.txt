
f=open('placas.txt','r')
datos=f.read()
f.close()
print(datos)

f=open('placas.txt','w')
lista=[
    'un auto\n',
    'dos autos\n',
    'tres autos\n',
]
f.writelines(lista)
f.close()









