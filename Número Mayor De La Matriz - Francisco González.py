class NumeroMayorMatriz:
    
    def main(self, B):
##      Construir una función que reciba como
##      parámetro una matriz 4x4 entera y
##      retorne el número de la fila en donde se
##      encuentre por primera vez el número
##      mayor de la matriz.
        A = []
        print("---Programa Para Localizar La Fila En Donde Se Encuentra El Mayor Número De La Matriz---")
        print("Ingrese los elementos de la matriz...")
        for i in range(4):
            A.append([])
            for j in range(4):
                x = int(input("Elemento [{},{}]: ".format(i, j)))
                A[i].append(x)
        print("")
        print("La matriz queda así:")
        for i in A:
            for j in i:
                print ("{}".format(j), end=" ")
            print("")
        print("")
        self.B = A
        return A

    def NumeroMayor(self):
        n = self.B[0][0]; fil = 0; ci = 0
        for i in range(4):
            for j in range(4):
                if (self.B[i][j] > n):
                    n = self.B[i][j]
                    fil = i
                else:
                    if(n == self.B[i][j]):
                        ci += 1
        if(ci == 16):
            return ci
        else:
            return fil
        
B = []
NMM = NumeroMayorMatriz()
B = NMM.main(B)
fila = NMM.NumeroMayor()
if(fila != 16):
    print("El mayor número de la matriz se encuentra por primera vez en la fila", fila)
else:
    print("No hay número mayor, porque la matriz está igualada a", B[0][0] )

