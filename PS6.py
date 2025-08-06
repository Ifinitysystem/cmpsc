"""
Course     : CMPSC 131, Summer 2025
File       : PS6.py 

Name       : Jonathan Reese
GitHub User: ifinitysystem
Collaboration Statement: N/A
"""

#-YOUR CODE STARTS HERE  (TODO) 
# Problem 1.1
def sum_of_rows(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            nums = line.strip().split(',')
            row_sum = 0
            for num in nums:
                row_sum += float(num)
            result.append(round(row_sum, 2))
    return result

# Problem 1.2
def sum_of_columns(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            converted_row = []
            for num in row:
                converted_row.append(float(num))
            data.append(converted_row)

    max_cols = 0
    for row in data:
        if len(row) > max_cols:
            max_cols = len(row)

    col_sums = []
    for i in range(max_cols):
        col_sums.append(0)

    for row in data:
        for i in range(len(row)):
            col_sums[i] += row[i]

    for i in range(len(col_sums)):
        col_sums[i] = round(col_sums[i], 2)

    return col_sums

# Problem 1.3
def is_magic_square(filename):
    square = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            int_row = []
            for num in row:
                int_row.append(int(num))
            square.append(int_row)

    n = len(square)
    for row in square:
        if len(row) != n:
            return False

    magic_sum = 0
    for i in range(len(square[0])):
        magic_sum += square[0][i]

    for row in square:
        row_sum = 0
        for val in row:
            row_sum += val
        if row_sum != magic_sum:
            return False

    for col in range(n):
        col_sum = 0
        for row in range(n):
            col_sum += square[row][col]
        if col_sum != magic_sum:
            return False

    diag1 = 0
    diag2 = 0
    for i in range(n):
        diag1 += square[i][i]
        diag2 += square[i][n - 1 - i]

    if diag1 != magic_sum or diag2 != magic_sum:
        return False

    return True

# Problem 1.4
def buy_ticket(filename, seat):
    seats = []
    with open(filename, 'r') as file:
        for line in file:
            seats.append(line.strip().split())

    row_char = seat[0]
    if 'a' <= row_char <= 'z':
        row_index = ord(row_char) - ord('a')
    else:
        row_index = ord(row_char) - ord('A')

    col_index = int(seat[1:]) - 1

    if row_index >= len(seats):
        return False
    if col_index >= len(seats[row_index]):
        return False

    if seats[row_index][col_index] != 'O':
        return False

    seats[row_index][col_index] = 'X'

    with open(filename, 'w') as file:
        for row in seats:
            file.write(' '.join(row) + '\n')

    return True

# Problem 2.1
def product_of_digits(n):
    if n < 10:
        return n if n != 0 else 1
    last = n % 10
    if last == 0:
        return product_of_digits(n // 10)
    else:
        return last * product_of_digits(n // 10)

# Problem 2.2
def near_by_unique(n):
    if n < 10:
        return n

    last = n % 10
    rest = n // 10
    second_last = rest % 10

    if last == second_last:
        return near_by_unique(rest) 
    else:
        return near_by_unique(rest) * 10 + last

# Problem 2.3
def zero_below(table, threshold):
    zero_below_helper(table, threshold, 0, 0)

def zero_below_helper(table, threshold, row, col):

    if row >= len(table):
        return

    if col >= len(table[row]):
        zero_below_helper(table, threshold, row + 1, 0)
        return

    if table[row][col] < threshold:
        table[row][col] = 0

    zero_below_helper(table, threshold, row, col + 1)

# Problem 2.4
def remove_evens(nums):
    if nums == []:
        return []
    first = nums[0]
    rest = remove_evens(nums[1:])
    if first % 2 != 0:
        return [first] + rest
    else:
        return rest

# Problem 2.5
def remove_evens_destructive(num_lst, index=0):
    if index >= len(num_lst):
        return
    if num_lst[index] % 2 == 0:
        del num_lst[index]
        remove_evens_destructive(num_lst, index)
    else:
        remove_evens_destructive(num_lst, index + 1)




################################################################################

def main():
    #-YOUR ASSERTIONS TO TEST ALL YOUR FUNCTIONS STARTS HERE (TODO)
 print(sum_of_rows('numbers.csv'))

 print(sum_of_columns('numbers.csv'))
 print(is_magic_square('num_2.txt'))
 print(buy_ticket("seats.txt", "a1"))
 print(buy_ticket("seats.txt", "B3"))
 print(buy_ticket("seats.txt", "A10"))
 print(product_of_digits(1024))  # Output: 8
 print(product_of_digits(1005))# Output: 5
 print(product_of_digits(1))# Output: 1
 print(product_of_digits(0))# Output: 1
 print(near_by_unique(22224666666782))# Output: 246782
 print(near_by_unique(5555))# Output: 5
 print(near_by_unique(121212))# Output: 121212
 print(near_by_unique(1112233))# Output: 123
 table = [[1, 6, 5], [3, -1], [6, 85, 12]]
 zero_below(table, 6)
 print(table)# Output: [[0, 6, 0], [0, 0], [6, 85, 12]]
 print(remove_evens([6, 8, 7, 65, 6, 4, 6]))  # Output: [7, 65]
 print(remove_evens([2, 4, 6])) # Output: []
 print(remove_evens([1, 3, 5]))# Output: [1, 3, 5]
 print(remove_evens([])) # Output: []
 num_lst = [6, 8, 7, 65, 6, 4, 6]
 remove_evens_destructive(num_lst)
 print(num_lst) # Output: [7, 65]

 

if __name__ == "__main__":
    main()
