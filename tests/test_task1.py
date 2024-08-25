from unittest import TestCase

from ed_utils.decorators import number, visibility
from constants import PlayerPosition, PlayerStats, TeamStats
from player import Player


class TestTask1(TestCase):

    def setUp(self) -> None:
        self.sample_players = [
            Player("Alexey", PlayerPosition.STRIKER, 21),
            Player("Maria", PlayerPosition.MIDFIELDER, 21),
            Player("Brendon", PlayerPosition.DEFENDER, 21),
            Player("Saksham", PlayerPosition.GOALKEEPER, 23),
        ]

    @number("1.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_player_init(self) -> None:
        """
        Basic test to see if the player's init has been set up correctly.
        """
        Alexey = self.sample_players[0]

        self.assertEqual(Alexey.name, "Alexey")
        self.assertEqual(Alexey.position, PlayerPosition.STRIKER)
        self.assertEqual(Alexey.age, 21)


    @number("1.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_player_stat_retrieval(self) -> None:
        """
        Testing the stat rettrieval of the player.
        This functionality should be implemented using the `__getitem__` method.
        """
        sample_player = self.sample_players[0]

        # Assert that the stats are zero
        for player_stat in PlayerStats:
            self.assertEqual(sample_player[player_stat], 0, f"Stat {player_stat.name} not set to 0 after player init")

    @number("1.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_player_stat_update(self) -> None:
        """
        Ensure you pass the previous task first before attempting this test.
        This functionality should be implemented using the `__setitem__` method.
        """
        sample_player = self.sample_players[0]

        for i, player_stat in enumerate(PlayerStats):
            sample_player[player_stat] = i + 1
            self.assertEqual(sample_player[player_stat], i + 1, f"Stat {player_stat.name} not updated correctly expected {i + 1} got {sample_player[player_stat]}")

    @number("1.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_player_stat_reset(self) -> None:
        """
        Ensure you pass the previous task first before attempting this test.
        """
        sample_player = self.sample_players[0]

        # Assume the player stats are 0'd after init this is tested in 1.3

        for i, player_stat in enumerate(PlayerStats):
            sample_player[player_stat] = i + 1
            self.assertEqual(sample_player[player_stat], i + 1, f"Stat {player_stat.name} not updated correctly expected {i + 1} got {sample_player[player_stat]}")

        sample_player.reset_stats()
        for i, player_stat in enumerate(PlayerStats):
            self.assertEqual(sample_player[player_stat], 0, f"Stat {player_stat.name} not reset to 0 after `reset_stats` method")
