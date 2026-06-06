import os

from recognize_hand import recognize_hand
from ucs import solve as ucs_solve
from gbfs import solve as gbfs_solve
from astar import solve as astar_solve
from dynamic_programming import solve as dp_solve
from mcts import solve as mcts_solve


def print_result(result):
    print("\n===== RESULT =====")
    print("Algorithm:", result["algorithm"])
    print("Voided Suit:", result["voided_suit"])
    print("Suit Code:", result["suit_code"])
    print("Cost:", result["cost"])
    print("Tiles to discard:", result["tiles_to_discard"])


def choose_screenshot():
    folder = "screenshots"

    files = [
        file for file in os.listdir(folder)
        if file.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    files.sort()

    if not files:
        raise FileNotFoundError("No screenshot files found in screenshots folder.")

    print("\nChoose Screenshot Sample")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

    choice = int(input("\nEnter screenshot choice: "))

    if choice < 1 or choice > len(files):
        raise ValueError("Invalid screenshot choice.")

    return os.path.join(folder, files[choice - 1])


def choose_algorithm(hand):
    print("\nChoose Algorithm")
    print("1. Uniform Cost Search (UCS)")
    print("2. Greedy Best First Search (GBFS)")
    print("3. A* Search")
    print("4. Dynamic Programming")
    print("5. Monte Carlo Tree Search (MCTS)")

    choice = input("\nEnter choice (1-5): ")

    if choice == "1":
        return ucs_solve(hand)
    elif choice == "2":
        return gbfs_solve(hand)
    elif choice == "3":
        return astar_solve(hand)
    elif choice == "4":
        return dp_solve(hand)
    elif choice == "5":
        return mcts_solve(hand)
    else:
        raise ValueError("Invalid algorithm choice.")


def main():
    image_path = choose_screenshot()

    print("\nSelected screenshot:", image_path)

    hand = recognize_hand(image_path, show_scores=True)

    print("\nDetected Hand:")
    print(hand)

    result = choose_algorithm(hand)

    print_result(result)


if __name__ == "__main__":
    main()