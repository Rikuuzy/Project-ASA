# Sichuan Mahjong 13-Tiles Solver

This project is an automated solver for the 13-tile variant of Sichuan Mahjong (also known as Blood River/Battle Mahjong, where one suit must be voided). It takes a screenshot of your starting hand, automatically detects the tiles using computer vision, and calculates the optimal strategy for playing the hand using various search algorithms.

## Features

- **Automatic Hand Recognition:** Uses OpenCV template matching to identify your 13 tiles from a screenshot.
- **Multiple Solvers:** Provides various algorithms to calculate the optimal voided suit and the best tiles to discard to reach a winning state (or minimum cost state).

### Supported Algorithms

1. **Uniform Cost Search (UCS):** Explores paths based on the lowest cumulative cost.
2. **Greedy Best First Search (GBFS):** Uses a heuristic to quickly find a promising path, though it may not always be optimal.
3. **A* Search:** Combines the benefits of UCS and GBFS by considering both the cost to reach a state and the estimated cost to the goal, guaranteeing an optimal path efficiently.
4. **Dynamic Programming:** Solves the problem by breaking it down into simpler subproblems and storing the results.
5. **Monte Carlo Tree Search (MCTS):** Uses random sampling and tree search to find the best move, particularly useful in complex or uncertain states.

## Project Structure

- `main.py`: The main entry point of the application. It handles user input (selecting a screenshot and algorithm) and orchestrates the recognition and solving process.
- `recognize_hand.py`: Contains the logic for processing the screenshot. It splits the image into individual tiles and classifies them using template matching.
- `astar.py`, `gbfs.py`, `ucs.py`, `dynamic_programming.py`, `mcts.py`: Implementations of the respective search algorithms.
- `templates/`: Directory containing the reference images for the Mahjong tiles, separated by suits (B, C, D - representing Bamboo, Characters, Dots/Circles). These are used by the computer vision module to classify the tiles in your hand.
- `screenshots/`: Directory where you should place the screenshots of your Mahjong hands to be analyzed.
- `debug_split_tiles/`: A directory generated during runtime where the individual sliced tiles from your screenshot are saved for debugging the vision module.

## How to Use

1. Ensure you have the necessary dependencies installed (e.g., `opencv-python` for `cv2`).
2. Place a screenshot of your 13-tile Mahjong hand into the `screenshots/` directory. (Ensure the screenshot matches the expected dimensions and alignment for the templates).
3. Run the main script:
   ```bash
   python main.py
   ```
4. Follow the on-screen prompts to:
   - Select the screenshot you want to analyze.
   - Choose which algorithm you want to use to solve the hand.
5. The program will output the detected tiles, the chosen algorithm's recommendation for the voided suit, the overall cost, and the specific tiles you should discard.
