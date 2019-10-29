import os
import pytest
import json
from parser.models.schema import Schema, Field

@pytest.fixture
def fixture_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures')

@pytest.fixture
def schema_path(fixture_path):
    return os.path.join(fixture_path, 'schemas')

@pytest.fixture
def data_path(fixture_path):
    return os.path.join(fixture_path, 'data')

@pytest.fixture
def expected_data(fixture_path):
    return json.load(open(os.path.join(fixture_path, "parsed/booleanmeasures.json")))

@pytest.fixture
def schema_instance(schema_path):
    return Schema.from_csvfile(os.path.join(schema_path, "booleanmeasures.csv"))

class TestExampleSchema:
    def test_instantiate_schema(self, schema_path):
        schema_instance = Schema.from_csvfile(os.path.join(schema_path, "booleanmeasures.csv"))
        assert len(schema_instance._fields) is 4
    
    def test_parse_data(self, schema_instance, data_path, expected_data):
        parsed_rows = []
        with open(os.path.join(data_path, "booleanmeasures.txt"), encoding='utf-8') as datafile:
            for row in datafile:
                parsed_rows.append(schema_instance.parse_row(row))        
        assert parsed_rows == expected_data


