import heapq

SUITS = {
    "B": "Bamboos",
    "C": "Characters",
    "D": "Dots"
}

def heuristic(hand, suit):
    return sum(tile.startswith(suit) for tile in hand)

def solve(hand):
    frontier = []

    for suit in SUITS:
        h = heuristic(hand, suit)
        heapq.heappush(frontier, (h, suit))

    best_h, best_suit = heapq.heappop(frontier)

    return {
        "algorithm": "Greedy Best-First Search",
        "voided_suit": SUITS[best_suit],
        "suit_code": best_suit,
        "cost": best_h,
        "tiles_to_discard": [
            tile for tile in hand if tile.startswith(best_suit)
        ]
    }