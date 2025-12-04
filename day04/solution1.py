dia = [line.strip() for line in open('input.txt')]

sum = 0
for i in range(len(dia)):
  for j in range(len(dia[i])):
    neighbours = 0
    if dia[i][j] != '@':
      continue
    for x in [-1, 0, 1]:
      for y in [-1, 0, 1]:
        if x == 0 and y == 0:
          continue
        if i+y < 0 or i+y >= len(dia) or j+x < 0 or j+x >= len(dia[i]):
          continue
        if dia[i+y][j+x] == '@':
          neighbours += 1
    if neighbours < 4:
      sum += 1

print(sum)
