# standard imports
import asyncio

# external imports
import aiohttp

# project imports


class PokemonFetcher(object):

    def __init__(self):
        self.name = "A python extractor object"

    async def get_pokemon_data(self, name):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://pokeapi.co/api/v2/pokemon/{name}") as response:
                if response.status != 200:
                    return None
                data = await response.json()
                return data

    async def get_multiple_pokemon_data(self, pokemon_names):
        tasks = []
        async with aiohttp.ClientSession() as session:
            for name in pokemon_names:
                task = asyncio.ensure_future(self.get_pokemon_data(name))
                tasks.append(task)
            pokemon_data = await asyncio.gather(*tasks)
            return pokemon_data