import re

def arithmetic_arranger(problems, evaluate = False):
    max_lengths = [len(max(problem.split(), key=len)) for problem in problems]
    arranged_problems = None
    operands = [ problem.split()[::2] for problem in problems ]
    operators = [ problem.split()[1] for problem in problems ] 

    if len(problems) > 5:
        arranged_problems = 'Error: Too many problems.'
        return arranged_problems
    if re.findall(r'[^+-]', ''.join(operators)):
        arranged_problems = "Error: Operator must be '+' or '-'."
        return arranged_problems
    if not all(item.isdigit() for item in [ part for piece in operands for part in piece ]):
        arranged_problems = 'Error: Numbers must only contain digits.'
        return arranged_problems
    if not all(len(item) < 5 for item in [ part for piece in operands for part in piece ]):
        arranged_problems = 'Error: Numbers cannot be more than four digits.'
        return arranged_problems
    
    answers = [ str(eval(problem)) for problem in problems ]
    top_row = ''
    bottom_row = ''
    divider_row = ''
    solutions_row = ''

    # Format construction:
    for i in range(len(operands)):
        top_row += operands[i][0].rjust(max_lengths[i] + 2)
        bottom_row += (operators[i] + operands[i][1].rjust(max_lengths[i] + 1)) 
        divider_row += '-' * (max_lengths[i] + 2)
        solutions_row += answers[i].rjust(max_lengths[i] + 2)
        
        if i != len(operands) - 1:
            equation_separator = ' ' * 4
            top_row += equation_separator
            bottom_row += equation_separator
            divider_row += equation_separator
            solutions_row += equation_separator
    
    if evaluate:
        arranged_problems = '\n'.join((top_row, bottom_row, divider_row, solutions_row))
    else: 
        arranged_problems = '\n'.join((top_row, bottom_row, divider_row))

    return arranged_problems
