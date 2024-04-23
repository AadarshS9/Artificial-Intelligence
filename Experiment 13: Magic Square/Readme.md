# Aim
Write a program to generate a Magic Square.

# Theoretical Background
A magic square of order n is an arrangement of nxn numbers, usually distinct integers, in a square, such that the n numbers in all rows, all columns and both diagonals sum to the same constant. A magic square contains the
integers from 1 to nxn. The constant sum in every rows, columns and diagonals are called the magic constant or magic sum, M. The magic constant of a normal magic square depends only on n and has the following value:
M = n(nxn+1)/2
The order of a magic square can be odd or even.

Rules for filling magic square
- Rule 1: The position of the next number is calculated by decrementing the row number of the previous number by 1, and incrementing the column number of the previous number by 1. At any time, if the calculated row position
becomes -1, it will wrap around to n-1. Similarly, if the calculated column position becomes n, it will wrap around to 0.
- Rule 2: If the magic square already contains a number at the calculated position, calculated column position will be decremented by 2, and calculated row position will be incremented by 1.
- Rule 3: If the calculated row position is -1 &amp; calculated column position is n, the new position would be: (0, n-2).

# Algorithm
- Step 1: Start.
- Step 2: Read the order of the matrix from the user and store it in n.
- Step 3: Create an n by n array.
- Step 4: Follow these steps to create a magic square.
  - Step 4.1: Place the number 1 in the middle of the first row.
  - Step 4.2: Subtract 1 from the row and add 1 to the column.
    - Step 4.2.1: If possible place the next number at that position.
    - Step 4.2.2: If not possible, follow these steps.
      - Step 4.2.2.1: If in row -1, then change to the last row.
      - Step 4.2.2.2: If in the last column change to the first column.
      - Step 4.2.2.3: If blocked, then drop down to the next row from the original position.
      - Step 4.2.2.4: If in the upper right corner, then drop down to the next row.
- Step 5: Display the magic square.
- Step 6: Stop
