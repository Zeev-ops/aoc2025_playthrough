import math

input = [line.replace('\n', '') for line in open('input.txt', 'r')]
operators = list(input.pop(len(input)-1).replace(' ', ''))

max = max(len(s) for s in input)
input = [s.ljust(max) for s in input]

result = 0
con = []
for i in range(len(input[0])-1, -1, -1):
  curr_number = ''
  for j in range(len(input)):
    curr_number += input[j][i]
  curr_number = curr_number.strip()
  if curr_number:
    con.append(int(curr_number))
    curr_number = ''
  else:
    operator = operators.pop()
    if operator == '+':
      result += sum(con)
    else:
      result += math.prod(con)
    con = []

operator = operators.pop()
if operator == '+':
  result += sum(con)
else:
  result += math.prod(con)
con = []

print(result)





