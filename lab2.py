#LAB2
#Exercicio1
shoppingList = ['potatoes', 'carrots', 'cod', 'sprouts']

#Exercicio2
scnElem = shoppingList[1]
print(scnElem)
lastElem = shoppingList[-1]
print(lastElem)

#Exercicio3
for i in shoppingList:
    print(i)

#Exercicio4
studentList = []

#Exercicio5
shoppingList.append('orange')
shoppingList.append('lime')
print(shoppingList)

#Exercicio6
shoppingList.remove('carrots')
shoppingList = shoppingList[1:-1]
print(shoppingList)

#Exercicio7
del studentList

#Exercicio8
squares = [x**2 for x in range (1,15)]
print(squares)

#Exercicio9
print(squares [:3])

#Exercicio10 
shopping = shoppingList
copy = shoppingList[:]
print(shopping)

#Exercicio11
shopping = shoppingList
shopping.append('orange')
print(shopping)

#Exercicio12
shoppingList.clear

#Exercicio13
newPurchases= ("bananas", "beans", "rice")
print(newPurchases[1])
#Ao colocarmos o newPurchases[0] = "apple" iremos obter um erro pois
#nao eh possivel atribuir este item ao tuplo

#Exercicio14
fruit = {1: 'orange', 2: 'apple', 3: 'pear', 4: 'grape', 5: 'peach' }
print(fruit)

#Exercicio15
weekList={1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
print(weekList)