#!/usr/bin/env python3
"""
Rock Paper Scissors
Author: SyntaxEG
"""
from game import Game, Player


def main() -> None:
    # TODO: User can pick a game mode
    # TODO: User can set number of players (game.calculate_winner() needs fixing for this)
    # TODO: User can set player names and is_computer attributes
    game = Game('Classic', [Player('Player'), Player('Computer', True)])

    print('Welcome to Rock-Paper-Scissors')

    # Main Loop
    while True:
        # Assign all computers a random sign
        game.assign_computer_sign()

        # Get all human player signs
        game.assign_player_sign()

        # Show everyone's selected sign
        game.print_selections()

        # Calculate a winner
        winner = game.calculate_winner()
        if winner is None:
            print('Tie')
        else:
            print(f'{winner.name} wins')
            winner.score += 1

        # Show the score
        game.print_score()


if __name__ == '__main__':
    main()
