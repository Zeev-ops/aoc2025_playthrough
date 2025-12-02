t = open('input.txt', 'r').read().strip().split(',')
t = [line.split('-') for line in t]

def check_string(a):
  temp_sum = 0
  earlyStop = False
  for i in range(0, len(a)//2):
    i += 1
    if len(a) % i != 0:
      continue
    for j in range(i, len(a), i):
      pat = a[:i]
      if a[j:j+i] != pat:
        break
    else:
      temp_sum += int(a)
      earlyStop = True
    if earlyStop:
      earlyStop = False
      break
  return temp_sum

sum = 0
for a, b in t:
  while a != b:
    sum += check_string(a)
    a = str(int(a)+1)
  sum += check_string(b)
print(sum)