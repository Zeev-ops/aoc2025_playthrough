banks = [bank.strip() for bank in open('input.txt')]

sum = 0
for b in banks:
  numbers = [0] * 12
  for i, num in enumerate(b):
    num = int(num)
    for j in range(len(numbers)):
      if numbers[j] < num and i < len(b)-(len(numbers)-j-1):
        numbers[j] = num
        for k in range(j+1, len(numbers)):
          numbers[k] = 0
        break
  sum += int(''.join(map(str, numbers)))

print(sum)