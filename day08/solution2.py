import math

input = [list(map(int, s.strip().split(','))) for s in open('input.txt', 'r')]
size = len(input)
dist = [[0.0 for _ in range(size)] for _ in range(size)]
circuits = []

for i in range(size):
  for j in range(i):
    dist[i][j] = int(math.sqrt((input[i][0] - input[j][0])**2 + (input[i][1] - input[j][1])**2 + (input[i][2] - input[j][2])**2))

def get_min_dist(dist):
  coord = (-1, -1)
  min_value = float('inf')
  for i in range(len(dist)):
    for j in range(i):
        if dist[i][j] < min_value:
          min_value = dist[i][j]
          coord = (i, j)
  return coord

def get_max_value(circuits):
  pos = 0
  max_value = 0
  for i in range(len(circuits)):
    if len(circuits[i]) > max_value:
      max_value = len(circuits[i])
      pos = i
  return pos

components = size
while components > 1:
  min_x, min_y = get_min_dist(dist)
  con_x, con_y = -1, -1
  for i, c in enumerate(circuits):
    if input[min_x] in c:
      con_x = i
    if input[min_y] in c:
      con_y = i

  if con_x != -1 and con_x == con_y:
    dist[min_x][min_y] = float('inf')
    continue

  if con_x == -1 and con_y == -1:
    circuits.append([input[min_x], input[min_y]])
  elif con_x != -1 and con_y == -1:
    circuits[con_x].append(input[min_y])
  elif con_y != -1 and con_x == -1:
    circuits[con_y].append(input[min_x])
  elif con_x != con_y:
    circuits[con_x] = circuits[con_x] + circuits[con_y]
    circuits.pop(con_y)
  components -= 1
  dist[min_x][min_y] = float('inf')

  if components == 1:
    print(input[min_x][0] * input[min_y][0])
    break

