import re

print("Ocurrencias de un fragmento de un libro\n")
archivo=open('Harry.txt',encoding='utf8')

linea=archivo.readline()
diccionario={}
while linea!="":
    palabras=linea.split()
    for i in range(len(palabras)):
        palabra=re.sub('[?|.|!|\|/|;|:|,|”|“|(|)|«|»|-|_]','',palabras[i])        
        if palabra in diccionario:
            diccionario[palabra]+=1
        else:
            diccionario.update({palabra:1})
    linea=archivo.readline()
print("Palabras y repeticiones")
for x in diccionario:
    print('({},{}) '.format(x, diccionario.get(x)))
archivo.close()
