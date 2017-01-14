# Declaracion de variable globales
v1 = ["es","igual","a"] # Variable de asignacion
v2 = ["es","una","matriz","con"]
v3 = ["encender","el","pin"]
v4 = ["apagar","el","pin"]
v5 = ["leer","el","pin"]
v6 = ["y","guardar","como"]
https://gist.github.com/anonymous/1e934675b6e195383ccbd2ea392dabde





# Se especifican los archivos de entrada

READ = "r"
WRITE = "w"

fentrada = "in.txt"
fsalida = "out.txt"

entrada = open(fentrada, READ)
salida = open(fsalida, WRITE)

# Se empieza a leer linea por linea el archivo

lineasDeEntrada = entrada.readlines()

for linea in lineasDeEntrada:
  
  # Se divide la linea por espacios
  
  linea = linea.split()
  
  # Solo si la linea no esta vacia
  
  if len(linea) > 0:
    
    # Aqui se ponen todas las instrucciones
    
    if (linea[1:4] == v1 ):
      salida.write("int "+linea[0]+" = "+str(linea[-1])+";\n")
      
      
      # Implementecion de digitalWrite(pin, <HIGH>)
		  # Encender el pin <int>
    elif (linea[0:3] == v3):
      salida.write("digitalWrite("+linea[-1]+",HIGH);\n")
		  	
			
		  # Implementacion de digitalWrite(pin, <LOW>)
	  	# Apagar el pin <int>
    elif (linea[0:3] == v4 and int(linea[-1])):
      salida.write("digitalWrite("+linea[-1]+",LOW);\n")
			
		
		  # Implementacion de delay(<milis>)
		  # Esperar <int> segundos
    elif (linea[0] == "esperar" and linea[-1] == "segundos" and int(linea[1])):
      x = int(linea[1]) * 1000 
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
    elif(linea[0] == "Configuracion" or linea[0] == "config" or linea[0] == "configuracion"):
      salida.write("\nvoid setup(){\n")
		
		# Bucle
    elif(linea[0] == "Bucle" or linea[0] == "bucle" or linea[0] == "loop"):
      salida.write("\nvoid loop(){\n")
      
    
      
  
    else:
      
      x = " ".join(linea)
      salida.write("\n"+x+"\n")
      
