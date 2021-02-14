class BusquedaBinaria:

    def main(self):
##      Dise˜ne un algoritmo que reciba como datos de 
##	entrada un número entero n, n números enteros, 
##	que serán los elementos de un vector de tama˜no 
##	n y un número entero x. Este algoritmo debe 
##	regresar como dato de salida la posición 
##	dentro del vector en la que se encuentra x. 
##	Esta posición debe ser determinada usando el 
##	método de búsqueda Binaria.
##	Entrada: n = 6, A = [4, 2, 6, 3, 7, 2], x = 4.
##	Salida: El número SI se encuentra en el arreglo.
        A = []; band = False
        print("--Programa Para Encontrar La Posición De Un Número En Método Binario---")
        n = int(input("Ingrese el límite del vector: "))
        x = int(input("Ingrese el número que desea buscar: "))
        print("Ingrese los elementos del vector...")
        for i in range(n):
            num = int(input("Elemento {}: ".format(i)))
            A.append(num)
        print("")
        print("Vector:",A)
        for i in range(1, n+1):
            for j in range(n-i):
                if (A[j] > A[j+1]):
                    aux = A[j]
                    A[j]=A[j+1]
                    A[j+1]=aux
        print("Vector Ordenado: ",A)
        inferior = 0; superior = n-1
        while(inferior <= superior and band == False):
            centro = int((superior+inferior)/2)
            if(A[centro] == x):
                print("El número buscado está en la posición", centro)
                band = True
            else:
                if(x > A[centro]):
                    inferior = centro + 1
                else:
                    superior = centro - 1
        if (band == False):
            print("El número",x,"no se encuentra en el vector.")

BusBin = BusquedaBinaria()
BusBin.main()
