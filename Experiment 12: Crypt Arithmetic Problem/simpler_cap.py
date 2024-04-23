# Q12) Crypt Arithmetic Problem
def evaluate(word, assigned):
    num = 0
    for char in word:
        if char in assigned:
            num = num * 10 + int(assigned[char])
        else:
            return None
    return num

def _solve(word1, word2, result, letters, assigned, solutions):
    if len(letters) == 0:
        if evaluate(word1, assigned) + evaluate(word2, assigned) == evaluate(result, assigned): 
            solutions.append(dict(assigned))
        return

    if len(result) > max(len(word1), len(word2)) + 1 or len(letters) > 10:
        return

    for i in range(10):
        num = str(i)
        if num not in assigned.values():
            cur_letter = letters.pop()
            assigned[cur_letter] = num
            if (word1[0] in assigned and assigned[word1[0]] == '0') or \
               (word2[0] in assigned and assigned[word2[0]] == '0') or \
               (result[0] in assigned and assigned[result[0]] == '0'):
                letters.append(cur_letter)
                del assigned[cur_letter]
                continue
            _solve(word1, word2, result, letters, assigned, solutions)
            del assigned[cur_letter]
            letters.append(cur_letter)

def solve(word1, word2, result):
    letters = list(set(word1 + word2 + result))  
    assigned = {}  
    solutions = []  

    _solve(word1, word2, result, letters, assigned, solutions)

    print("CRYPTARITHMETIC PUZZLE SOLVER")
    if solutions:
        solution = solutions[0]
        print(solution)
        # Display in the requested format
        print(f"{word1}({''.join([solution[char] for char in word1])}) + {word2}({''.join([solution[char] for char in word2])}) = {result}({''.join([solution[char] for char in result])})")
    else:
        print("No solution found.")

# Example usage:
solve('SEND', 'MORE', 'MONEY')
