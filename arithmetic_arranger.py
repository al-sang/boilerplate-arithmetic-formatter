# '''     '   32         1      45      123      988\n'
#         '- 698    - 3801    + 43    +  49    +  40\n'
#         '-----    ------    ----    -----    -----\n'
#         ' -666     -3800      88      172     1028',
# '''


def arithmetic_arranger(problems, solve=False):
    parsed_problems = [problem.split(' ') for problem in problems]
    operators = [problem[1] for problem in parsed_problems]
    numbers = [problem[0::2] for problem in parsed_problems]

    if len(parsed_problems) > 5:
        return 'Error: Too many problems.'

    for sign in operators:
        if ((sign.strip() != '+') and (sign.strip() != '-')):
            return "Error: Operator must be '+' or '-'."

    for pair in numbers:
        for number in pair:
            if not number.isnumeric():
                return 'Error: Numbers must only contain digits.'

            elif len(number) > 4:
                return 'Error: Numbers cannot be more than four digits.'

    answers = [problem for problem in parsed_problems]

    for index, problem in enumerate(parsed_problems):
        if problem[1].strip() == "+":
            answers[index].append(int(problem[0]) + int(problem[2]))
        else:
            answers[index].append(int(problem[0]) - int(problem[2]))

    return ''
