class DigitosPrimos:

    def main(self):
##      Leer n números enteros,
##	almacenarlos en un vector y
##	determinar cuántos dígitos primos
##	hay en los números leídos.
        cde = 0; cp = 0; A = []
        print("---Programa Para Contar Dígitos Primos---")
        n = int(input("Ingrese el límite del vector: "))
        print("Ingrese los elementos del vector...")
        for i in range(n):
            x = int(input("Elemento {}: ".format(i)))
            A.append(x)
        print("")
        print("Vector:",A)
        print("")
        for i in range(n):
            num = str(A[i])
            for j in range(len(num)):
                aux = int(num[j])
                for k in range(1,aux+1):
                    if(aux % k == 0):
                        cde += 1
                if(cde == 2):
                    cp += 1
                cde = 0
        if(cp != 0):
            print("En total hay", cp ,"dígitos primos ingresados en el vector.")
        else:
            print("No hay dígitos primos ingresados en el vector.")

                        
digPri = DigitosPrimos()
digPri.main()
