#Exercise 2 : What is the Season ?

"""Instructions
Ask the user to input a month (1 to 12).
Display the season of the month received :
Spring runs from March (3) to May (5)
Summer runs from June (6) to August (8)
Autumn runs from September (9) to November (11)
Winter runs from December (12) to February (2)# """


month = int(input("Choose a month of the year between 1 and 12 :"))

if month in [3,4,5] :
 print("The season is Spring")
elif month in [6,7,8] :
 print("The season is Summer")
elif month in [9,10,11] : 
 print("The season is Autumn")
else : 
 print("The season is Winter") 
 