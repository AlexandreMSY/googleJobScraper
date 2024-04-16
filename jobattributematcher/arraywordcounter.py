def arrayWordMatcher(array1: list[str], array2: list[str]):
    wordsMatched = 0
    wordsFound = []

    for wordInArray1 in array1:
        wordInArray1 = str(wordInArray1).lower()
        for wordInArray2 in array2:
            wordInArray2 = str(wordInArray2).lower()
            if wordInArray2.find(wordInArray1) != -1:
                wordsFound.append(wordInArray2)
                wordsMatched += 1

    return {"numOfWordsMatched": wordsMatched, "wordsFound": wordsFound}
