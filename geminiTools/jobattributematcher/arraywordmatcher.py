import unidecode
from difflib import SequenceMatcher

def arrayWordMatcher(array1: list[str], array2: list[str]):
    wordsMatched = 0
    wordsFound = []

    for wordInArray1 in array1:
        wordInArray1 = str(wordInArray1).lower()
        wordInArray1 = unidecode.unidecode(wordInArray1)
        
        for wordInArray2 in array2:
            wordInArray2 = str(wordInArray2).lower()
            wordInArray2 = unidecode.unidecode(wordInArray2)
            
            if wordInArray1 in wordInArray2:
                if wordInArray2 in wordsFound:
                    pass 
                else:
                    wordsFound.append(wordInArray2)
                    wordsMatched += 1

    return {"numOfWordsMatched": wordsMatched, "wordsFound": wordsFound}
