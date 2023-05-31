def arithmetic_arranger(problems, show_answers=False):
  # error1
  if len(problems) > 5:
    return "Error: Too many problems."

  # strings
  st_1 = ""
  nd_2 = ""
  rd_3 = ""
  th_4 = ""
  arranged_problems = ""

  for problem in problems:
    problem_spt = problem.split()
    # error2
    if problem_spt[1] == "+" or problem_spt[1] == "-":
      operator = problem_spt[1]
    else:
      return ("Error: Operator must be '+' or '-'.")
    # error3
    try: 
      num1 = int(problem_spt[0])
      num2 = int(problem_spt[2])
    except:
      return "Error: Numbers must only contain digits."
    # error4
    if len(problem_spt[0]) > 4 or len(problem_spt[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    # dashes
    if len(problem_spt[0]) + 2 > len(problem_spt[2]) + 2:
      dash_size = len(problem_spt[0]) + 2
    else: 
      dash_size = len(problem_spt[2]) + 2
      
    # operations
    if operator=="+":
      result = num1+num2
    else: 
      result = num1-num2

    # visualization
    line_1 = str(num1).rjust(dash_size)
    line_2 = str(num2).rjust(dash_size-1)
    dash_line="-" * dash_size
    line_4 = str(result).rjust(dash_size)

    if problem != problems[-1]:
      st_1 += line_1 + "    "
      nd_2 += operator + line_2 + "    "
      rd_3 += dash_line + "    "
      th_4 += line_4 + "    "
    else:
      st_1 += line_1
      nd_2 += operator + line_2
      rd_3 += dash_line
      th_4 += line_4

  # the end
  if show_answers == True:
    arranged_problems = st_1 +'\n'+ nd_2 +'\n'+ rd_3 +'\n'+ th_4
  else: 
    arranged_problems = st_1 +'\n'+ nd_2 +'\n'+ rd_3

  return arranged_problems
