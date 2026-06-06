import heapq

SUITS = {
    "B": "Bamboos",
    "C": "Characters",
    "D": "Dots"
}

def solve(hand):
    priority_queue = []

    for suit in SUITS:
        cost = sum(tile.startswith(suit) for tile in hand)
        heapq.heappush(priority_queue, (cost, suit))

    best_cost, best_suit = heapq.heappop(priority_queue)

    return {
        "algorithm": "Uniform Cost Search",
        "voided_suit": SUITS[best_suit],
        "suit_code": best_suit,
        "cost": best_cost,
        "tiles_to_discard": [
            tile for tile in hand if tile.startswith(best_suit)
        ]
    }