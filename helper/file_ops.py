import yaml


class Yaml:
    def read(self, path):
        with open(path, "r") as file:
            try:
                content = yaml.safe_load(file)
                return content
            except yaml.YAMLError as exc:
                print(exc)


class Txt:
    def read(self, path):
        with open(path, "r") as file:
            try:
                content = file.read()
                return content
            except FileNotFoundError as exc:
                print(exc)
