
# Convierte una lista a un string
# Se le debe de suministrar un segmento
# De la forma list2str(lista, 2, 3) (lista[2:3])
def list2str(lista,x=None,y=None):
	temp = ""
	for i in lista[x:y]:
		temp = temp + i
	
	return temp




def main(nombreDelArchivo, salidaDelArchivo):
	# Variables globales
	v1 = ["es","igual","a"] # Variable de asignacion
	v2 = ["es","una","matriz","con"]
	v3 = ["encender","el","pin"]
	v4 = ["apagar","el","pin"]
	v5 = ["leer","el","pin"]
	v6 = ["y","guardar","como"]
	v7 = ["leer","el"]
	
	lineasCount = 0
	
	
	
	# Se abre el archivo de entrada
	entrada = open(nombreDelArchivo, "r")
	salida = open(salidaDelArchivo, "w")
	
	# Se itera sobre todas las lineas del archivo
	
	for linea in entrada.readlines():
		
		#Primero caracter a caracter
		#Toda la seccion dentro a "", sus espacios son reemplazados 
		#por _
		
		# Se divide la linea por los espacios
		
		linea = linea.split()
		lineasCount = lineasCount +1
		print (lineasCount)
		

		# Implementacion de int <varname> = <int>
		# De la forma " <varname> es igual a <int>"
		# [<varname>,es,igual,a,<int>]
		
		if (linea[1:4] == v1 ):
			salida.write("int "+linea[0]+" = "+str(linea[-1])+";\n")
		
		
		# Implementecion de digitalWrite(pin, <HIGH>)
		# Encender el pin <int>
		elif (linea[0:3] == v3 and int(linea[-1])):
			salida.write("digitalWrite("+linea[-1]+",HIGH);\n")
			
			
		# Implementacion de digitalWrite(pin, <LOW>)
		# Apagar el pin <int>
		elif (linea[0:3] == v4 and int(linea[-1])):
			salida.write("digitalWrite("+linea[-1]+",LOW);\n")
			
		
		# Implementacion de delay(<milis>)
		# Esperar <int> segundos

		elif (linea[0] == "esperar" and linea[-1] == "segundos" and int(linea[1])):
			x = (int(linea[1]) * 1000)
			salida.write("delay("+str(x)+");\n")
			
			
		# Implementacion de delayas(milis) 
		# Esperar <int> milisegundos
		elif (linea[0] == "esperar" and linea[-1] == "milisegundos" and int(linea[1])):
			salida.write("delay("+linea[1]+");\n")
			
		# Implementacion de int x = digitalRead(pin)
		# Leer el pin <int> y guardar como <varname>
		elif (linea[0:3] == v5 and linea[4:7] and int(linea[3])):
			salida.write("int "+linea[-1]+" = digitalRead("+linea[3]+");\n")
		
		# Leer <varname> y guardar como <varname2>
		elif (linea[0] == "leer" and linea[3:6] ):
			salida.write("int "+linea[-1]+" = digitalRead("+linea[1]+");\n")	
			
		# Implementacion de pinMode(<pin num>,<output>)
		# el pin <int> es de salida
		elif (linea[0:2] == ["el","pin"] and linea[3:] == ["es","de","salida"]):
			salida.write("pinMode("+linea[2]+",OUTPUT);\n")
		
		# el pin <int> es de entrada
		elif (linea[0:2] == ["el","pin"] and linea[3:] == ["es","de","entrada"]):
			salida.write("pinMode("+linea[2]+",INPUT);\n")
		
		# Implementacion de void setup
		# Inicio {
		elif(linea[0:] ==("Configuracion")):
			salida.write("void setup() {\n")
		
		# Bucle
		elif(linea[0:] == ("Bucle")):
			salida.write("{\nvoid loop() {\n")
			
		#En caso contrario escribi la linea
		

		
		else:
			salida.write(linea.join())
		
			

	# Se cierran los ficheros
	entrada.close()
	salida.close()
	

main("in1.txt", "out2.txt")
			
