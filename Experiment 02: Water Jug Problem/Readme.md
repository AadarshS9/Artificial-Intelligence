# Aim
Write a program to implement a Water Jug problem

# Theoretical Background
Two jugs are given with capacities m and n. Initially they are given empty. There is an unlimited supply of water. There are two possibilities: either fill the whole jug or a quantity that is less than the given capacity of
jugs. A third positive integer ‘d’ will be also given. Using the two given jugs, ‘d’ amount of water should be filled in the second jug and at the same time the number of steps taken to fill ‘d’ capacity should also be returned.

Some of the production rules to solve water jug problem are:
1. (m,y), if x&lt;m =&gt; Fill the m gallon jug completely.
2. (x,n), if y&lt;n =&gt; Fill the n gallon jug completely.
3. (x-d,y), if x&gt;0 =&gt; Pour some part of m gallon jug.
4. (x,y-d), if y&gt;0 =&gt; Pour some part of n gallon jug.
5. (0,y), if x&gt;0 =&gt; Empty m gallon jug.
6. (x,0), if y&gt;0 =&gt; Empty n gallon jug.
7. (m,y-(m-x)), if x+y&lt;m+n =&gt; Pour some water from the n gallon jug to fill the m gallon jug.
8. (x-(n-y),n), if x+y&lt;m+n =&gt; Pour some water from the m gallon jug to fill the n gallon jug.
9. (x+y,0), if x+y&lt;m =&gt; Pour all water from n gallon jug to m gallon jug.
10. (0,x+y), if x+y&lt;n =&gt; Pour all water from m gallon jug to n gallon jug.

# Algorithm
- Step 1: Start.
- Step 2: Read the capacities of jug 1 and jug 2 from the user and store it in the variable jug1 and jug2.
- Step 3: Read the amount of water to be present in the second jug and store it in the variable ‘aim’.
- Step 4: Create a function ‘WaterJugSolver’ with parameters ‘amt1’ and ‘amt2’.
- Step 5: Within the function ‘WaterJugSolver’, apply the rules to solve the water jug problem and display the paths through which the problem is solved.

# Solution
- waterjug.py
- waterjug.png
