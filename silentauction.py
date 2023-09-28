from silentauctionart import logo
print(logo)

bids = {}

def find_highest_bidder(total_bids):
    h_bid = 0
    for bidder in total_bids:
        b = int(total_bids[bidder])
        if b > h_bid:
            h_bid = b
            winner = bidder
            print(f"The winner is {winner} with a bid amount of ${h_bid}")


not_bid_again = True
while not_bid_again:
    name = input("What is your name? \n")
    bid = input("What is your bid price? \n$")
    bids[name] = bid

    yes_no = True
    while yes_no:
        go_again = input("Are there other users who want to bid? 'yes' or 'no'\n").lower()
        if go_again == 'yes' or go_again == 'no':
            if go_again == 'no':
                find_highest_bidder(bids)
                yes_no = False
                not_bid_again = False
            else:
                yes_no = False
        else:
            print("Wrong input.")
