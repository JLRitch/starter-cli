# standard imports
import getpass
import platform

# external imports
import click

# project imports
import pycli
from pycli.extractors import PyExtractor


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