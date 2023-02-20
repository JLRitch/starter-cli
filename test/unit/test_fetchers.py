# standards imports
import unittest
from unittest.mock import patch, MagicMock

# external imports

# project imports
from pycli.fetchers import PokemonFetcher


class TestGetMultiplePokemonData(unittest.TestCase):
    async def test_get_multiple_pokemon_data(self):
        pokemon_names = ["pikachu", "charmander", "squirtle", "bulbasaur"]
        expected_data = [
            {"name": "pikachu", "height": 4, "weight": 60},
            {"name": "charmander", "height": 6, "weight": 85},
            {"name": "squirtle", "height": 5, "weight": 90},
            {"name": "bulbasaur", "height": 7, "weight": 69}
        ]
        
        mock_response = MagicMock()
        mock_response.json = MagicMock(return_value=expected_data[0])
        
        with patch("aiohttp.ClientSession.get") as mock_get:
            mock_get.return_value.__aenter__ = MagicMock(return_value=mock_response)
            mock_get.return_value.__aexit__ = MagicMock(return_value=None)
            
            actual_data = await PokemonFetcher.get_multiple_pokemon_data(pokemon_names)
            
            self.assertEqual(actual_data, expected_data)
