#!/usr/bin/env python3
"""
Rock Paper Scissors
Author: SyntaxEG
"""
import random


SIGNS = ('ROCK', 'PAPER', 'SCISSORS')
RULES = (
    # (winner, loser)
    ('ROCK', 'SCISSORS'),
    ('PAPER', 'ROCK'),
    ('SCISSORS', 'PAPER')
)


class Player:
    score: int = 0
    sign: str

    def __init__(self, name: str, is_computer: bool = False) -> None:
        self.name = name
        self.is_computer = is_computer


def print_sign_list() -> None:
    """Print the list of signs to the terminal"""
    print('\nSelect a sign:')
    for x in range(1, len(SIGNS) + 1):
        print(f'{x}: {SIGNS[x - 1]}')


def get_player_sign() -> str:
    """Get a sign selection from the player"""
    while True:
        try:
            return SIGNS[int(input('--> ')) - 1]
        except (ValueError, IndexError):
            print('That is not a valid option, try again.')


def get_computer_sign() -> str:
    """Give the computer a random sign"""
    return random.choice(SIGNS)


def compare_two_signs(player1: Player, player2: Player) -> Player:
    """Compare two signs against the rules and return the winner"""
    # Compare signs
    if (player1.sign, player2.sign) in RULES:
        return player1
    elif (player2.sign, player1.sign) in RULES:
        return player2


def main() -> None:
    player = Player('Player')
    computer = Player('Computer', True)

    print('Welcome to Rock-Paper-Scissors')

    while True:
        print_sign_list()
        player.sign = get_player_sign()
        computer.sign = get_computer_sign()

        print(f'Player: {player.sign}')
        print(f'Computer: {computer.sign}')

        winner = compare_two_signs(player, computer)
        if winner is None:
            print('Tie')
        else:
            print(f'{winner.name} wins')
            winner.score += 1

        print(f'Score: Player[{player.score}] Computer[{computer.score}]')


if __name__ == '__main__':
    main()
