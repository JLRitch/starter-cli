# standard imports
import pathlib
# external imports

# project imports


def abs_path(fpath: str) -> pathlib.Path:
    """
    Takes a path string and converts to absolute path if it is relative
    """

    if pathlib.Path(fpath).is_absolute():
        return pathlib.Path(fpath)
    else:
        return pathlib.Path().cwd().joinpath(fpath)