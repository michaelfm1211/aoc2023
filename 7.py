# this is kind of messy code, but it works

# part 1

lookup = {'2': 'a', '3': 'b', '4': 'c', '5': 'd', '6': 'e', '7': 'f', '8': 'g',
          '9': 'h', 'T': 'i', 'J': 'j', 'Q': 'k', 'K': 'l', 'A': 'm'}


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    def val(self):
        '''Assign each card a unique 6 character string for sorting'''

        # calculate the rank
        freq_dict = {}
        for card in self.cards:
            if card not in freq_dict:
                freq_dict[card] = 0
            freq_dict[card] += 1
        freq = freq_dict.values()
        if 5 in freq:
            self.rank = 6
        elif 4 in freq:
            self.rank = 5
        elif 3 in freq and 2 in freq:
            self.rank = 4
        elif 3 in freq:
            self.rank = 3
        elif sum(1 for x in freq if x == 2) == 2:
            self.rank = 2
        elif 2 in freq:
            self.rank = 1
        else:
            self.rank = 0

        # create a string that will sort the cards alphabetically
        self.card_rep = ''.join(lookup[card] for card in self.cards)

        return f'{self.rank}{self.card_rep}'

    def __repr__(self):
        return f'{self.cards}\t{self.bid}\t{self.val()}'


hands = []
for line in open('7.txt'):
    parts = line.strip().split(' ')
    hands.append(Hand(parts[0], int(parts[1])))

hands.sort(key=lambda hand: hand.val())
# print(*(hand for hand in hands), sep='\n')
win = sum((i + 1) * hand.bid for i, hand in enumerate(hands))
print(win)

# part 2

lookup['J'] = '0'


def part2_val(self):
    jokers = 0
    freq_dict = {}
    for card in self.cards:
        if card == 'J':
            jokers += 1
            continue
        if card not in freq_dict:
            freq_dict[card] = 0
        freq_dict[card] += 1
    freq = freq_dict.values()

    try:
        max_freq = max(freq)
        pairs = sum(1 for x in freq if x == 2)
    except ValueError:
        # this only fails if freq_dict is empty because its all jokers
        max_freq = 0
        pairs = 0

    if max_freq + jokers == 5:
        self.rank = 6
    elif max_freq + jokers == 4:
        self.rank = 5
    elif (3 in freq and 2 in freq) or (pairs + jokers == 3):
        self.rank = 4
    elif max_freq + jokers == 3:
        self.rank = 3
    elif pairs + jokers == 2:
        self.rank = 2
    elif max_freq + jokers == 2:
        self.rank = 1
    else:
        self.rank = 0

    self.card_rep = ''.join(lookup[card] for card in self.cards)
    return f'{self.rank}{self.card_rep}'


Hand.val = part2_val
hands.sort(key=lambda hand: hand.val())
# print(*(hand for hand in hands), sep='\n')
win = sum((i + 1) * hand.bid for i, hand in enumerate(hands))
print(win)
