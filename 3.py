from string import digits

# part 1

# parse each line into a list of numbers and symbols, and their positions in
# the line
nums = []
symbols = []
for lineno, line in enumerate(open('3.txt')):
    nums.append([])
    symbols.append([])

    num = ''
    num_start_pos = 0
    for i, ch in enumerate(line):
        if ch in digits:
            if num == '':
                # start of a new number
                num_start_pos = i
            num += ch
        elif num != '':
            # end of a number
            nums[-1].append((int(num), range(num_start_pos - 1, i + 1)))
            num = ''

        if ch not in digits and ch != '.' and ch != '\n':
            symbols[-1].append(i)

# go over symbols and add up numbers that are adjacent
total = 0
for lineno, line in enumerate(symbols):
    for symbol in line:
        for y in range(lineno - 1 if lineno > 0 else lineno, lineno + 2):
            for num in nums[y]:
                if symbol in num[1]:
                    total += num[0]
print(total)

# part 2

sum_ratios = 0
for lineno, line in enumerate(symbols):
    for symbol in line:
        adj_nums = []
        for y in range(lineno - 1 if lineno > 0 else lineno, lineno + 2):
            for num in nums[y]:
                if symbol in num[1]:
                    adj_nums.append(num[0])
        if len(adj_nums) == 2:
            sum_ratios += adj_nums[0] * adj_nums[1]
print(sum_ratios)
