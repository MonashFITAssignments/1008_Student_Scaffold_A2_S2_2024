from __future__ import annotations
from data_structures.referential_array import ArrayR
from constants import GameResult, PlayerPosition, PlayerStats, TeamStats
from player import Player
from typing import Collection, Union, TypeVar

T = TypeVar("T")


class Team:
    def __init__(self, team_name: str, players: ArrayR[Player]) -> None:
        """
        Constructor for the Team class

        Args:
            team_name (str): The name of the team
            players (ArrayR[Player]): The players of the team

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def reset_stats(self) -> None:
        """
        Resets all the statistics of the team to the values they were during init.

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def add_player(self, player: Player) -> None:
        """
        Adds a player to the team.

        Args:
            player (Player): The player to add

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def remove_player(self, player: Player) -> None:
        """
        Removes a player from the team.

        Args:
            player (Player): The player to remove

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def get_number(self) -> int:
        """
        Returns the number of the team.

        Complexity:
            Analysis not required.
        """
        raise NotImplementedError

    def get_name(self) -> str:
        """
        Returns the name of the team.

        Complexity:
            Analysis not required.
        """
        raise NotImplementedError

    def get_players(self, position: Union[PlayerPosition, None] = None) -> Union[Collection[Player], None]:
        """
        Returns the players of the team that play in the specified position.
        If position is None, it should return ALL players in the team.
        You may assume the position will always be valid.
        Args:
            position (Union[PlayerPosition, None]): The position of the players to return

        Returns:
            Collection[Player]: The players that play in the specified position
            held in a valid data structure provided to you within
            the data_structures folder this includes the ArrayR
            which was previously prohibited.

            None: When no players match the criteria / team has no players

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def get_statistics(self):
        """
        Get the statistics of the team

        Returns:
            statistics: The teams' statistics

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def get_last_five_results(self) -> Union[Collection[GameResult], None]:
        """
        Returns the last five results of the team.
        If the team has played less than five games,
        return all the result of all the games played so far.

        For example:
        If a team has only played 4 games and they have:
        Won the first, lost the second and third, and drawn the last,
        the array should be an array of size 4
        [GameResult.WIN, GameResult.LOSS, GameResult.LOSS, GameResult.DRAW]

        **Important Note:**
        If this method is called before the team has played any games,
        return None the reason for this is explained in the specefication.

        Returns:
            Collection[GameResult]: The last five results of the team
            or
            None if the team has not played any games.

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def get_top_x_players(self, player_stat: PlayerStats, num_players: int) -> list[tuple[int, str, Player]]:
        """
        Note: This method is only required for FIT1054 students only!

        Args:
            player_stat (PlayerStats): The player statistic to use to order the top players
            num_players (int): The number of players to return from this team

        Return:
            list[tuple[int, str, Player]]: The top x players from this team
        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def __setitem__(self, statistic: TeamStats, value: int) -> None:
        """
        Updates the team's statistics.

        Args:
            statistic (TeamStats): The statistic to update
            value (int): The new value of the statistic

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def __getitem__(self, statistic: TeamStats) -> int:
        """
        Returns the value of the specified statistic.

        Args:
            statistic (TeamStats): The statistic to return

        Returns:
            int: The value of the specified statistic

        Raises:
            ValueError: If the statistic is invalid

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def __len__(self) -> int:
        """
        Returns the number of players in the team.

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """
        Optional but highly recommended.

        You may choose to implement this method to help you debug.
        However your code must not rely on this method for its functionality.

        Returns:
            str: The string representation of the team object.

        Complexity:
            Analysis not required.
        """
        return ""

    def __repr__(self) -> str:
        """Returns a string representation of the Team object.
        Useful for debugging or when the Team is held in another data structure."""
        return str(self)
