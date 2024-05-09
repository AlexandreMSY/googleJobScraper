from typing import Type
from user.userdetails import User
from geminiTools.jobattributematcher.arraywordmatcher import arrayWordMatcher
from geminiTools.degree_relation_checker import DegreeRelationChecker
from dotenv import load_dotenv
import os

load_dotenv(".env")


class JobAttributeMatcher:
    def __init__(self, user: Type[User], jobAttributes: dict):
        self.user = user
        self.jobAttributes = jobAttributes

    def __matchSkills(self) -> dict:
        userSkills = self.user.skills
        jobRequiredSkills = self.jobAttributes["skills"]

        jobRequiredHardSkills = jobRequiredSkills["hard"]

        return arrayWordMatcher(userSkills, jobRequiredHardSkills)

    def __matchLanguages(self) -> dict:
        userLanguages = self.user.languages
        jobRequiredLanguages = self.jobAttributes["languages"]

        return arrayWordMatcher(userLanguages, jobRequiredLanguages)

    def __matchDegrees(self) -> dict:
        userDegrees = []
        degreeObjects = self.user.degrees
        jobRequiredDegrees = self.jobAttributes["degrees"]

        for object in degreeObjects:
            userDegrees.append(object.name)
        
        wordsFound = arrayWordMatcher(userDegrees, jobRequiredDegrees)
        
        if wordsFound['numOfWordsMatched'] == 0:
            if len(jobRequiredDegrees) == 0: pass
            
            degreeRelation = DegreeRelationChecker(os.getenv("GEMINI_API_KEY"), userDegrees, jobRequiredDegrees)
            degreesRelated = degreeRelation.checkRelation()
            
            if degreesRelated:
                return {'numOfWordsMatched': len(userDegrees), 'wordsFound': userDegrees}
            else:
                return {'numOfWordsMatched': 0, 'wordsFound': []}
            
        else:
            return wordsFound

    def attributesMatched(self) -> dict:
        skills = self.__matchSkills()
        languages = self.__matchLanguages()
        degrees = self.__matchDegrees()

        return {
            "skills": {
                "numOfWordsMatched": skills["numOfWordsMatched"],
                "wordsFound": skills["wordsFound"],
            },
            "languages": {
                "numOfWordsMatched": languages["numOfWordsMatched"],
                "wordsFound": languages["wordsFound"],
            },
            "degrees": {
                "numOfWordsMatched": degrees["numOfWordsMatched"],
                "wordsFound": degrees["wordsFound"],
            },
        }
