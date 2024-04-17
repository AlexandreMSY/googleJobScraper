from datetime import date

class Degree:
    def __init__(self, name : str, degreeType : str, startDate : date, endDate : date = None):
        self.name = name
        self.type = degreeType
        self.startDate = startDate
        self.endDate = endDate