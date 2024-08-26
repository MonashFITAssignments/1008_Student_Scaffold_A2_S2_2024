from unittest import TestCase

from data_structures.referential_array import ArrayR
from ed_utils.decorators import number, visibility
from tests.helper import take_out_from_adt
from constants import GameResult, PlayerPosition, TeamStats
from player import Player
from team import Team


class TestTask2(TestCase):

    def setUp(self) -> None:
        self.sample_players = [
            Player("Alexey", PlayerPosition.STRIKER, 22),
            Player("Maria", PlayerPosition.MIDFIELDER, 22),
            Player("Brendon", PlayerPosition.DEFENDER, 22),
            Player("Saksham", PlayerPosition.GOALKEEPER, 22),
            Player("Rupert", PlayerPosition.GOALKEEPER, 45),
        ]
        self.valid_team_stats = TeamStats
        self.sample_team = Team("Sample Team", ArrayR.from_list(self.sample_players))

    @number("2.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_team_init_basic(self) -> None:
        self.assertEqual(self.sample_team.get_name(), "Sample Team", "The team name is incorrect")

    @number("2.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_team_stats_init(self) -> None:
        """
        Basic test to see if the player's stats have been set up correctly.
        Checks if the correct stats are present and initialised to 0.
        """
        sample_team = self.sample_team

        for stat in self.valid_team_stats:
            if stat == TeamStats.LAST_FIVE_RESULTS:
                continue
            self.assertEqual(sample_team[stat], 0, f"Stat {stat} should be initialised to 0")

    @number("2.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_team_changes(self) -> None:
        """
        Testing if statistics are updated correctly for the team.
        """

        c_team = self.sample_team
        """
        Aside from this test stats will only be incremented
        Games played and Points are also updated as a result of the wins, draws and losses
        so we assert the checks early because
        c_team["Wins"] = 1
        will also update the games played and points
        """
        c_team[TeamStats.WINS] = 1
        self.assertEqual(c_team[TeamStats.GAMES_PLAYED], 1, "Games Played stat not updated correctly")
        c_team[TeamStats.DRAWS] = 0
        c_team[TeamStats.LOSSES] = 0
        c_team[TeamStats.GOALS_FOR] = 2
        c_team[TeamStats.GOALS_AGAINST] = 1

        self.assertEqual(c_team[TeamStats.WINS], 1, "Wins stat not updated correctly")
        self.assertEqual(c_team[TeamStats.DRAWS], 0, "Draws stat not updated correctly")
        self.assertEqual(c_team[TeamStats.LOSSES], 0, "Losses stat not updated correctly")
        self.assertEqual(c_team[TeamStats.GOALS_FOR], 2, "Goals For stat not updated correctly")
        self.assertEqual(c_team[TeamStats.GOALS_AGAINST], 1, "Goals Against stat not updated correctly")
        self.assertEqual(c_team[TeamStats.GOALS_DIFFERENCE], 1, "Goals Difference stat not updated correctly")

    @number("2.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_teams_additional_methods(self) -> None:
        # checking __len__ method
        self.assertEqual(len(self.sample_team), 5, "The team should have 5 players")

        self.assertEqual(self.sample_team.get_name(), "Sample Team", "The team name is incorrect")

    @number("2.5")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_teams_with_player_teams(self) -> None:
        """
        Testing if the team has the correct number of players.
        """

        #### STRIKER ####
        team_player = self.sample_team.get_players(PlayerPosition.STRIKER)
        self.assertIsNotNone(team_player,"None player was returned for get_players('PlayerPosition.STRIKER') This is incorrect as there is a player in the team with the position Striker.")
        self.assertEqual(len(team_player), 1, f"Only one player should be returned for Striker you have returned {len(team_player)}")
        team_player = take_out_from_adt(team_player)
        self.assertEqual(team_player[0].get_name(), "Alexey", "Incorrect player found for Striker")


        #### MIDFIELDER ####
        team_player = self.sample_team.get_players(PlayerPosition.MIDFIELDER)
        self.assertIsNotNone(team_player,"None player was returned for get_players('PlayerPosition.MIDFIELDER') This is incorrect as there is a player in the team with the position Midfielder.")
        self.assertEqual(len(team_player), 1, f"Only one player should be returned for Midfielder you have returned {len(team_player)}")
        team_player = take_out_from_adt(team_player)
        self.assertEqual(team_player[0].get_name(), "Maria", "Incorrect player found for Midfielder")


        #### DEFENDER ####
        team_player = self.sample_team.get_players(PlayerPosition.DEFENDER)
        self.assertIsNotNone(team_player,"None player was returned for get_players('PlayerPosition.DEFENDER') This is incorrect as there is a player in the team with the position Defender.")
        self.assertEqual(len(team_player), 1, f"Only one player should be returned for Defender you have returned {len(team_player)}")
        team_player = take_out_from_adt(team_player)
        self.assertEqual(team_player[0].get_name(), "Brendon", "Incorrect player found for Defender")


    @number("2.6")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_teams_with_player_teams_2(self) -> None:
        """
        Testing if the team has the correct number of players.
        """

        # Get the GOALKEEPER (should return two players)
        team_players = self.sample_team.get_players(PlayerPosition.GOALKEEPER)
        self.assertIsNotNone(team_players, "No player was returned for team > get_players> 'PlayerPosition.GOALKEEPER'")
        self.assertEqual(len(team_players), 2,
                         f"Two players should be returned for Goalkeeper you have returned {len(team_players)}")
        team_players = take_out_from_adt(team_players)

        """
        Note the ordering matters
        Saksham is the first goalkeeper to be added
        then Rupert is the second goalkeeper to be added
        """
        expected_names = ["Saksham", "Rupert"]
        for idx, player in enumerate(team_players):
            self.assertEqual(player.get_position(), PlayerPosition.GOALKEEPER,
                             f"Incorrect player position, expected {PlayerPosition.GOALKEEPER} got {player.get_position()}")
            self.assertEqual(player.get_name(), expected_names[idx],
                             f"Expected player {expected_names[idx]} got {player.get_name()}.")

    @number("2.7")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_adding_players_to_teams(self) -> None:
        """
        Testing if the players are added to the team correctly.
        """
        sample_team = self.sample_team
        sample_players = self.sample_players
        for player in self.sample_players:
            self.assertIn(player, sample_team.get_players(), f"Player {player.get_name()} not found in the team")

        # remove the players from the team
        for i, player in enumerate(self.sample_players):
            player_position = player.get_position()
            sample_team.remove_player(player)
            # Check if they were removed
            if player_position is not PlayerPosition.GOALKEEPER:
                self.assertIsNone(sample_team.get_players(player_position), f"Player {player.get_name()} not removed from the team")
            elif player.get_name() == "Saksham":
                self.assertEqual(len(sample_team.get_players(PlayerPosition.GOALKEEPER)), 1, "Only one goalkeeper should be left in the team")
            else:
                # Final removal
                self.assertIsNone(sample_team.get_players(PlayerPosition.GOALKEEPER), f"Player {player.get_name()} not removed from the team")
                self.assertIsNone(sample_team.get_players(), "All players should have been removed from the team so None should be returned.")
                self.assertEqual(len(sample_team), 0, "All players should have been removed from the team")



        sample_team.add_player(sample_players[0])
        self.assertEqual(len(sample_team), 1, "The team should have 1 player")
        sample_team.add_player(sample_players[1])
        self.assertEqual(len(sample_team), 2, "The team should have 2 players")
        sample_team.add_player(sample_players[2])
        self.assertEqual(len(sample_team), 3, "The team should have 3 players")
        sample_team.add_player(sample_players[3])
        self.assertEqual(len(sample_team), 4, "The team should have 4 players")
        sample_team.add_player(sample_players[4])
        self.assertEqual(len(sample_team), 5, "The team should have 5 players")
        self.assertEqual(len(sample_team.get_players(PlayerPosition.GOALKEEPER)),
                         2, "The team should have 2 goalkeepers")
        self.assertEqual(len(sample_team.get_players(PlayerPosition.STRIKER)), 1, "The team should have 1 striker")
        self.assertEqual(len(sample_team.get_players(PlayerPosition.MIDFIELDER)),
                         1, "The team should have 1 midfielder")
        self.assertEqual(len(sample_team.get_players(PlayerPosition.DEFENDER)), 1, "The team should have 1 defender")
        self.assertEqual(len(sample_team.get_players(PlayerPosition.GOALKEEPER)),
                         2, "The team should have 2 goalkeepers")

    @number("2.8")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_reset_stats(self) -> None:
        """
        Testing if the stats are reset correctly.
        """
        sample_team = self.sample_team
        sample_team[TeamStats.WINS] += 1
        sample_team[TeamStats.DRAWS] += 1
        sample_team[TeamStats.LOSSES] += 1
        sample_team[TeamStats.LOSSES] += 1
        sample_team[TeamStats.GOALS_FOR] += 2
        sample_team[TeamStats.GOALS_AGAINST] = 1
        """"
        GAMES_PLAYED = 4 (Skipped)
        POINTS = 4 (Skipped)
        WINS = 1
        DRAWS = 1
        LOSSES = 2
        GOALS_FOR = 2
        GOALS_AGAINST = 1
        GOALS_DIFFERENCE = 1
        LAST_FIVE_RESULTS = None (to be tested in another test)
        Order for the expected stats below
        """
        # Double check they were actually set
        expected = [4, 4, 1, 1, 2, 2, 1, 1, None]
        exp_stats = self.valid_team_stats
        for idx, stat in enumerate(exp_stats):
            # We're currently not testing these stats
            # You'll find tests for these below
            if stat in [TeamStats.LAST_FIVE_RESULTS, TeamStats.POINTS, TeamStats.GOALS_DIFFERENCE, TeamStats.GAMES_PLAYED]:
                continue
            self.assertEqual(sample_team[stat], expected[idx], f"Stat {stat} should be {expected[idx]}")

        sample_team.reset_stats()

        for stat in self.valid_team_stats:
            if stat in [TeamStats.LAST_FIVE_RESULTS]:
                continue
            self.assertEqual(sample_team[stat], 0, f"Stat {stat} should be reset to 0")

        # We're not checking last five results in this task but ensure you reset it
        sample_team[TeamStats.DRAWS] = 1
        self.assertEqual(sample_team[TeamStats.GAMES_PLAYED], 1, "Games Played stat not updated correctly after reset")

    @number("2.9")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_cascading_stats(self) -> None:
        sample_team = self.sample_team
        sample_team[TeamStats.WINS] += 1

        self.assertEqual(sample_team[TeamStats.WINS], 1,
                         f"The team should have 1 win, you have {sample_team[TeamStats.WINS]}")
        self.assertEqual(sample_team[TeamStats.GAMES_PLAYED], 1,
                         f"The team should have played 1 game, you have {sample_team[TeamStats.GAMES_PLAYED]}")
        # A win is worth 3 points please see the GameResult Enum in constants.py
        self.assertEqual(sample_team[TeamStats.POINTS], 3,
                         f"The team should have 3 points, you have {sample_team[TeamStats.POINTS]}")

        sample_team[TeamStats.DRAWS] += 1
        self.assertEqual(sample_team[TeamStats.DRAWS], 1,
                         f"The team should have 1 draw, you have {sample_team[TeamStats.DRAWS]}")
        self.assertEqual(sample_team[TeamStats.GAMES_PLAYED], 2,
                         f"The team should have played 2 games, you have {sample_team[TeamStats.GAMES_PLAYED]}")
        # A draw is worth 1 point
        self.assertEqual(sample_team[TeamStats.POINTS], 4,
                         f"The team should have 4 points, you have {sample_team[TeamStats.POINTS]}")

    @number("2.10")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_last_five(self) -> None:
        """
        When the team has not played any games the last five results should return None
        """
        sample_team = self.sample_team
        student_last_five = sample_team.get_last_five_results()

        # When the team has not played any games the last five results should return None
        self.assertIsNone(student_last_five, "The last five results should be None as no games have taken place")

        # Sample team wins a game
        sample_team[TeamStats.WINS] += 1

        student_last_five = sample_team.get_last_five_results()
        student_last_five = take_out_from_adt(student_last_five)
        self.assertEqual(len(student_last_five), 1,
                         "The last five results should hold a single win, the length of your array is incorrect indicating you have additional elements.")

        self.assertEqual(student_last_five[0], GameResult.WIN,
                         f"The last five results should hold a `GameResult.WIN`, you have {student_last_five[0]}")

        sample_team[TeamStats.LOSSES] += 1
        student_last_five = sample_team.get_last_five_results()

        self.assertEqual(len(student_last_five), 2,
                         f"The last five results should hold a single win and a loss (two elements), you have {len(student_last_five)} elements.")
        student_last_five = take_out_from_adt(student_last_five)

        self.assertEqual(student_last_five[0], GameResult.WIN,
                         f"The last five results should hold a `GameResult.WIN`, you have {student_last_five[0]}")
        self.assertEqual(student_last_five[1], GameResult.LOSS,
                         f"The last five results should hold a `GameResult.LOSS`, you have {student_last_five[1]}")

        sample_team[TeamStats.LOSSES] += 1
        sample_team[TeamStats.LOSSES] += 1
        sample_team[TeamStats.LOSSES] += 1

        sample_team[TeamStats.LOSSES] += 1
        sample_team[TeamStats.LOSSES] += 1
        sample_team[TeamStats.LOSSES] += 1
        student_last_five = sample_team.get_last_five_results()

        self.assertEqual(len(student_last_five), 5,
                         f"The last five results should hold a maximum of 5 elements, you have {len(student_last_five)} elements.Oldest elements should be removed first.")

        student_last_five = take_out_from_adt(student_last_five)

        for result in student_last_five:
            self.assertEqual(result, GameResult.LOSS,
                             f"The last five results should hold a `GameResult.LOSS`, you have {result}")

        self.assertEqual(sample_team[TeamStats.WINS], 1,
                         f"The team should have 1 win, you have {sample_team[TeamStats.WINS]}")
        self.assertEqual(sample_team[TeamStats.LOSSES], 7,
                         f"The team should have 7 losses, you have {sample_team[TeamStats.LOSSES]}")
        self.assertEqual(sample_team[TeamStats.GAMES_PLAYED], 8,
                         f"The team should have played 8 games, you have {sample_team[TeamStats.LOSSES]}")

    @number("2.11")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_last_five_2(self) -> None:
        """
        Some additional tests you should look to pass
        test 2.10 first before looking to fix issues in this task.

        """
        sample_team = self.sample_team
        sample_team[TeamStats.WINS] += 1
        sample_team[TeamStats.DRAWS] += 1
        sample_team[TeamStats.LOSSES] += 1
        student_last_five = sample_team.get_last_five_results()
        # Second call should not break anything
        student_last_five = sample_team.get_last_five_results()
        self.assertEqual(len(student_last_five), 3, f"Only three matches have occured, thus you should only have three elements in the last five results, you have {len(student_last_five)} elements.")

        # We extract an Array R from your ADT of choice in order to compare the results with the expected
        # Order matters!
        student_last_five = take_out_from_adt(student_last_five)

        expected = [GameResult.WIN, GameResult.DRAW, GameResult.LOSS]
        self.assertEqual(len(student_last_five), len(expected), "Incorrect number of results returned")
        for idx in range(len(expected)):
            self.assertEqual(student_last_five[idx], expected[idx],
                             f"The last five results should hold a {expected[idx]}, you have {student_last_five[idx]} issue is at index {idx} of your returned value.")

        sample_team[TeamStats.WINS] += 1
        sample_team[TeamStats.WINS] += 1

        # Check once more before we have to drop out a result
        expected = [GameResult.WIN, GameResult.DRAW, GameResult.LOSS, GameResult.WIN, GameResult.WIN]
        student_last_five = sample_team.get_last_five_results()
        self.assertEqual(len(student_last_five), len(expected), "Incorrect number of results returned")
        student_last_five = take_out_from_adt(student_last_five)

        for idx in range(len(expected)):
            self.assertEqual(student_last_five[idx], expected[idx],
                             f"The last five results should hold a {expected[idx]}, you have {student_last_five[idx]} issue is at index {idx} of your returned value.")

        # Now we have 5 results we should drop the first result which is the Win
        sample_team[TeamStats.LOSSES] += 1
        student_last_five = sample_team.get_last_five_results()
        self.assertEqual(len(student_last_five), 5, "Incorrect number of results returned")
        student_last_five = take_out_from_adt(student_last_five)

        expected = [GameResult.DRAW, GameResult.LOSS, GameResult.WIN, GameResult.WIN, GameResult.LOSS]
        self.assertEqual(len(student_last_five), len(expected), "Incorrect number of results returned")
        self.assertEqual(len(student_last_five), len(expected), "Incorrect number of results returned")
        for idx in range(len(expected)):
            self.assertEqual(student_last_five[idx], expected[idx],
                             f"The last five results should hold a {expected[idx]}, you have {student_last_five[idx]} issue is at index {idx} of your returned value.")

    @number("2.12")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_get_players(self):
        """
        Testing if the players are returned correctly.
        """
        # Create a sample team different to the one in the setup
        sample_team = Team("Sample Team", ArrayR.from_list(self.sample_players[0:1]))

        # Get the players
        players = sample_team.get_players()

        # Expected result
        expected = [self.sample_players[0]]

        # Check if the players are correct
        self.assertEqual(len(players), len(expected), "Incorrect number of players returned")
        self.assertEqual(players[0], expected[0], "Incorrect player returned")

        # Add all the rest of the players
        for player in self.sample_players[1:]:
            sample_team.add_player(player)

        # Get the players
        players = sample_team.get_players()

        # Expected result in order
        expected = ArrayR.from_list([self.sample_players[3], self.sample_players[4], self.sample_players[2], self.sample_players[1], self.sample_players[0]])

        # Check if the players are correct
        self.assertEqual(len(players), len(expected), "Incorrect number of players returned")
        for i in range(len(players)):
            self.assertEqual(players[i], expected[i], "Incorrect player returned / order of players incorrect")
