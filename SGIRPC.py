# Importamos las librerías necesarias
import time
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import ModuloSGIRPC
import threading

def timer(timer_runs):
    while timer_runs.is_set():
        espacio='-------------'

        try:
            ModuloSGIRPC.procesolocal("GAMII", "GAM2S")
            print("Se han filtrado los datos de la nueva estación en GAM")
        except:
            print("Hubo un problema al filtrar los datos de la nueva estación en GAM")

        try:
            ModuloSGIRPC.procesolocal("DelMar","TLAS")
            print("Se han filtrado los  datos de la nueva estacion en Tlahuac")
        except:
            print("Hubo un problema al filtrar los datos de la nueva estación en Tlahuac")

        try:
            ModuloSGIRPC.procesolocal("Cuajimal","STFS")
            print("Se han filtrado los  datos de la nueva estacion en Santa Fe")
        except:
            print("Hubo un problema al filtrar los datos de la nueva estación en Santa Fe")

        try:
            ModuloSGIRPC.procesolocal("Tezonco","TEZS")
            print("Se han filtrado los  datos de la nueva estacion en Iztapalapa II")
        except:
            print("Hubo un problema al filtrar los datos de la nueva estación en Iztapalapa II")

        try:
            ModuloSGIRPC.procesolocal("Lomas","LOMS")
            print("Se han filtrado los  datos de la nueva estacion en Iztapalapa1")
        except:
            print("Hubo un problema al filtrar los datos de la nueva estación en Iztapalapa1")

        try:
            ModuloSGIRPC.procesolocal("Belveder","BELVS")
            print("Se han filtrado los  datos de la nueva estacion en Ajusco")
        except:
            print("Hubo un problema al filtrar los datos de la nueva estación en Ajusco")
        
        try:
            ModuloSGIRPC.procesolocal("SanJeron", "SJEROS")
            print("Se han filtrado los datos de la nueva estación en San Jeronimo")
        except:
            print("Hubo un problema al filtrar los datos de la nueva estación en San Jeronimo")

        try:
            ModuloSGIRPC.proceso("iztacalco","AGOS")
        except:
            print("Hubo un problema con la descarga de datos de esta estación")

        try:
            ModuloSGIRPC.proceso("azcapotzalco","FERS")
        except:
            print("Hubo un problema con la descarga de datos de esta estación")

        try:
            ModuloSGIRPC.proceso("cuautepec","CUAUS")
        except:
            print("Hubo un problema con la descarga de datos de esta estación")

        try:
            ModuloSGIRPC.proceso("juarez", "SGIRPC")
        except:
            print("Hubo un problema con la descarga de datos de esta estación")

        try:
            ModuloSGIRPC.proceso("miguelhidalgo","LEGS")
        except:
            print("Hubo un problema con la descarga de datos de esta estación")

        try:
            ModuloSGIRPC.proceso("milpaalta","MPAS")
        except:
            print("Hubo un problema con la descarga de datos de esta estación")

        try:
            ModuloSGIRPC.proceso("topilejo","TPJS")
        except:
            print("Hubo un problema con la descarga de datos de esta estación")

        try:
            ModuloSGIRPC.proceso("coyoacan","SURS")
        except:
            print("Hubo un problema con la descarga de datos de esta estación")

        try:
            ModuloSGIRPC.proceso("xochimilco","TLHS")
        except:
            print("Hubo un problema con la descarga de datos de esta estación")

        final=datetime.now()
        print(final)
        time.sleep(270)   # 10 minutos=600.Se le estaron un par de segundos del proceso.
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()

