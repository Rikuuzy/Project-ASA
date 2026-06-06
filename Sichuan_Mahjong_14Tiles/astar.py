import heapq

SUITS = {
    "B": "Bamboos",
    "C": "Characters",
    "D": "Dots"
}

def g_cost(hand, suit):
    # Actual cost: number of tiles that must be removed
    return sum(tile.startswith(suit) for tile in hand)

def heuristic(hand, suit):
    # For this simple problem, estimated remaining cost is 0
    # because choosing a suit immediately reaches the goal.
    return 0

def solve(hand):
    frontier = []

    for suit in SUITS:
        g = g_cost(hand, suit)
        h = heuristic(hand, suit)
        f = g + h

        heapq.heappush(frontier, (f, g, suit))

    best_f, best_g, best_suit = heapq.heappop(frontier)

    return {
        "algorithm": "A* Search",
        "voided_suit": SUITS[best_suit],
        "suit_code": best_suit,
        "cost": best_g,
        "tiles_to_discard": [
            tile for tile in hand if tile.startswith(best_suit)
        ]
    }