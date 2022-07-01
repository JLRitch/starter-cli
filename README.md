# starter-cli
A template cli to get you up and running with click

# Install (local dev with venv)
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

# Run commands

## Check version

```shell
python -m pycli --version
```
Output:

```
Running pycli version 0.0.1 with CPython 3.8.10 on Linux
```

## Check for nerd

```shell
python -m pycli --nerd
```
Output:

```
WARNING: A NEW CLI APPROACHES!!
```

## Read requirements.txt

```shell
python -m pycli extract deps -f requirements.txt
```
Output:

```
click==8.1.3
colorama==0.4.5
Successfully read packages!!
```