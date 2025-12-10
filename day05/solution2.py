input = [line.strip() for line in open('input.txt')]
ranges = [tuple(map(int, r.split('-'))) for r in input[:input.index('')]]

n = 0
changed = False
newrange = (-1, -1)
remove = (-1, -1)
while True:
  if len(ranges) < 2:
    break
  for i in range(len(ranges)):
    minI, maxI = ranges[i]
    for j in range(i+1, len(ranges)):
      minJ, maxJ = ranges[j]
      if minJ <= maxI and minJ >= minI and maxJ >= maxI: # right overlap
        newrange = (minI, maxJ)
        changed = True
        remove = (i, j)
        break
      elif minJ <= minI and maxJ >= minI and maxJ <= maxI: # left overlap
        newrange = (minJ, maxI)
        changed = True
        remove = (i, j)
        break
      elif minJ >= minI and maxJ <= maxI: # j fully in i
        newrange = (minI, maxI)
        changed = True
        remove = (i, j)
        break
      elif minJ <= minI and maxJ >= maxI: # i fully in j
        newrange = (minJ, maxJ)
        changed = True
        remove = (i, j)
        break

    if changed:
      break

  # no updates to the whole list
  if not changed:
    break

  ranges.pop(remove[1])
  ranges.pop(remove[0])
  ranges.append(newrange)
  changed = False
  remove = (-1, -1)
  newrange = (-1, -1)

for (min, max) in ranges:
  n += 1 + (max - min)
print(n)
