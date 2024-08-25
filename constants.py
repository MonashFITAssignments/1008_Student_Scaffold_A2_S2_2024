from enum import Enum, IntEnum


class GameResult(IntEnum):
    """
    Enum class to represent the possible game results
    Valid results are: Win, Draw, Loss
    """
    WIN = 3
    DRAW = 1
    LOSS = 0


class Constants:
    """
    These constants are provided for convenience in your code. These may or may not be useful for you.
    As in A1a, the constants should be treated as variable while programming
    as well as while performing complexity analysis
    """
    SEASON_LENGTH = 38
    TEAM_MIN_PLAYERS = 11
    TEAM_MAX_PLAYERS = 15
    MAX_NUM_TEAMS = 20


class PlayerStats(Enum):
    GAMES_PLAYED = "Games Played"
    GOALS = "Goals"
    ASSISTS = "Assists"
    TACKLES = "Tackles"
    INTERCEPTIONS = "Interceptions"
    STAR_SKILL = "Star Skill"
    WEAK_FOOT_ABILITY = "Weak Foot Ability"
    WEIGHT = "Weight"
    HEIGHT = "Height"


class TeamStats(Enum):
    GAMES_PLAYED = "Games Played"
    POINTS = "Points"
    WINS = "Wins"
    DRAWS = "Draws"
    LOSSES = "Losses"
    GOALS_FOR = "Goals For"
    GOALS_AGAINST = "Goals Against"
    GOALS_DIFFERENCE = "Goals Difference"
    LAST_FIVE_RESULTS = "Last Five Results"


class PlayerPosition(Enum):
    """
    Enum class to represent the soccer positions
    Valid positions are: Striker, Midfielder, Defender, Goalkeeper
    """
    GOALKEEPER = "Goalkeeper"
    DEFENDER = "Defender"
    MIDFIELDER = "Midfielder"
    STRIKER = "Striker"


class ResultStats(Enum):
    """
    Enum class to represent the possible keys from a completed game
    """
    HOME_GOALS = "Home Goals"
    AWAY_GOALS = "Away Goals"
    GOAL_SCORERS = "Goal Scorers"
    GOAL_ASSISTS = "Goal Assists"
    TACKLES = "Tackles"
    INTERCEPTIONS = "Interceptions"
