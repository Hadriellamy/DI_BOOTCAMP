#Exercise 1 : Lists

"""Instructions

Write Python code to complete the following tasks.

#1 Given a list [1, 2, 3, 4], print out all the values in the list one by one.

#2 Given a list [1, 2, 3, 4], print out all the values in the list multiplied by 20.

#3 Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter of each name: ["E", "T", "M"].

#4 Given a list [1, 2, 3, 4, 5, 6], return a new list with all the even values: [2, 4, 6].

#5 Given two lists [1, 2, 3, 4] and [3, 4, 5, 6], return a new list that contains only the values present in both lists: [3, 4].

#6 Given a list of words ["Elie", "Tim", "Matt"], return a new list with each word reversed and in lowercase: ["eile", "mit", "ttam"].

#7 Given two strings "first" and "third", return a new list of the letters that are present in both strings: ["i", "r", "t"].

#8 For all numbers between 1 and 100, return a list of the numbers that are divisible by 12: [12, 24, 36, 48, 60, 72, 84, 96].

#9 Given the string "amazing", return a list with all the vowels removed: ["m", "z", "n", "g"].

#10 Generate a list with the following value: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

#11 Generate a list with the following structure:

[
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
]

"""


#Solution


#1
list1 = [1,2,3,4,]
print(list1[0],list1[1],list1[2],list1[3])


#2
print([num * 20 for num in list1])
#Another method : print(list1[0] * 20 ,list1[1] * 20 ,list1[2] * 20 ,list1[3] * 20)


#3
list2 = ["Elie", "Tim", "Matt"]
print([char[0] for char in list2])


#4
list3 = [1, 2, 3, 4, 5, 6]

for num in list3 : 
    if num%2 == 0:
      print(num, end = " ")

print()     


#5
list4 = [1, 2, 3, 4]
list5 = [3, 4, 5, 6]

result = list(set(list4) & set(list5))
print(result) 



#6
list6 = ["Elie", "Tim", "Matt"]
result = []

for char in list6 : 
    result.append([char[::-1].lower()])

print(result)  

#7
word1 = "first"
word2 = "third"

common_letter = sorted(list[(set(word1) & set(word2))])
print(common_letter) 

#8
divisible_by_12 = []
for number in range(1,101) :
    if number %12 == 0 :
        divisible_by_12.append(number)

print(divisible_by_12) 


#9
word = "amazing"
voyelle = "aeiou"
result = []

result = [char for char in word if char not in voyelle]
print(result)  


#10
result = []

for i in range(3):
    result.append(list(range(3)))

print(result)   


#11
result = []

for i in range(10):
    result.append(list(range(10)))

print(*result, sep="\n")




   
      







