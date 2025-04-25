
import json
import os
import csv


class TestData:
    @staticmethod
    def get_json_data(file_name):
        test_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_name))
        with open(test_data_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def get_csv_data(file_name):
        test_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_name))
        data = []
        with open(test_data_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data