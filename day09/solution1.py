red_tiles = [list(map(int, s.strip().split(','))) for s in open('input.txt', 'r')]

highest = 0
for i, [t1x, t1y] in enumerate(red_tiles):
  for t2x, t2y in red_tiles[i+1:]:
    curr = (abs(t1x - t2x)+1) * (abs(t1y - t2y)+1)
    if curr > highest:
      highest = curr

print(highest)