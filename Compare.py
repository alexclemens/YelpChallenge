def reposition(classifier, photoID):
    import re
    import os
    
    photoName = photoID + ".jpg"
    newFolder =  "/Users/chriscziesla/Downloads/" + classifier + "/" + photoName
    oldFolder = "/Users/chriscziesla/Downloads/yelp_photos/photos/" + photoName
    if os.path.isfile(oldFolder):
        os.rename(oldFolder, newFolder)
    return

def compare(old):
    import string
    tf = open(old, 'r')
    classify = ""
    classifiers = ['hamburger', 'chicken', 'pizza', 'steak', 'sandwich', 'cheeseburger', 'fries', 'salad', 'breakfast','wings', 'beef', 'pasta', 'fruit', 'eggs', 'tuna']
    for line in tf:
        par = line.split("'")
        cap = par[3]
        photoID = par[5]
        parCap = cap.split(" ")
        for i in range(0, len(parCap)):
            testWord = parCap[i].lower()
            testWord2 = testWord.translate(None, string.punctuation)
            for j in range(0, len(classifiers)):
                if testWord2 == classifiers[j]:
                    classify = classifiers[j]
                    reposition(classify, photoID)
                    break
                
            
            
                    
