from unittest import TestCase

from ed_utils.decorators import number, visibility
from constants import PlayerStats, TeamStats
from hashy_perfection_table import HashyPerfectionTable
from hashy_step_table import HashyStepTable


class TestTask3(TestCase):

    def setUp(self) -> None:
        self.perfect_table: HashyPerfectionTable = HashyPerfectionTable()
        self.step_table: HashyStepTable = HashyStepTable()

    @number("3.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_perfect_hash_valid(self):
        for i, player_stat in enumerate(PlayerStats):
            self.perfect_table[player_stat.value] = i
            self.assertEqual(self.perfect_table[player_stat.value], i, f"Player stat {player_stat.name} not set to {i}")
        self.assertEqual(len(self.perfect_table), len(PlayerStats), f"Wrong length: expected {len(PlayerStats)}, got {len(self.perfect_table)}")


    @number("3.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_perfect_hash_invalid(self):
        for i, letter in enumerate(['A', 'B', 'C']):
            self.assertRaises(KeyError, lambda: self.perfect_table[letter])

    @number("3.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_perfect_hash_delete(self):
        for i, player_stat in enumerate(PlayerStats):
            self.perfect_table[player_stat.value] = i

        for i, player_stat in enumerate(PlayerStats):
            del self.perfect_table[player_stat.value]
            self.assertRaises(KeyError, lambda: self.perfect_table[player_stat.value])
            self.assertEqual(len(self.perfect_table), len(PlayerStats) - i - 1, f"Wrong length: expected {len(PlayerStats) - i - 1}, got {len(self.perfect_table)}")

    @number("3.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_step_hash_valid(self):
        for i, player_stat in enumerate(PlayerStats):
            self.step_table[player_stat.value] = i
            self.assertEqual(self.step_table[player_stat.value], i, f"Player stat {player_stat.name} not set to {i}")
        self.assertEqual(len(self.step_table), len(PlayerStats), f"Wrong length: expected {len(PlayerStats)}, got {len(self.step_table)}")

    @number("3.5")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_step_hash_delete(self):
        for i, player_stat in enumerate(PlayerStats):
            self.step_table[player_stat.value] = i

        for i, player_stat in enumerate(PlayerStats):
            del self.step_table[player_stat.value]
            self.assertRaises(KeyError, lambda: self.step_table[player_stat.value])
            self.assertEqual(len(self.step_table), len(PlayerStats) - i - 1, f"Wrong length: expected {len(PlayerStats) - i - 1}, got {len(self.step_table)}")

    @number("3.6")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_step_hash_delete_advanced(self):
        self.step_table = HashyStepTable([97])
        self.step_table.hash = lambda _: 0
        lookup_table: list[str] = ['A', 'B', 'C', 'D', 'E']

        for letter in lookup_table:
            self.step_table[letter] = letter

        for i, letter in enumerate(lookup_table):
            del self.step_table[letter]
            self.assertRaises(KeyError, lambda: self.step_table[letter])
            for j in range(i + 1, len(lookup_table)):
                self.assertEqual(self.step_table[lookup_table[j]], lookup_table[j], f"Letter not found after deletion")

            self.assertEqual(len(self.step_table), len(lookup_table) - i - 1, f"Wrong length: expected {len(PlayerStats) - i - 1}, got {len(self.step_table)}")
