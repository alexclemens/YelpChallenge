

def reposition(txt):
    import re
    import os

    tf = open(txt)
    
    for line in tf:
        fileName = re.sub(r"\'(.+?)\'", r'', line)
        temp = ".jpg"
        photoName = fileName + temp
        old = "/Users/chriscziesla/Downloads/yelp_photos/photos" + photoName
        new = "/Users/chriscziesla/Downloads/food_with_captions_id" + photoName
        os.rename(old, new)
    return
