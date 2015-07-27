# Absolute Difference between Diagonals in Matrix
x = int(raw_input())

row_index = 0
col_index = x - 1
col1 = 0
col2 = 0

for i in range(x):
    data = raw_input()
    numbers = data.split(" ")
    col1 = col1 + int(numbers[row_index])
    col2 = col2 + int(numbers[col_index])

    row_index = row_index + 1
    col_index = col_index - 1

print abs(col1 - col2)
