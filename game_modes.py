class Classic:
    NAME = 'Classic Rock-Paper-Scissors'
    SIGNS = 'ROCK', 'PAPER', 'SCISSORS'
    # (Winner, Loser)
    RULES = (
        ('ROCK', 'SCISSORS'),
        ('PAPER', 'ROCK'),
        ('SCISSORS', 'PAPER')
    )


class BigBangTheory(Classic):
    NAME = 'Big Bang Theory'
    SIGNS = Classic.SIGNS + ('LIZARD', 'SPOCK')
    RULES = Classic.RULES + (
        ('ROCK', 'LIZARD'),
        ('PAPER', 'SPOCK'),
        ('SCISSORS', 'LIZARD'),
        ('LIZARD', 'PAPER'),
        ('LIZARD', 'SPOCK'),
        ('SPOCK', 'SCISSORS'),
        ('SPOCK', 'ROCK')
    )


class FireWater(Classic):
    NAME = 'Fire & Water'
    SIGNS = Classic.SIGNS + ('FIRE', 'WATER')
    RULES = Classic.RULES + (
        ('FIRE', 'ROCK'),
        ('FIRE', 'PAPER'),
        ('FIRE', 'SCISSORS'),
        ('WATER', 'FIRE'),
        ('ROCK', 'WATER'),
        ('PAPER', 'WATER'),
        ('SCISSORS', 'WATER')
    )


GAME_MODES = {
    'Classic': Classic,
    'BigBangTheory': BigBangTheory,
    'FireWater': FireWater
}
