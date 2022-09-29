# determinar un capital c para verigualr que mes se dara el valor de 20000 con uninteres compuesto del 5%

print("--------------------------------------------------------------")
print("---se determinara en que mes se dara el doble de lo inicial---")
print("----------------con interes copuesto del 5 %------------------")
print("--------------------------------------------------------------")

#input
c=int(input("ingrese el valor inicial: "))

i=1
sum=0

#proseccing

while sum<=20000:
    sum=sum+sum*0.05
    i=i+1

# putput

print("el mes es"+str(i))
