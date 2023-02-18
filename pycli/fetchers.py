# standard imports
import asyncio

# external imports
import aiohttp

# project imports


async def get_pokemon_data(name):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://pokeapi.co/api/v2/pokemon/{name}") as response:
            if response.status != 200:
                return None
            data = await response.json()
            return data

async def get_multiple_pokemon_data(pokemon_names):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for name in pokemon_names:
            task = asyncio.ensure_future(get_pokemon_data(name))
            tasks.append(task)
        pokemon_data = await asyncio.gather(*tasks)
        return pokemon_data

if __name__ =="__main__": # pragma: no cover
    async def main():
        pokemon_names = ["pikachu", "charmander", "squirtle", "bulbasaur"]
        pokemon_data = await get_multiple_pokemon_data(pokemon_names)
        print(pokemon_data)

    asyncio.run(main())