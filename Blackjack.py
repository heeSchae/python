def next_move(string):
    
    total = 0
    A = False
    
    for card in string:
        if card == "J" or card == "K" or card == "Q" or card == "0":
            total += 10
           
        
        elif card.isdigit():
            total += int(card)
           
        else:
            A = True
    if A:
        if total >= 6 and total <= 10:
            total += 11
        elif total >10:
            total += 1
    
    if total <17:
        return "Hit"
    elif total >=17 and total <= 21:
        return "Stay"
    elif total > 21:
        return "Bust"
    
