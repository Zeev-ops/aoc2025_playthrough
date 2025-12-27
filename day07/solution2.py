input = [list(s.strip()) for s in open('input.txt', 'r')]

def add_new_item(next_checks_dict: dict, pos: int, count: int):
  if pos in next_checks:
    next_checks_dict[pos] += count
  else:
    next_checks_dict[pos] = count

curr_checks = {input[0].index('S'): 1}
for i in range(1, len(input)):
  next_checks = {}
  for pos, count in curr_checks.items():
    if input[i][pos] == '^':
      if pos-1 >= 0:
        add_new_item(next_checks, pos-1, count)
      if pos+1 < len(input[i]):
        add_new_item(next_checks, pos+1, count)
    else:
      add_new_item(next_checks, pos, count)
  curr_checks = next_checks

print(sum(curr_checks.values()))
