# starter-cli
A template cli to get you up and running with click

# Setup local dev with venv
1) clone repo
2) make and activate venv

```shell
python3 -m venv env
source env/bin/activate
```
3) install requirements
```shell
python -m pip install -r requirements.txt
```
# Install from cloned repo
```shell
pip install .
```

# Run commands

## Check version

```shell
# if setup for local dev
python -m pycli --version

# if installed as cli
pycli --version
```
Output:

```
Running pycli version 0.0.1 with CPython 3.8.10 on Linux
```

## Check for nerd

```shell
# if setup for local dev
python -m pycli --nerd

# if installed as cli
pycli --version
```
Output:

```
WARNING: A NEW CLI APPROACHES!!
```

## Read requirements.txt

```shell
# if setup for local dev
python -m pycli extract deps -f requirements.txt

# if installed as cli
pycli extract deps -f requirements.txt
```
Output:

```
click==8.1.3
colorama==0.4.5
Successfully read packages!!
```

## Collect Pokemon

```shell
pycli fetch pokemon --name=bulbasaur,charmander
```