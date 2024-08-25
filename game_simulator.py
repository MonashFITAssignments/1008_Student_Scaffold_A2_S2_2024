from __future__ import annotations
from data_structures.hash_table import LinearProbeTable
from data_structures.referential_array import ArrayR
from constants import PlayerPosition, PlayerStats, ResultStats
from player import Player
from random_gen import RandomGen
from team import Team


class GameSimulator:

    @staticmethod
    def simulate(home_team: Team, away_team: Team) -> LinearProbeTable:
        """
        Simulates a game between two teams, considering player stats for a more probabilistic outcome.
        Note: To call this method, use: GameSimulator.simulate(home_team, away_team)

        Args:
            home_team (Team): The home team.
            away_team (Team): The away team.

        Returns:
            LinearProbeTable: A table with keys 'Home Goals', 'Away Goals', 'Goal Scorers',
                            'Goal Assists', 'Interceptions', 'Tacklers'
        """
        result_table: LinearProbeTable = LinearProbeTable()

        # 1. Determine goals scored by each team with a higher likelihood of low scores
        goal_distribution: list[int] = [0] * 30 + [1] * 30 + [2] * 20 + [3] * 10 + [4] * 5 + [5] * 5
        home_goals: int = RandomGen.random_choice(goal_distribution)
        away_goals: int = RandomGen.random_choice(goal_distribution)
        result_table[ResultStats.HOME_GOALS.value] = home_goals
        result_table[ResultStats.AWAY_GOALS.value] = away_goals

        # 2. Select goal scorers and assist providers based on stats
        goal_scorers: list[str] = []
        goal_assists: list[str] = []
        home_players: ArrayR[Player] = home_team.get_players()
        away_players: ArrayR[Player] = away_team.get_players()

        # Get a list of outfield player from both teams
        home_outfield: list[Player] = [player for player in home_players if player.get_position() != PlayerPosition.GOALKEEPER]
        away_outfield: list[Player] = [player for player in away_players if player.get_position() != PlayerPosition.GOALKEEPER]

        all_players: ArrayR[Player] = ArrayR(len(home_players) + len(away_players))

        for i in range(len(home_players)):
            all_players[i] = home_players[i]

        for i in range(len(away_players)):
            all_players[i + len(home_players)] = away_players[i]

        for _ in range(home_goals):
            scorer: Player = GameSimulator.__weighted_choice(home_outfield, PlayerStats.STAR_SKILL, PlayerStats.WEIGHT, PlayerStats.HEIGHT)
            goal_scorers.append(scorer.get_name())

            if RandomGen.random_chance(0.7):  # 70% chance of an assist
                assist: Player = GameSimulator.__weighted_choice(home_outfield, PlayerStats.STAR_SKILL, PlayerStats.WEAK_FOOT_ABILITY)
                goal_assists.append(assist.get_name())

        for _ in range(away_goals):
            scorer: Player = GameSimulator.__weighted_choice(away_outfield, PlayerStats.STAR_SKILL, PlayerStats.WEIGHT, PlayerStats.HEIGHT)
            goal_scorers.append(scorer.get_name())

            if RandomGen.random_chance(0.7):  # 70% chance of an assist
                assist: Player = GameSimulator.__weighted_choice(away_outfield, PlayerStats.STAR_SKILL, PlayerStats.WEAK_FOOT_ABILITY)
                goal_assists.append(assist.get_name())

        result_table[ResultStats.GOAL_SCORERS.value] = ArrayR.from_list(goal_scorers)
        result_table[ResultStats.GOAL_ASSISTS.value] = ArrayR.from_list(goal_assists)

        # 3. Assign interceptions and tackles based on defensive stats
        interceptions: list[str] = [GameSimulator.__weighted_choice(all_players, PlayerStats.HEIGHT).get_name() for _ in range(RandomGen.randint(0, 10))]
        tackles: list[str] = [GameSimulator.__weighted_choice(all_players, PlayerStats.HEIGHT).get_name() for _ in range(RandomGen.randint(0, 10))]

        result_table[ResultStats.TACKLES.value] = ArrayR.from_list(tackles)
        result_table[ResultStats.INTERCEPTIONS.value] = ArrayR.from_list(interceptions)

        return result_table

    @staticmethod
    def __weighted_choice(players: list, *attributes: str) -> Player:
        """
        Selects a player based on weighted stats.

        Args:
            players (list): List of players to choose from.
            *attributes (str): Attributes to consider for weighting.

        Returns:
            Player: The selected player.
        """
        total_weight: int = sum(
            sum(player[attr] for attr in attributes) for player in players
        )

        if total_weight == 0:  # Handle edge case where all weights are zero
            return RandomGen.random_choice(players)

        rand_val: int = RandomGen.random_choice(range(total_weight))
        cumulative_weight: int = 0
        for player in players:
            player_weight: int = sum(player[attr] for attr in attributes)
            cumulative_weight += player_weight
            if cumulative_weight >= rand_val:
                return player

        # Fallback in case rounding errors cause a miss
        return RandomGen.random_choice(players)
