#blind-auction
from art import blind_auction_logo
import os

# first method
'''print(blind_auction_logo)
should_continue_bid = True
bid_dict = {}
while should_continue_bid:
    name = input("Enter User name: ")
    bid = float(input("Enter bid price: $"))
    bid_dict[name] = bid
    print(bid_dict)
    another_bid = input("Type 'yes' if there are other users for bidding, otherwise 'no': ")
    if another_bid == 'yes':
        os.system('cls')
    
    else:
        should_continue_bid = False
        higgest_bid = 0
        for price in bid_dict:
            bid_price = bid_dict[price]
            if bid_price > higgest_bid:
                higgest_bid = bid_price
        print(higgest_bid)
        print("winner")'''

#find higgest 
'''bid = {
    'hardeep': 78,
    'neetu': 200,
    'riya': 15
}
high = 0
for bid_price in bid:
    price = bid[bid_price]
    #print(price)
    if price>high:
        high = price
print(high)'''

#second method
print(blind_auction_logo)
bid_dict =  {}
def higgest_bid(bid_dict):
    higgest_bid = 0
    winner = 0
    for price in bid_dict:
        bid_price = bid_dict[price]
        if bid_price > higgest_bid:
            higgest_bid = bid_price
            winner = price
    print(f"The winner is {winner} with a bid of ${higgest_bid}")

should_continue_bid = True
while should_continue_bid:
    name = input("Enter User name: ")
    bid = float(input("Enter bid price: $"))
    bid_dict[name] = bid
    print(bid_dict)
    another_bid = input("Type 'yes' if there are other users for bidding, otherwise 'no': ")
    if another_bid == 'yes':
        os.system('cls')
    
    else:
        should_continue_bid = False
        higgest_bid(bid_dict)

