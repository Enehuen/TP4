#Actualizacion hecha por Ezequiel Nehuen
#Empezamos el programa ingresando las funciones necesarias para validacion de los datos ingresados.
#Estas 3 funciones son para validar que los valores ingresados esten en un rango entre 0 y 99 o 10.00 y 999.99
#Asi como tambien implemente una subfuncion que verifique que los datos son de valor numerico, ya que todos entran como cadena
#Esto lo hice para ahorrar el "int()" y poder volver a pedir un valor sin que el programa termine en error.
def validocodigo(x,tope,min):
  if x.isnumeric():  #Funcion que valida si un valor es numerico, asi lo transformo a int o le asigno un valor manejable
    x = int(x)
    if x<min:
      return 1
    elif x<tope:
      return 0
    else:
      return 1
  else:
    return 1
#Definimos una funcion para validar el type del precio y sus rangos de valores como en la anterior funcion.
def validoprecio(x,tope,min):
  if x.replace('.','',1).isdigit(): #Funcion que valide si un numero tiene decimales
    x=float(x)
    if x<min:
      return 1
    elif x<=tope:
      return 0
    else:
      return 1
  else:
    return 1

#Empezamos el programa ingresando un valor preferiblemente numerico.
CP = input("Ingrese un código de pieza(00-99), ingrese 0 para finalizar: ")
#Asigno el contador de códigos de piezas fuera del bucle ya que si no lo hago el contador se vuelve a 0 cada vez que vuelvo a pedir un CP
cantcp = 0

#En este punto aclaramos que la cadena de texto sea "0" debido a que el input siempre es str
while CP!="0":
  validoCP=validocodigo(CP,99,0)
  if validoCP==0:
    CP=int(CP)
    cantcc = 0  #Empiezo un contador de piezas en esta parte del codigo para que se reinicie cada vez que el loop termine
    PrT = 0   #asigno la variable precio total en esta parte del codigo para que se vuelva a 0 junto con el contador
    cantcp += 1 #Iniciamos el contador de cantidad de piezas.
    print(f'Su código de pieza es: {CP}')
    CC=input(f"Ingrese un código de componente de por lo menos 2 dígitos, ingrese 0 para finalizar:")
    while CC!="0":
      validoCC=validocodigo(CC,99,0)
      if validoCC==0:
        CC=int(CC)
        CC=(CC*100)+CP  #En este punto opte porque el Codigo de componente sea calculado en base al CC sobre 100 y sumarle el CP como decimales.
        print(f'Su código de componente es {CC}')
        PrC = input('Ingrese el precio del componente: ')
        while PrC!=True:
          validoPrC=validoprecio(PrC,999.99,10)
          if validoPrC==0:
            PrC=float(PrC)
            cantcc += 1
            PrT = PrT+PrC
            CC=input(f'El precio del componente es ${PrC}, vuelva a ingresar un componente o ingrese 0 para finalizar: ')
            break
          else:
            PrC = input('Precio de componente incorrecto, vuelva a ingresar un precio entre 10,00 y 999,99: ')
      else:
        CC=input('Código de componente incorrecto, vuelva a ingresar un código entre 01 y 99 o ingrese 0 para finalizar: ')
    print(f"El precio total de {cantcc} componentes es: ${PrT}")
    CP = input('Vuelva a ingresar un código de pieza o ingrese 0 para finalizar: ')
  else:
    CP = input('Código de pieza incorrecto, vuelva a ingresar un código entre 01 y 99 o ingrese 0 para finalizar: ')
print(f'La cantidad de piezas procesadas fueron: {cantcp}.')
