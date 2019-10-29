"""
A parser that uses a schema to process a text file and post the resulting rows to a URL
"""
import argparse
from pathlib import Path
import os
import requests

from models.schema import Schema

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='an integer for the accumulator',
                        default="https://2swdepm0wa.execute-api.us-east-1.amazonaws.com/prod/NavaInterview/measures",
                        required=False)
    parser.add_argument('--data_path', help="a path to datafiles", default="./data", required=False)
    parser.add_argument('--schema_path', help="a path to schemafiles", default="./schemas", required=False)
    parser.add_argument('--dry_run', help="Don't call the service, just print the requests", default=False, action='store_true', required=False)
    args = parser.parse_args()

    data_path = Path(args.data_path)

    for data_file in data_path.glob('*.txt'):
        print(f"Processing: {data_file.name}")
        schema_file = os.path.join(args.schema_path, schema(data_file.name))
        process_data(datafile=data_file, schemafile=schema_file, url=args.url, dry_run=args.dry_run)

    
def process_data(datafile, schemafile, url, dry_run=False):
    """ Given a data file path and a schema file path, 
        instantiate the schema file, use it to parse the data file,
        and make requests to the given URL
    """
    schema = Schema.from_csvfile(schemafile)
    with open(datafile, encoding='utf-8') as datafile:
        for row in datafile:
            parsed_row = schema.parse_row(row)
            if dry_run:
                print(parsed_row)
            else:
                response = requests.post(url, json=parsed_row)
                response.raise_for_status()


def schema(datafile):
    """ This is naive as heckfire 
    """
    return datafile.replace('txt', 'csv')

if __name__ == "__main__":
    main()
