#Actualizacion hecha por Ezequiel Nehuen
def validacion_cods(x):
    if x.isnumeric():
        x = int(x)
        if 0 <= x <= 99:
            return 1
    return 0

def validacion_prc(x):
    if x.replace('.', '', 1).isdigit():
        x = float(x)
        if 10 <= x <= 999.99:
            return 1
    return 0

def validacion_cc(cc, cp):
    if cc.isnumeric() and cp.isnumeric():
        if len(cc) == 2 and len(cp) == 2:
            if validacion_cods(cc) and validacion_cods(cp):
                cc = int(cc)
                cp = int(cp)
                cc = (cc * 100) + cp  # Formando el código del componente
                return cc
    return 0

cant_cc = 0
cant_cp = 0
prt = 0

cp = input("Ingrese un código de pieza entre 00 y 99 o ingrese 0 para finalizar: ")
while cp != "0":
    if validacion_cods(cp):
        print(f"Codigo de pieza {cp}")
        cant_cp += 1
        cc = input("Ingrese un código de componente o ingrese 0 para finalizar: ")
        while cc != "0":
            cc = validacion_cc(cc, cp)
            if cc:
                print(f'Su código de componente es {cc}')
                prc = input('Ingrese el precio del componente: ')
                if validacion_prc(prc):
                    cant_cc += 1
                    prt += float(prc)
                else:
                    print("Precio de componente invalido, ingrese uno nuevo")
            else:
                print("Codigo de componente invalido")
            cc = input("Ingrese un código de componente o ingrese 0 para finalizar: ")
        print(f"El precio total de {cant_cc} componentes es de ${prt}")
        prt = 0
        cant_cc = 0
    else:
        print("Codigo de pieza invalido")
    cp = input("Ingrese un código de pieza entre 00 y 99 o ingrese 0 para finalizar: ")
print(f"En total se procesaron {cant_cp} de piezas")