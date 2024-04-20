#Q12) Crypt Arithmetic Problem 
from typing import Iterable
from itertools import permutations
import re

Formula = str  # A formula in Math notation, like "NUM ^ BER = PLAY"
Pformula = str  # A formula in Python notation, like "NUM ** BER == PLAY"
Solution = str  # A formula with letters replaced by digits, like "356 + 742 = 1098"

def solve(formula) -> Iterable[Solution]:
    letters = all_letters(formula)  # Get all unique letters from the formula
    pformula = to_python(formula)  # Convert the formula to Python notation
    for digits in permutations('1234567890', len(letters)):  # Iterate through all permutations of digits for the letters
        if valid(subst(digits, letters, pformula)):  # Check if the substituted formula is valid
            yield format_solution(subst(digits, letters, formula), digits)  # If valid, yield the solution in the desired format

def subst(digits, letters, formula) -> Formula:
    return formula.translate(str.maketrans(letters, cat(digits)))  # Substitute letters with digits

def valid(pformula) -> bool:
    try:
        return (not leading_zero(pformula)) and (eval(pformula) is True) # Check if the pformula has no leading zero and evaluates to True
    except ArithmeticError:
        return False

def to_python(formula: Formula) -> Pformula:
    return formula.replace(' = ', ' == ').replace('^', '**')  # Convert mathematical symbols to Python operators eg. = to ==

def all_letters(formula: str) -> str:
    return cat(sorted(set(re.findall('[A-Z]', formula))))  # Get all unique letters in the form of an alphabetized string and sort them

def format_solution(formula, digits) -> Solution:
    return formula.format(*digits)

def first(iterable): "First element"; return next(iter(iterable), None)

cat = ''.join  # Function to concatenate strings

leading_zero = re.compile(r'\b0[0-9]').search  # Regular expression to check for leading zero

solution = first(solve('SEND + MORE = MONEY'))  # Get the first solution found
if solution:
    print("SEND + MORE = MONEY\n" + solution)  # Print the formula along with the solution in the desired format
else:
    print("No solution found.")
