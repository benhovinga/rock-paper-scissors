import random
from player import Player
from game_modes import GAME_MODES


class Game:
    game_mode: str
    signs: tuple
    rules: tuple
    players: list

    def __init__(self, game_mode: str, players: list) -> None:
        self.game_mode = game_mode
        self.signs = GAME_MODES[game_mode].SIGNS
        self.rules = GAME_MODES[game_mode].RULES
        self.players = players

    def print_sign_list(self) -> None:
        """Print the list of signs to the terminal"""
        for x in range(1, len(self.signs) + 1):
            print(f'{x}: {self.signs[x - 1]}')

    def get_player_sign(self) -> str:
        """Get a sign selection from the player"""
        while True:
            try:
                return self.signs[int(input('--> ')) - 1]
            except (ValueError, IndexError):
                print('That is not a valid option, try again.')

    def assign_player_sign(self) -> None:
        """Ask each player for a sign"""
        for player in self.players:
            if not player.is_computer:
                print(f'"{player.name}", pick your sign')
                self.print_sign_list()
                player.sign = self.get_player_sign()

    def assign_computer_sign(self) -> None:
        """Assign all computer players a random sign"""
        for player in self.players:
            if player.is_computer:
                player.sign = random.choice(self.signs)

    def compare_two_signs(self, player1: Player, player2: Player) -> Player:
        """Compare two signs against the rules and return the winner"""
        # Compare signs
        if (player1.sign, player2.sign) in self.rules:
            return player1
        elif (player2.sign, player1.sign) in self.rules:
            return player2

    def print_selections(self):
        for player in self.players:
            print(f'{player.name}: {player.sign}')

    def print_score(self) -> None:
        for player in self.players:
            print(f'{player.name}: {player.score}')

    def calculate_winner(self) -> Player:
        # TODO: Calculate for more than 2 players
        return self.compare_two_signs(self.players[0], self.players[1])
