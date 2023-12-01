# part a
s = 0
for line in open('1.txt'):
    digits = [int(d) for d in line.strip() if d.isdigit()]
    s += digits[0] * 10 + digits[-1]
print(s)

# part b
nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
        'eight', 'nine']
s = 0
for line in open('1.txt'):
    line = line.strip()
    digits = []
    for i, ch in enumerate(line):
        if ch.isdigit():
            digits.append(int(ch))
        else:
            for val, num in enumerate(nums):
                if line[:i+1][-len(num):] == num:
                    digits.append(val)
    s += digits[0] * 10 + digits[-1]
print(s)
