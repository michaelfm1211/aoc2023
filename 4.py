from collections import defaultdict

pts = 0
copies = defaultdict(lambda: 1)
for i, line in enumerate(open('4.txt')):
    winning_txt, ours_txt = line.strip().split(': ')[1].split(' | ')
    winning = {int(num) for num in winning_txt.split(' ') if num != ''}
    ours = [int(num) for num in ours_txt.split(' ') if num != '']

    copies_of_this = copies[i]  # do this outside of the loop to register
    won = sum(1 for num in ours if num in winning)
    for j in range(won):
        # for every copy of this card, add a new card for our winnings
        copies[i + j + 1] += copies_of_this
print(sum(copies.values()))
