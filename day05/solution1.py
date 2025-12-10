input = [line.strip() for line in open('input.txt')]
at = input.index('')
ranges, list = input[:at], input[at+1:]

list = [int(i) for i in list]
ranges = [tuple(map(int, r.split('-'))) for r in ranges]

n = 0
for item in list:
  for (min, max) in ranges:
    if item >= min and item <= max:
      n += 1
      break

print(n)
