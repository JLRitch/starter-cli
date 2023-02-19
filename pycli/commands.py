# standard imports
import getpass
import platform
import asyncio
import json

# external imports
import click

# project imports
import pycli
from pycli.extractors import PyExtractor
from pycli.fetchers import get_multiple_pokemon_data


###############
### Module-level variables
###############
user = getpass.getuser()

###############
### Call back functions
###############
def print_version(
    ctx: click.Context,
    param: click.Parameter,
    value: bool
) -> None:
    if not value or ctx.resilient_parsing:
        return
    click.echo(
        f"Running pycli version {pycli.__version__} with {platform.python_implementation()} {platform.python_version()} on {platform.system()}"
    )
    ctx.exit()

def nerd(
    ctx: click.Context,
    param: click.Parameter,
    value: bool
) -> None:
    """
    For the funnies.
    """
    if not value or ctx.resilient_parsing:
        return
    click.echo(click.style(f"WARNING: A NEW CLI APPROACHES!! RUN AWAY {user}",  bg='red', fg='white'))
    ctx.exit()


###############
### cli base
###############
@click.group("pycli")
@click.option(
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Display the pycli version and exit.",
)
@click.option(
    "--nerd",
    is_flag=True,
    callback=nerd,
    expose_value=False,
    is_eager=True,
    help="pycli nerds"
)
def app():
    # present only for sub-commands
    pass

###############
### extract commands
###############
@app.group("extract")
def create():
     # present only for sub-commands
    pass

@create.command("deps")
@click.option(
    "-f",
    "--file_path",
    type=str,
    help="The path to the dependency file you want to read"
)
@click.option(
    "-d",
    "--dependency_list_type",
    type=click.Choice(['requirements.txt', 'setup.py']),
    help="The type of dependency list being scanned (i.e. requirements.txt or package.json)"
)
def extract_dependencies(
    file_path: str,
    dependency_list_type: str
):
    """
    extract_depenedencies reads a dependency manifest file and prints package/version
    """
    extractor = PyExtractor()
    extractor.read_requirements("requirements.txt")

    click.echo(click.style(f"Successfully read packages!!", fg="green"))

###############
### fetch commands
###############
@app.group("fetch")
def create():
     # present only for sub-commands
    pass

@create.command("pokemon")
@click.option(
    "-n",
    "--names",
    type=str,
    help="The names of the pokemon you want to fetch data for"
)
@click.option(
    "--testing",
    is_flag=True,
    expose_value=True,
    is_eager=True,
    help="Enables test mode on cli commands.",
)
def fetch_pokemon(
    names: str,
    testing: bool=False
):
    """
    fetch_pokemon gets data from the pokemon api for the provided pokemon
    """
    pokemon_names = names.split(",")
    if testing:
        pokemon_data = [{"name": name, "height": 1, "weight": 1} for name in pokemon_names]
        click.echo(
            json.dumps(pokemon_data)
        )
        return pokemon_data
    async def fetch_request():
        pokemon_data = await get_multiple_pokemon_data(pokemon_names)
        return pokemon_data
    pokemon_data = asyncio.run(fetch_request())
    click.echo(json.dumps(pokemon_data, indent=4))
