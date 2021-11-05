import yaml


def read_yaml(f):
    with open(f, "r") as con:
        x = yaml.safe_load(con)
    return x