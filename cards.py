import random
card1=random.randint(0,13)
card2=random.randint(0,13)
if card2==card1:
    card2=random.randint(0,13)
card3=random.randint(0,13)
if card3==card1 or card3==card2:
    card3=random.randint(0,13)
card4=random.randint(0,13)
if card4==card1 or card4==card2 or card4==card3:
    card4=random.randint(0,13)
card5=random.randint(0,13)
if card5==card1 or card5==card2 or card5==card3 or card5==card4:
    card5=random.randint(0,13)
print(str(card1),str(card2),str(card3),str(card4),str(card5))