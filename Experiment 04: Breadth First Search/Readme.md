# Aim
Write a Python program to implement Breadth First Search.

# Theoretical Background
Breadth First Search is an algorithm used for traversing graphs or trees. Traversing means visiting each node of the graph. Breadth First Search is a recursive algorithm to search all the vertices of a graph or a tree. BFS in
Python can be implemented by using data structures like dictionaries and lists. Breadth First Search in tree and graph is almost the same. The only difference is that the graph may contain cycles, so we may traverse to the same node
again.

As Breadth First Search is the process of traversing each node of the graph, a standard BFS algorithm traverses each vertex of the graph, a standard BFS algorithm traverses each vertex of the graph into two parts (i) Visited and
(ii) Not Visited. So, the purpose of the algorithm is to visit all the vertices while avoiding cycles. BFS starts from a node, then it checks all the nodes at distance one from the beginning node, then it checks all the nodes at distance two and so
on. So as to recollect the nodes to be visited. BFS uses a queue. It begins at the root of the tree or graph and investigates all nodes at the current depth level before moving on to nodes at the next depth level.

# Algorithm
- Step 1: Start.
- Step 2: Read a graph from the user in the form of a dictionary and list and store it in the variable ‘graph’.
- Step 3: Initialize two lists ‘visited’ and ‘queue’.
- Step 4: Create a function ‘bfs’ and perform the following operations:
   - Step 4.1: Start by putting any one of the graph’s vertices at the back of the queue.
   - Step 4.2: Now take the front item of the queue and add it to the visited list.
   - Step 4.3: Create a list of that vertex’s adjacent nodes. Add those which are not within the visited list to the rear of the queue.
   - Step 4.4: Continue from Step 4.2 to Step 4.3, until the queue is empty.
- Step 5: Display the front item of the queue as each time it is popped out.
- Step 6: Stop.

# Solution
- bfs.py
- bfs.png
