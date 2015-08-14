
def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.
    returns: string - story in plain text
    """
    ciphertext = getStoryString()
    wordList = loadWords()
    shift = findBestShift(wordList, ciphertext)
    return applyShift(ciphertext, shift)