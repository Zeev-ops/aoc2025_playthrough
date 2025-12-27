input = [s.strip() for s in open('input.txt', 'r')]

num_splits = 0
curr_checks = {input[0].find('S')}
for i in range(1, len(input)-1):
  next_checks = set()
  for pos in curr_checks:
    if input[i][pos] == '^':
      num_splits += 1
      if pos-1 >= 0:
        next_checks.add(pos-1)
      if pos+1 < len(input[i]):
        next_checks.add(pos+1)
    else:
      next_checks.add(pos)
  curr_checks = next_checks
print(num_splits)
