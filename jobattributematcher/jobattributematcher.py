from typing import Type
from user.userdetails import User
from jobattributematcher.arraywordcounter import arrayWordMatcher


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
        userDegrees = self.user.degrees
        jobRequiredDegrees = self.jobAttributes["degree"]
        
        return arrayWordMatcher(userDegrees, jobRequiredDegrees)

    def attributesMatched(self) -> dict:
        skills = self.__matchSkills()
        languages = self.__matchLanguages()
        degrees = self.__matchDegrees()
        
        return {
            "skills": {"numOfWordsMatched": skills["numOfWordsMatched"], "wordsFound": skills["wordsFound"]},    
            "languages": {"numOfWordsMatched": languages["numOfWordsMatched"], "wordsFound": languages["wordsFound"]},    
            "degrees": {"numOfWordsMatched": degrees["numOfWordsMatched"], "wordsFound": degrees["wordsFound"]}    
        }