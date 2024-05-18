import toml
import os

tomlContent = """
[GOOGLE]
location_max_distance = 0                 # Use: 0 = 2km, 1 = 10km, 2 = 25km, 3 = 50km, 4 = 100km, 5 = 300km, 6 = Anywhere
max_date_posted = 0                       # Use: 0 = All, 1 = Past day, 2 = Past 3 days, 3 = Past week, 4 = Past month
"""


def createToml(path : str = "."):
    path = f"{path}/config.toml"
    isFileCreated = os.path.exists(path)

    if isFileCreated:
        return
    else:
        print("toml config file generated")
        file = open(path, "w")
        file.write(tomlContent)
        file.close()
