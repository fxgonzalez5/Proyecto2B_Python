class PrimosMenores:

    def main(self):
##      Leer una matriz 4x6 entera y determinar
##	en qué posiciones están los menores
##	primos por fila.
        cde = 0; primo = 0; band = False; A = []
        print("---Programa Para Encontrar El Menor Primo Por Fila---")
        print("Ingrese los elementos de la matriz...")
        for i in range(4):
            A.append([])
            for j in range(6):
                x = int(input("Elemento [{},{}]: ".format(i, j)))
                A[i].append(x)
        print("")
        print("La matriz queda así:")
        for i in A:
            for j in i:
                print ("{}".format(j), end=" ")
            print("")
        print("")
        for i in range(4):
            for j in range(6):
                for k in range (1,A[i][j]+1):
                    if(A[i][j] % k == 0):
                        cde += 1
                if(cde == 2):
                    if(primo == 0):
                        primo = A[i][j]
                    else:
                        if(A[i][j] < primo):
                            primo = A[i][j]
                cde = 0
            for j in range(6):
                if((primo == A[i][j]) and (primo != 0)):
                    if(band == False):
                        print("El menor número primo de la fila {} se encuentra en las posición: ".format(i), end="")
                        band = True
                    print ("[{},{}]".format(i, j), end=" ")
            if(band == False):
                print("No se ha encontrado ningún número primo en la fila {}".format(i), end="")
            print("")
            band = False
            primo = 0
            
priMen = PrimosMenores()
priMen.main()
