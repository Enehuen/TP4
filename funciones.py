#Estas funciones son para validar que los valores ingresados esten en un rango entre 0 y 99 o entre 10.00 y 999.99
#Asi como tambien implemente una subfuncion que verifique que los datos son de valor numerico, ya que todos entran como cadena de texto
#Esto lo hice para ahorrar el "int()" y poder volver a pedir un valor sin que el programa termine en error.
def validocodigo(x,tope,min): #En este nuevo codigo implementamos valores generales para marcar los limites de la validacion señaladas por Alicia, en este caso, marcando un tope y un minimo.
  if x.isnumeric():  #Funcion que valida si un valor es numerico, asi lo transformo a int o le asigno un valor manejable
    x = int(x)
    if x<min:
      return 1
    elif x<=tope:
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
