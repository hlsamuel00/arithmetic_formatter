def arithmetic_arranger(problems, evaluate = False):
  # Error Checking: If the length of problems is greater than 5, return an error.
  if len(problems) > 5:
    return 'Error: Too many problems.'

  # Initialize the lists to hold the operands, operators, and answers for later use. 
  operands, operators, answers = [], [], []

  # Iterate through each problem and extract the numbers for each line and the operators. Return an error if the operand isn't '+' or '-', if there are characters outside of digits and the two operators, and if the length of a number is greater than 4 digits.
  for problem in problems:
    new_string, max_length = [], 0
    temp_operands = []
    for idx,char in enumerate(problem):
      if char in 'x/':
        return "Error: Operator must be '+' or '-'."

      if char.isalpha():
        return "Error: Numbers must only contain digits."

      if char.isdigit():
        new_string.append(char)

      if char in '+-':
        operators.append(char)

      if new_string and (char == ' ' or idx == len(problem)-1):
        if len(new_string) > 4:
          return 'Error: Numbers cannot be more than four digits.'
        else:
          temp_operands.append(''.join(new_string))
          max_length = max(max_length, len(new_string))
          new_string = []

    operands.append([operand.rjust(max_length + (2 - idx)) for idx, operand in enumerate(temp_operands)])
    answers.append(str(eval(problem)).rjust(max_length + 2))

  # Initialize our top row, bottom row, divider row, and solutions row lists. Also initialize our equation divider.
  top_row, bottom_row, divider_row, solutions_row = [], [], [], []
  equation_divider = ' ' * 4

  # Iterate for each problem and assemble each row for later use. Each row contains one element from the 3 lists created above. The divider row will be the length of the bottom_row element.
  for i in range(len(problems)):
    top_row.append(operands[i][0])
    bottom_row.append(operators[i] + operands[i][1])
    divider_row.append('-' * len(bottom_row[-1]))
    solutions_row.append(answers[i])

  # Initialize our return output as an empty list.
  arranged_problems = []

  # Iterate over each of the rows and combine the values in the list with the equation separator. Each value in the row list is a separate equation. 
  for row in (top_row, bottom_row, divider_row, solutions_row):
    arranged_problems.append(equation_divider.join(row))

  # If evaluate is False, remove the solutions row (last row in the arranged problems list)
  if not evaluate:
    arranged_problems = arranged_problems[:-1]

  # Return a string of each row separated on each line.
  return '\n'.join(arranged_problems)
