SUITS = {
    "B": "Bamboos",
    "C": "Characters",
    "D": "Dots"
}

def solve(hand):
    """
    Dynamic Programming approach.
    Store the computed cost of each suit so it is not recalculated.
    """

    dp = {}

    for suit in SUITS:
        dp[suit] = sum(tile.startswith(suit) for tile in hand)

    best_suit = min(dp, key=dp.get)
    best_cost = dp[best_suit]

    return {
        "algorithm": "Dynamic Programming",
        "voided_suit": SUITS[best_suit],
        "suit_code": best_suit,
        "cost": best_cost,
        "tiles_to_discard": [
            tile for tile in hand if tile.startswith(best_suit)
        ],
        "dp_table": dp
    }