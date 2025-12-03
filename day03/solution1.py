banks = [bank.strip() for bank in open('input.txt')]

sum = 0
for b in banks:
  first_num, second_num = 0, 0
  for i, num in enumerate(b):
    num = int(num)
    if first_num < num and i < len(b)-1:
      first_num = num
      second_num = 0
      continue

    if second_num < num:
      second_num = num
  sum += first_num * 10 + second_num

print(sum)