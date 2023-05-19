def arithmetic_arranger(problems, show_answer=False):
    
  # Checking for entries more than 5
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    for problem in problems:
        # Splitting the problem into different parts
        operand1, operator, operand2 = problem.split()

        # Checking for the right operators(+/-)
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Checking if the strings are digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if the digits are more than 4
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Finding the sum or subtraction
        if operator == '+':
            answer = int(operand1) + int(operand2)
        else:
            answer = int(operand1) - int(operand2)

        # Create the arranged problem
        width = max(len(operand1), len(operand2)) + 2
        arranged_operand1 = operand1.rjust(width)
        arranged_operand2 = operator + ' ' + operand2.rjust(width-2)
        arranged_dashes = '-' * width
        arranged_answer = str(answer).rjust(width) if show_answer else ''

        arranged_problems.append([arranged_operand1, arranged_operand2, arranged_dashes, arranged_answer])

    # Join the arranged problems horizontally
    arranged_lines = []
    for line in zip(*arranged_problems):
        arranged_lines.append('    '.join(line))

    # Join the arranged lines vertically
    arranged_string = '\n'.join(arranged_lines)

    return arranged_string