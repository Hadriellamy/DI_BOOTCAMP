#Instructions
"""
Given a “Matrix” string:

7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!


The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
A grid means that you could potentially break it into rows and columns, like here:

7	i	i
T	s	x
h	%	?
i		#
s	M	
$	a	
#	t	%
^	r	!


Matrix: A matrix is a two-dimensional array. It is a grid of numbers arranged in rows and columns.
To reproduce the grid, the matrix should be a 2D list, not a string



To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.

Using his technique, try to decode this matrix.

Hints:
Use
● lists for storing data
● Loops for going through the data
● if/else statements to check the data
● String for the output of the secret message

Hint (if needed) : Look at the remote learning “Matrix” video.

"""


# Le texte brut de la matrice
matrix_str = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

lines = matrix_str.splitlines()
matrix = [list(line) for line in lines]

cols = max(len(row) for row in matrix)

result_columns = []
for col in range(cols):
    col_str = ""
    gap = False
    for row in matrix:
        if col < len(row):
            ch = row[col]
            if ch.isalpha():
                if gap and col_str != "":
                    col_str += " "
                col_str += ch
                gap = False
            else:
                if col_str != "":
                    gap = True
    result_columns.append(col_str)

final_message = " ".join(result_columns)
print(final_message)
