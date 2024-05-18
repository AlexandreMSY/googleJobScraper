import toml
import os


def readToml(path):
    file = open(path, "r")
    fileContent = file.read()

    parsedToml = toml.loads(fileContent)

    return parsedToml
