import math
from art import logo
def find_heighest_bidder(record):
    heighest = -math.inf
    for key in record:
        if (heighest < record[key]):
            heighest = record[key]
            bidder = key
    print(bidder,heighest)
bid_record = {}
another_bid = True
while another_bid:
    print(logo)
    name = input('Enter Name: ').lower()

    bid = int(input('Enter Bid: '))
    
    bid_record[name] = bid
    
    new_another_bid = input('Want another bid: ').lower()
    
    if new_another_bid == 'no':
        another_bid = False
        find_heighest_bidder(bid_record)

#print(bid_record)
