import paths

def weatherlinktext(estacion):
    filetxt1 = paths.file+estacion+".txt"
    print(filetxt1)
    filetxt2 = paths.file+estacion+"2.txt"
    print(filetxt2)
    filecsv = paths.file+estacion+".csv"
    print(filecsv)

    with open(filetxt1,'r+',encoding='utf-8') as datos:
        contenido=datos.read()
        text0=contenido.replace('Last updated','fechaHora')
        text1=text0.replace('Barometer','presionBar')
        text2=text1.replace('Temperature', 'temperatura')
        text3=text2.replace('Humidty','humedadRelativa')
        text4=text3.replace('Wind Speed','velocidadViento')
        text5=text4.replace('Wind Direction','direccionViento')
        print(text5)
        with open(filetxt2,'w',encoding='utf-8') as rewrite:
            rewrite.write(text5)
        

test=weatherlinktext('LALADRILLERA')