import csv
typecast = {
    "TEXT": str,
    "INTEGER": int,
    "BOOLEAN": bool
}

class Schema:
    """ Contains a string schema for breaking text into objects
        using the casting method for that type
    """
    def __init__(self, fields):
        self._fields = fields

    def parse_row(self, string_data):
        """ Take a textfile row and return a dict from it """
        parsed = {}
        string_data = string_data.replace(u'\u200b', '')
        for field in self._fields:
            parsed[field.name] = field.type_method(string_data[field.start_index:field.end_index])
        return parsed

    @staticmethod
    def from_csvfile(csv_filename):
        """ Instantiate a Schema object from a csvfile """
        fields = []
        with open(csv_filename, encoding="utf-8") as csv_data:
            csv_reader = csv.reader(csv_data, delimiter=",")
            start_index = 0
            for name, width, datatype in csv_reader:
                datatype = datatype.strip('\u200b').upper()
                width = int(width.strip('\u200b'))
                name = name.strip('\u200b')
                if datatype not in typecast:
                    raise ValueError(f"Unknown datatype {datatype}")

                fields.append(Field(name=name,
                                    start_index = start_index,
                                    end_index = start_index + width,
                                    type_method=typecast[datatype]))
                start_index += width
        return Schema(fields=fields)


class Field:
    """ Contains a field from schema """
    def __init__(self, type_method, start_index, end_index, name):
        self.type_method = type_method
        self.start_index = start_index
        self.end_index = end_index
        self.name = name


