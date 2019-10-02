#LAB1
from math import sqrt
from datetime import date
#Exercicio1
x = int(input ("Insira um numero: "))
if type(x) == int:
    print("O numero eh inteiro")
else:
    print("O numero nao eh inteiro")

#Exercicio2
x = int (input ("Insira um numero: "))
if x%2 != 0:
    print("O numero eh impar")
else:
    print("O numero eh par")

#Exercicio3
x = int(input ("Insira um numero: "))
y = int(input ("Insira um numero: "))
if x > y:
    print("O primeiro numero eh maior que o 2º")
elif x == y:
    print("Os numeros sao iguais")
else:
    print("O segundo numero eh maior que o primeiro")

#Exercicio4
x = int(input ("Insira um numero: "))
y = int(input ("Insira um numero: "))
if x%y == 0:
    print("Eh multiplo")
else:
    print ("Nao eh multiplo")

#Exercicio5
capital = 200
tempo = 3
taxa = 0.03
formula = capital * tempo * taxa

#Exercicio6
capital2 = 200
tempo2 = 3
taxa2 = 0.03
formula2 = (capital * (1+ (taxa **tempo)))
print(formula)

#Exercicio7
peso = 50
altura = 1.56
BMI = (peso)/(altura**2)

#Exercicio8
golden = (1 + sqrt(5))/2
print(golden)

#Exercicio9

#Exercicio10
hoje = date.today()
ano = 1998
anos = hoje.year() - 1998
print (anos)

#Exercicio11
nome = "ana leonor"
nameBig = nome.upper()
nameTitle = name.title()
nameSmall = name.lower()
nameCapitalize = name.capitalize()
print(nameBig)
print(nameTitle)
print(nameSmall)
print(nameCapitalize)

#Exercicio12
nome = "ana leonor"
print(nome.find('leo'))