import random
import math

SUITS = {
    "B": "Bamboos",
    "C": "Characters",
    "D": "Dots"
}

SIMULATIONS = 1000


def evaluate(hand, suit):
    """
    Reward function.
    Fewer tiles in the chosen suit = higher reward.
    """
    count = sum(tile.startswith(suit) for tile in hand)

    # reward range 0..13
    return 13 - count


def solve(hand):
    visits = {suit: 0 for suit in SUITS}
    rewards = {suit: 0.0 for suit in SUITS}

    for _ in range(SIMULATIONS):

        # Selection (simple UCB1)
        total_visits = sum(visits.values()) + 1

        best_suit = None
        best_ucb = float("-inf")

        for suit in SUITS:

            if visits[suit] == 0:
                best_suit = suit
                break

            avg_reward = rewards[suit] / visits[suit]

            ucb = avg_reward + math.sqrt(
                2 * math.log(total_visits) / visits[suit]
            )

            if ucb > best_ucb:
                best_ucb = ucb
                best_suit = suit

        # Simulation
        reward = evaluate(hand, best_suit)

        # Backpropagation
        visits[best_suit] += 1
        rewards[best_suit] += reward

    best_suit = max(
        SUITS.keys(),
        key=lambda s: rewards[s] / max(visits[s], 1)
    )

    cost = sum(tile.startswith(best_suit) for tile in hand)

    return {
        "algorithm": "Monte Carlo Tree Search",
        "voided_suit": SUITS[best_suit],
        "suit_code": best_suit,
        "cost": cost,
        "tiles_to_discard": [
            tile for tile in hand if tile.startswith(best_suit)
        ],
        "simulations": SIMULATIONS
    }