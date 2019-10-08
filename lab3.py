#!/usr/bin/env python
# coding: utf-8

# # Lab 3
# In the following cell cell you have several list. 
#list of 007 movies where Sean Connery features James Bond
moviesSeanConnery = ["Dr. No (1962)",
"From Russia with Love (1963)",
"Goldfinger (1964)",
"Thunderball (1965)",
"You Only Live Twice (1967)",
"Diamonds Are Forever (1971)",    
"Never Say Never Again (1983)"]  

#list of 007 movies where David Neven features James Bond
moviesDavidNeven=["Casino Royale (1967)"]    

#list of 007 movies where George Lazenby features James Bond
moviesGeorgeLazenby=["On Her Majesty's Secret Service (1969)"]  
          
#list of 007 movies where Roger Moore features James Bond   
moviesRogerMoore=[ "Live and Let Die (1973)",
"The Man with the Golden Gun (1974)",
"The Spy Who Loved Me (1977)",
"Moonraker (1979)",
"For Your Eyes Only (1981)",
"Octopussy (1983)",
"A View to a Kill (1985)"]

#list of 007 movies where Timothy Dalton features James Bond  
moviesTimothyDalton=[
"The Living Daylights (1987)",
"Licence to Kill (1989)"  
]

#list of 007 movies where Pierce Brosnan features James Bond  
moviesPierceBrosnan=[
"GoldenEye (1995)",
"Tomorrow Never Dies (1997)",
"The World Is Not Enough (1999)",
"Die Another Day (2002)"
]

#list of 007 movies where Daniel Craig features James Bond 
moviesDanielCraig=["Casino Royale (2006)",
"Quantum of Solace (2008)",
"Skyfall (2012)",
"Spectre (2015)"]


# 1. Create a list of lists (movies007). The list will be composed by each list of movies featured by each actor.
movies007=[]
movies007.append(moviesSeanConnery)
movies007.append(moviesDavidNeven)
movies007.append(moviesGeorgeLazenby)
movies007.append(moviesRogerMoore)
movies007.append(moviesTimothyDalton)
movies007.append(moviesPierceBrosnan)
movies007.append(moviesDanielCraig)
print(movies007)

# 2. How many movies were played by the first actor to play James Bond?
moviesFirstActor = len(movies007[0])
print(moviesFirstActor)

# 3. How many movies were played by the last actor to play James Bond?
moviesLastActor = len(movies007[-1])
print(moviesLastActor)

# 4. How many actors played the role of James Bond?
actorsRole = len(movies007)
print(actorsRole)


# 5. Create a new list with the number of movies played by each actor
listNumber = []
for i in movies007:
    listNumber.append(len(i))
print(listNumber)

# 6.  How many movies were played by the actor who appeared most often in movies?
maxValue = max(listNumber)
print(maxValue)


# 7. How many movies were played by the actor who appeared in fewer movies?
minValue = min(listNumber)
print(minValue)


# 8. Create a new list (movies007a) with all the films. 
movies007a = []
for i in movies007:
    for j in i:
        movies007a.append(j)
print(movies007a)


# 9. Sort the elements of the list 
movies007a.sort()
print (movies007a)

# 10. Reverse the order of the list. What will happen if this method is executed twice? Does this method sort the list if it is not sorted?
movies007a.reverse()
print(movies007a)

#Se fizermos a operação 2 vezes, a lista volta ao original


# 11. What is the index of the movie "Spectre (2015)" in the list of movies
stringx = 'Spectre (2015)'
num = 0
for i in movies007a:
    if i != stringx:
        num+=1
    else:
        print (num)


# 12. Add the movie "007 and the bad Guy of the climate change (2020)" in the 11th position.
movies007a.insert(11,'007 and the bad Guy of the climate change (2020)')
print(movies007a)

# 13. It was a mistake. Remove the movie "007 and the bad Guy of the climate change (2020)"
stringx = '007 and the bad Guy of the climate change (2020)'
for i in movies007a:
    if i == stringx:
        movies007a.remove(i)
print (movies007a)




