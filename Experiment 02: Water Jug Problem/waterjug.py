from collections import defaultdict 
visited = defaultdict(lambda: False)

def waterJugSolver(amt1, amt2): 
	# Returns true if goal achieved.
	if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
		print(amt1, amt2)
		return True
	
	# Checks if combination visited. If not, proceed.
	if visited[(amt1, amt2)] == False:
		print(amt1, amt2)
	
		# Changes the boolean value of the combination as it is visited. 
		visited[(amt1, amt2)] = True
	
		# Check for all the 6 possibilities and see if a solution is found in any one of them.
		return (waterJugSolver(0, amt2) or
				waterJugSolver(amt1, 0) or
				waterJugSolver(jug1, amt2) or
				waterJugSolver(amt1, jug2) or
				waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
				amt2 - min(amt2, (jug1-amt1))) or
				waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
				amt2 + min(amt1, (jug2-amt2))))
	
	# Return False if the combination is already visited to avoid repetition otherwise recursion will enter an infinite loop.
	else:
		return False

jug1=int(input("Kindly enter capacity of jug1: "))
jug2=int(input("Kindly enter capacity of jug2: "))
aim=int(input("Kindly enter the desired aim for jug2: "))
print("\nSteps: ")
waterJugSolver(0, 0)
