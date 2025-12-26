input = [line.strip().split() for line in open('input.txt', 'r')]

sum = 0
temp = 1
for i in range(len(input[0])):
  for j in range(len(input)-1):
    if input[-1][i] == '+':
      sum += int(input[j][i])
    else:
      temp *= int(input[j][i])
  if input[-1][i] == '*':
    sum += temp
    temp = 1

print(sum)