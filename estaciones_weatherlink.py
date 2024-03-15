import weatherlink

# # Function to create directories
# def makedir(path):
#     if not os.path.exists(path):
#         os.makedirs(path)
#         print("El directorio " + path + " ha sido creado")
#     else:
#         print("El directorio " + path + " ya existe")

# pathestaciones = "../estaciones"
# pathfiles = "../files"
# makedir(pathestaciones)
# makedir(pathfiles)

# Try to get data for station
try:
    weatherlink.weatherlink("LALADRILLERA","https://www.weatherlink.com/bulletin/191c4832-5370-43ba-8274-7be9be6517a7")
except Exception as e:
    print("ERROR:",e)

try:
    weatherlink.weatherlink("CUERNAVACA","https://www.weatherlink.com/bulletin/3be7838c-5871-4c0b-ace1-8def8be84aff")
except Exception as e:
    print("ERROR:",e)
