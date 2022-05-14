import yaml

def read_parameters():
    with open("../config/parameters.yml", "r") as stream:
        try:
            credentials = yaml.safe_load(stream)
            return credentials
        except yaml.YAMLError as exc:
            print(exc)
            return None


parameters = read_parameters()