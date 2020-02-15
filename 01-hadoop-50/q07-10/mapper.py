#! /usr/bin/python3

##
## Esta es la funcion que mapea la entrada a parejas (clave, valor)
##
import sys
if __name__ == "__main__":
    ##
    ## itera sobre cada linea de codigo recibida
    ## a traves del flujo de entrada
    ##        
    for line in sys.stdin:
        letra = ""
        fecha = ""
        valor = ""
        cantidad = 0
        
        line = line.strip()
        splits = line.split()
        letra = splits[0]
        fecha = splits[1]
        valor = splits[2]
        
        sys.stdout.write("{}\t{}\t{}\n".format(letra,fecha,valor))
