import paths
from datetime import date, time, datetime

def weatherlinktext(estacion):
    filetxt1 = paths.file+estacion+".txt"
    print(filetxt1)
    filetxt2 = paths.file+estacion+"2.txt"
    print(filetxt2)
    filecsv = paths.file+estacion+".csv"
    print(filecsv)


def current_date_format(date):
months = ("ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE")
day = date.strftime("%d")
month = months[date.month - 1]
year = date.year
messsage = "{} - {} - {}".format(day, month, year)

return messsage

day=datetime.today()
currentday=day.strftime('Día :%d, Mes: %m, Año: %Y')
print(currentday)
fecha=currentday
fechaformat=(current_date_format(fecha))
print(fechaformat)

    # with open(filetxt1,'r',encoding='utf8') as lines, open(filetxt2,'w',encoding='utf-8') as output:
    #     for line in lines: #Lee cada linea una por una 
    #         if line.strip(): #Si encuentra una linea vacia la elimina
    #             output.write(line)

    # with open(filetxt2,'r',encoding='utf-8') as lines,

    # with open(filetxt2,'r+',encoding='utf-8') as datos:
    #     contenido=datos.read()
    #     text0=contenido.replace('Last updated:','fechaHora')
    #     text1=text0.replace('Barometer','presionBar')
    #     text2=text1.replace('Temperature', 'temperatura')
    #     text3=text2.replace('Humidity','humedadRelativa')
    #     text4=text3.replace('Wind Speed','velocidadViento')
    #     text5=text4.replace('Wind Direction','direccionViento')
    #     text6=text5.replace(' ',',')
    #     print(text6)
    

        
try:
    test=weatherlinktext('LALADRILLERA')
except Exception as e:
    print('ERROR:',e)