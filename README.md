# Rock, Paper, Scissors Game in Python

A simple, terminal-based Rock, Paper, Scissors game written in Python, featuring multiple game modes. This project was created to demonstrate fundamental programming logic, user input handling, and conditional structures.

## Features

-   Classic Rock, Paper, Scissors logic (Rock > Scissors, Scissors > Paper, Paper > Rock).
-   **Three distinct game modes:**
    1.  Player vs. Player
    2.  Player vs. Computer
    3.  Computer vs. Computer (Simulation)
-   Interactive Command-Line Interface (CLI).
-   Score tracking across multiple rounds.
-   Option to continue playing or end the game after each round.

## How to Play

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/PedroMagno07/python-rock-paper-scissors.git](https://github.com/PedroMagno07/python-rock-paper-scissors.git)
    ```
    2.  **Navigate to the project directory:**
    ```sh
    cd python-rock-paper-scissors
    ```

3.  **Run the script:**
    ```sh
    python rock_paper_scissors.py
    ```

4.  Follow the on-screen prompts to select a game mode and make your move (1 for Rock, 2 for Paper, 3 for Scissors).

## Game Logic

The winner of each round is determined by a mathematical trick based on the players' choices (1, 2, or 3). The difference between Player 1's choice and Player 2's choice determines the outcome:

-   A difference of `0` is a **Tie**.
-   A difference of `1` or `-2` means **Player 1 wins**.
-   Any other result means **Player 2 wins**.

The computer's choices are generated randomly using Python's `random` module.

## Authors

This project was created by **Pedro Magno** and **Patrick Davidsonn**.
