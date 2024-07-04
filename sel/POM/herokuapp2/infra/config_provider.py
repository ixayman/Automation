import json


class ConfigProvider:

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'r') as f:
                config = json.load(f)
                print(f"Config loaded: {config}")
                return config
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty configuration.")
            return {}
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {filename}. Starting with an empty configuration.")
            return {}