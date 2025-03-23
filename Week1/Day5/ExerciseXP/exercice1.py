#Exercise 1 : Convert Lists Into Dictionaries
"""
Instructions

Convert the two following lists, into dictionaries.
Hint: Use the zip method
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

"""
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict1 = dict(zip(keys, values))
print(dict1)  
