# Silent Auction

The Silent Auction project is a simple Python script that simulates an auction where multiple users can place bids. The bids are stored in a dictionary, and at the end of the auction, the program calculates and announces the highest bidder. This project demonstrates basic input handling, loops, and dictionary usage in Python.

**Features:**
- **Bid Entry:** Users can enter their name and bid amount to participate in the auction.
- **Multiple Bidders:** The program supports multiple users, allowing each to place a bid before determining the winner.
- **Highest Bidder Calculation:** The script calculates the highest bid from the collected bids and announces the winner.
- **Input Validation:** The program ensures that users provide valid inputs for bidding and whether to continue the auction.

**Note**: This project was inspired by Angela Yu's course on Udemy.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### How to Use

1. Clone or download the repository to your local machine.
2. Run the script using Python:

   ```bash
   python silent_auction.py
   ```

3. Follow the on-screen prompts to:
   - Enter your name and bid amount.
   - Indicate whether there are other users who want to place a bid.
   - Continue the auction until all bids are placed.

4. The program will determine the highest bid and announce the winner.

### Customization

You can customize the Silent Auction by:
- **Modifying the Artwork:** Change the `logo` in the `silentauctionart.py` file to display different artwork at the start of the auction.
- **Adding Bid Validations:** Implement additional checks to ensure that bid amounts are valid (e.g., positive numbers).
- **Enhancing the User Interface:** Add more features like displaying all bids at the end or allowing users to re-bid.
