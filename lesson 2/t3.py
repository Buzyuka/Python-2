import yaml

source_data = {
    "list": [
        "Item 1",
        "Item 2",
        "Item 3",
    ],
    "int": 123,
    "nest": {
        1: "\u0024",
        2: "\u00D8",
        3: "\u00A9"
    }
}


def write_yaml(data, file_name):
    with open(file_name, "w") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


def load_yaml(file_name):
    with open(file_name) as f:
        return yaml.load(f)


write_yaml(source_data, "file.yaml")
loaded_data = load_yaml("file.yaml")

assert (loaded_data == source_data)
