import google.generativeai as genai

"""
This class is a tool for checking if 2 degree arrays are closely related using Gemini
"""

class DegreeRelationChecker:
    def __init__(self, geminiApiKey : str, degreeArray1 : list, degreeArray2 : list) -> None:
        self.geminiApiKey = geminiApiKey
        self.degreeArray1 = degreeArray1
        self.degreeArray2 = degreeArray2
        
        self.__GEMINI_PROMPT_MESSAGE = f"""
            degrees = {str(self.degreeArray1)}

            are the elements in the array closely related to the array elements below?

            "degrees": {str(self.degreeArray2)}

            answer with True or False only, do not use any more words or observations
        """
        
        genai.configure(api_key=self.geminiApiKey)
        self.model = genai.GenerativeModel("gemini-pro")
        
    def checkRelation(self) -> bool:
        response = self.model.generate_content(self.__GEMINI_PROMPT_MESSAGE)
        return bool(response.text)