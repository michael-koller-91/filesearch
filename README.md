# Filesearch

A command line tool written in Python to find files and file contents matching (Python) regex patterns.

## Example usage

Print the usage help:
```bash
filesearch
```

Find all files ending with `.py`:
```bash
filesearch ".*.py\b"
```

Find all files ending with `.py` but exclude files in the folder `.git`:
```bash
filesearch ".*.py\b" ".git"
```

In all files ending with `.py` but excluding files in the folder `.git`, find lines containing `def`:
```bash
filesearch ".*.py\b" ".git" "def"
```

In the previous example, also print the 3 lines before and after the matching line
```bash
filesearch ".*.py\b" ".git" "def" 3
```

## Installation
### Option 1 (recommended): Install as standalone command line tool

If you want to be able to run `filesearch` from anywhere in the terminal, you can use the following two commands.
First, create a source distribution with
```bash
python setup.py sdist
```

Second, use [pipx](https://github.com/pypa/pipx) to install and be able to run the application in an isolated environment:
```bash
python -m pipx install .
```
This requires `pipx` to be installed (e.g., via `python -m pip install pipx`).

### Option 2: No installation

If you only want to use [main.py](filesearch/main.py), no packages need to be installed.
Navigate to [filesearch/](filesearch/) and use
```bash
python main.py --help
```
to get instructions on how to use the tool.
