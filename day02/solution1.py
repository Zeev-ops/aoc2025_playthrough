t = open('input.txt', 'r').read().strip().split(',')
t = [line.split('-') for line in t]

sum = 0
for a, b in t:
  while a != b:
    mid = len(a) //2
    if a[0:mid] == a[mid:]:
      sum += int(a)
    a = str(int(a)+1)
  if b[0:len(b)//2] == b[len(b)//2:]:
    sum += int(b)
print(sum)