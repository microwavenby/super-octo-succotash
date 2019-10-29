# super-octo-succotash

A tool for processing some data based on schemas

Sasha Z Reid
@microwavenby

## Note:

I did not provide the data / schema directories in an empty form within this Git repo;
there are the example files pasted from the PDF in the `test/fixtures/data` and `test/fixtures/schemas` paths.

The script does take command line options including `--help` and can be passed an arbitrary `schemas` and `data` path;
one could for instance do `python parser/parser.py --data_path=./test/fixtures/data/ --schema_path=./test/fixtures/schemas/ --dry_run`, for instance.


## Execution

### Using PIP

1. pip3 install -r requirements.txt
2. python3 parser/parser.py

### Using virtualenv

1. virtualenv --python=python3 venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python parser/parser.py

## Running Tests

### Using PIP

1. pip3 install -r requirements.txt
2. pytest

### Using virtualenv

1. virtualenv --python=python3 venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. pytest
