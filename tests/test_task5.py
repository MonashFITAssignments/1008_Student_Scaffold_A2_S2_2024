from unittest import TestCase

from constants import Constants, PlayerPosition, PlayerStats, TeamStats
from ed_utils.decorators import number, visibility
from data_structures.bset import BSet
from data_structures.referential_array import ArrayR
from tests.helper import take_out_from_adt
from constants import Constants, GameResult
from player import Player
from random_gen import RandomGen
from season import Season
from team import Team
from typing import Union


class Roster:
    FIRST_NAMES: list[str] = ['Abey', 'Alexey', 'Ann', 'Alexandria', 'Ben', 'Bavley', 'Brett', 'Brendon', 'Chloe',
                              'Christian', 'Daniel', 'Fermi', 'Hui', 'Laura', 'Lisa', 'Maria', 'Matthew', 'Patrick',
                              'Rupert', 'Saksham', 'Yasmeen']

    LAST_NAMES: list[str] = ['Bot', 'Bellingham', 'Bonmatí', 'Caicedo', 'Danial', 'Fernandes', 'Francis', 'Hernández',
                             'Henry', 'Iniesta', 'Kerr', 'Messi', 'Mbappé', 'Modric', 'Pearson',
                             'Peterson', 'Ronaldo', 'Roberto', 'Stacie', 'Sparks', 'Wright', 'York', 'Zidane']

    TEAM_NAMES: list[str] = ['Badgers', 'Blitz', 'Commanders', 'Ferguson', 'Gladiators', 'Grizzlies',
                             'Hot Shots', 'Razorbacks', 'Renegades', 'Tiger Sharks', 'Wildcats',
                             'The Flash', 'Blue Angels', 'Fineapples', 'Shock Squad', 'Cherry Blossoms',
                             'Cheetah Girls', 'The Fever', 'Victoria Secret', 'Sweet & Salty', 'Lady Birds']

    PLAYER_NAMES: list[str] = []

    @classmethod
    def generate_players(cls):
        for first_name in cls.FIRST_NAMES:
            for last_name in cls.LAST_NAMES:
                cls.PLAYER_NAMES.append(f'{first_name} {last_name}')

    @classmethod
    def generate_teams(cls, num_teams: int) -> ArrayR[Team]:
        if len(cls.PLAYER_NAMES) == 0:
            cls.generate_players()

        full_roster: list[Player] = []
        taken_names: BSet = BSet()
        for i in range(Constants.TEAM_MAX_PLAYERS * Constants.MAX_NUM_TEAMS):
            player_name: Union[str, None] = None
            while player_name is None:
                player_no: int = RandomGen.randint(1, len(cls.PLAYER_NAMES))
                if player_no not in taken_names:
                    player_name = cls.PLAYER_NAMES[player_no - 1]
                    taken_names.add(player_no)
            position = RandomGen.random_choice(list(PlayerPosition))
            age = RandomGen.randint(18, 30)

            player = Player(player_name, position, age)
            player[PlayerStats.WEIGHT] = RandomGen.randint(70, 90)
            player[PlayerStats.HEIGHT] = RandomGen.randint(150, 180)
            player[PlayerStats.STAR_SKILL] = RandomGen.randint(0, 5)
            player[PlayerStats.WEAK_FOOT_ABILITY] = RandomGen.randint(0, 5)
            full_roster.append(player)

        teams: ArrayR[Team] = ArrayR(num_teams)
        for i in range(num_teams):
            num_players: int = RandomGen.randint(Constants.TEAM_MIN_PLAYERS, Constants.TEAM_MAX_PLAYERS)
            players: ArrayR[Player] = ArrayR(num_players)
            for j in range(num_players):
                player_idx = RandomGen.randint(0, len(full_roster) - 1)
                players[j] = full_roster[player_idx]
                del full_roster[player_idx]

            teams[i] = Team(cls.TEAM_NAMES[i], players)

        return teams


class TestTask5(TestCase):
    def __verify_results(self, expected_results: list[list[Union[str, int, list]]]) -> None:
        for row_no, row in enumerate(self.season.get_leaderboard()):
            for cell_no, cell in enumerate(row):
                if cell_no == 9:
                    results: ArrayR[GameResult] = take_out_from_adt(cell)
                    for result_no, game_result in enumerate(results):
                        self.assertEqual(expected_results[row_no][cell_no][result_no].value, game_result.value)
                else:
                    self.assertEqual(expected_results[row_no][cell_no], cell)

    def setUp(self) -> None:
        RandomGen.set_seed(123)
        self.season: Union[Season, None] = None

    @number("5.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_simulate_season(self):
        teams = Roster.generate_teams(4)
        self.season = Season(teams)
        self.season.simulate_season()
        for team in teams:
           self.assertEqual(team[TeamStats.GAMES_PLAYED], 6, "All teams should have played 38 games")

    @number("5.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_small_leaderboard(self):
        teams = Roster.generate_teams(4)
        self.season = Season(teams)
        self.season.simulate_season()

        expected_results: list[list[Union[str, int, list[GameResult]]]] = [
            ['Badgers',     6, 11, 3, 2, 1, 12,  8,  4, [GameResult.DRAW, GameResult.WIN,  GameResult.WIN,  GameResult.WIN,  GameResult.LOSS]],
            ['Blitz', 	    6, 10, 3, 1, 2, 10,  8,  2, [GameResult.WIN,  GameResult.WIN,  GameResult.LOSS, GameResult.WIN,  GameResult.LOSS]],
            ['Ferguson',    6,  7, 2, 1, 3, 10, 11, -1, [GameResult.LOSS, GameResult.LOSS, GameResult.WIN,  GameResult.LOSS, GameResult.WIN]],
            ['Commanders',  6,  5, 1, 2, 3, 11, 16, -5, [GameResult.DRAW, GameResult.LOSS, GameResult.LOSS, GameResult.LOSS, GameResult.WIN]]
        ]

        self.__verify_results(expected_results)

    @number("5.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_player_stats(self):
        # Set the seed to 123
        RandomGen.set_seed(123)

        # Generate the teams and simulate the season
        teams = Roster.generate_teams(4)
        self.season = Season(teams)
        self.season.simulate_season()

        # Expected results of the stats for all players of the first team
        expected_results: dict = {
            'Badgers': {
                'Ann Caicedo': {PlayerStats.GAMES_PLAYED: 6, PlayerStats.GOALS: 5, PlayerStats.ASSISTS: 0, PlayerStats.TACKLES: 2, PlayerStats.INTERCEPTIONS: 0},
                'Matthew Pearson': {PlayerStats.GAMES_PLAYED: 6, PlayerStats.GOALS: 0, PlayerStats.ASSISTS: 0, PlayerStats.TACKLES: 1, PlayerStats.INTERCEPTIONS: 1},
                'Ben Hernández': {PlayerStats.GAMES_PLAYED: 6, PlayerStats.GOALS: 0, PlayerStats.ASSISTS: 2, PlayerStats.TACKLES: 0, PlayerStats.INTERCEPTIONS: 0},
                'Lisa Roberto': {PlayerStats.GAMES_PLAYED: 6, PlayerStats.GOALS: 1, PlayerStats.ASSISTS: 0, PlayerStats.TACKLES: 2, PlayerStats.INTERCEPTIONS: 2},
                'Patrick Modric': {PlayerStats.GAMES_PLAYED: 6, PlayerStats.GOALS: 0, PlayerStats.ASSISTS: 0, PlayerStats.TACKLES: 0, PlayerStats.INTERCEPTIONS: 0},
                'Lisa Mbappé': {PlayerStats.GAMES_PLAYED: 6, PlayerStats.GOALS: 2, PlayerStats.ASSISTS: 1, PlayerStats.TACKLES: 1, PlayerStats.INTERCEPTIONS: 1}
            }
        }
        # Get all the players of the first team
        players = teams[0].get_players()

        # Create a dictionary of the players with the name as the key and the player object as the value
        players_dict = {player.get_name(): player for player in players}

        # Check the stats of the players of the first team
        for player_name, stats in expected_results['Badgers'].items():
            player = players_dict[player_name]
            for stat, value in stats.items():
                self.assertEqual(value, player[stat], f"{player_name} {stat} not correct")
