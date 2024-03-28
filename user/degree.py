from datetime import date

class Degree:
    def __init__(self, degreeName : str, degreeType : str, startDate : date, endDate : date = None):
        self.name = degreeName
        self.type = degreeType
        self.startDate = startDate
        self.endDate = endDate