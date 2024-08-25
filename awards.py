from __future__ import annotations
from data_structures.referential_array import ArrayR
from constants import PlayerStats
from season import Season


class Awards:
    def __init__(self, season: Season, player_stat: PlayerStats, num_top_players: int) -> None:
        """
        Initializes the awards based on the provided teams, player stat and top players.

        Args:
            season (season): The season we are generating the awards for.
            player_stat (PlayerStat): The player stat to order the awards by (in descending order)
            num_top_players (int): The number of players from each team to track.
        """
        raise NotImplementedError

    def get_leaderboard(self) -> ArrayR[ArrayR[int | str]]:
        """
        Generates the leaderboard of awards.

        Returns:
            ArrayR(ArrayR[ArrayR[int | str]]):
                Outer array represents each team in the leaderboard
                Inner array consists of 10 elements:
                    - Player Name (str)
                    - Games Played (int)
                    - Goals (int)
                    - Assists (int)
                    - Tackles (int)
                    - Interceptions (int)
                    - Star Skill (int)
                    - Weak Foot Ability (int)
                    - Weight (int)
                    - Height (int)

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
            str: The string representation of the awards object.

        Complexity:
            Analysis not required.
        """
        raise NotImplementedError

    def __repr__(self) -> str:
        """Returns a string representation of the Awards object.
        Useful for debugging or when the Awards are held in another data structure."""
        return str(self)
