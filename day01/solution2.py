list = [(line[0], int(line[1:].strip())) for line in open('input.txt', 'r')]

curr = 50
pw = 0
for dir, val in list:
  pw += val // 100
  val %= 100
  if val == 0:
    continue
  if curr == 0:
    curr = val if dir == 'R' else 100 - val
    continue

  temp = (curr + val) if dir == 'R' else (curr - val)
  if temp == 0:
    pw += 1
    curr = temp
  elif temp > 0:
    pw += temp // 100
    curr = temp % 100
  else: # temp < 0
    temp = abs(temp)
    pw += temp // 100
    pw += 1
    curr = 100 - (temp % 100)
print(pw)