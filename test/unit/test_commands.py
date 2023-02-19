# standards imports
import unittest
from unittest.mock import patch, MagicMock

# external imports

# project imports
from click.testing import CliRunner
from pycli import commands


class TestFetchPokemon(unittest.TestCase):

    """
    The purpose of testing the commands.py module is to ensure the interface is
    workings as intended, business logic and requests should be tested
    separately
    """

    def test_fetch_single_pokemon(self):
        self.maxDiff == 1000
        runner = CliRunner()
        result = runner.invoke(commands.fetch_pokemon, ["--names=bulbasaur", "--testing"])
        assert result.exit_code == 0
        assert result.output == '[{"name": "bulbasaur", "height": 1, "weight": 1}]\n'

    def test_fetch_multiple_pokemon(self):
        self.maxDiff == 1000
        runner = CliRunner()
        result = runner.invoke(commands.fetch_pokemon, ["--names=bulbasaur,charmander", "--testing"])
        assert result.exit_code == 0
        assert result.output == '[{"name": "bulbasaur", "height": 1, "weight": 1}, {"name": "charmander", "height": 1, "weight": 1}]\n'
