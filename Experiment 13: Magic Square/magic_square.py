#Q13) Magic Square - Odd numbers only
def create_magic_square(n):
    # Step 3: Create an n by n array initialized with zeros
    magic_square = [[0] * n for _ in range(n)]
    
    # Step 4.1: Place the number 1 in the middle of the first row
    i = 0
    j = n // 2
    num = 1
    magic_sum = n * (n ** 2 + 1) // 2  # Calculate the magic constant using the formula
    
    # Step 4.2: Fill the magic square with numbers
    while num <= n * n:
        magic_square[i][j] = num
        num += 1
        
        # Step 4.2.1: Calculate the next position
        next_i = (i - 1) % n
        next_j = (j + 1) % n
        
        # Step 4.2.2: Check if the next position is available
        if magic_square[next_i][next_j] == 0:
            i, j = next_i, next_j
        else:
            # Step 4.2.2.1: If in row -1, then change to the last row
            if next_i == -1:
                next_i = n - 1
            # Step 4.2.2.2: If in the last column change to the first column
            if next_j == n:
                next_j = 0
            # Step 4.2.2.3: If blocked, then drop down to the next row from the original position
            i = (i + 1) % n
            j = j
    
    return magic_square, magic_sum

def display_magic_square(magic_square, magic_sum):
    # Step 5: Display the magic square
    print("Magic Square:")
    for row in magic_square:
        print(" ".join(map(str, row)))
    
    # Display magic sum
    print("\nMagic Sum (Rows, Columns, Diagonals):", magic_sum)


# Step 1: Start
print("Magic Square Generator")
print("----------------------")
# Step 2: Read the order of the matrix from the user and store it in n
n = int(input("Enter the order of the magic square: "))

# Generate magic square
magic_square, magic_sum = create_magic_square(n)

# Display magic square
display_magic_square(magic_square, magic_sum)
