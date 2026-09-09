a, b, c, d, e = map(int, input().split())

card_sets = set([a, b, c, d, e])
card = sorted([a, b, c, d, e]) #card = Cards sorted list

def Full_house_checker():
    if card[0] == card[3] or card[1] == card[4]:
        print("NO HAND")
    else:
        print("FULL HOUSE")
    return

def Three_card_checker():
    if card[0] == card[2] or card[1] == card[3] or card[2] == card[4]:
        print("THREE CARD")
    else:
        print("TWO PAIR")
    return

if len(card_sets) == 2:
    Full_house_checker()
elif len(card_sets) == 3:
    Three_card_checker()
elif len(card_sets) == 4:
    print("ONE PAIR")
else:
    print("NO HAND")
