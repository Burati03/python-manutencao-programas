valor = float(input("Digite o valor: "))

notas100 = int(valor // 100)
valor = valor % 100

notas50 = int(valor // 50)
valor = valor % 50

notas20 = int(valor // 20)
valor = valor % 20

notas10 = int(valor // 10)
valor = valor % 10

notas5 = int(valor // 5)
valor = valor % 5

notas2 = int(valor // 2)
valor = valor % 2

notas1 = int(valor // 1)
valor = round(valor % 1, 2) 

print("100:", notas100)
print("50 :", notas50)
print("20 :", notas20)
print("10 :", notas10)
print("5  :", notas5)
print("2  :", notas2)
print("1  :", notas1)
