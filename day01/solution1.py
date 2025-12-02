list = [(line[0], int(line[1:].strip())) for line in open('input.txt', 'r')]

curr = 50
pw = 0
for dir, val in list:
  curr = (curr + val) if dir == 'R' else (curr - val)
  curr %= 100
  if curr == 0:
    pw += 1

print(pw)