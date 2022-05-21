import random

heads = 0
tails = 0

def coinFlip(number):
    global heads 
    global tails
    for i in range(number):
        flip = random.randint(1,2)
        if flip == 1:
            heads += 1
        else:
            tails += 1
        
    print('Total No of HEADS: ',heads)
    print('Total No Of TAILS: ',tails)

    print('Total FLIPS: ',i+1)

coinFlip(34983)