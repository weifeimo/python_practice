a, b, c, d, e = map(int, input().split())
set_sum = set([a, b, c, d, e])

def Three_card_checker():
    cards = sorted([a, b, c, d, e])
    if cards[0] == cards[2] or cards[1] == cards[3] or cards[2] == cards[4]:
        print("THREE CARD")
    else:
        print("TWO PAIR")
    return

if len(set_sum) == 2:
    print("FULL HOUSE")
elif len(set_sum) == 3:
    Three_card_checker()
elif len(set_sum) == 4:
    print("ONE PAIR")
else:
    print("NO HAND")
