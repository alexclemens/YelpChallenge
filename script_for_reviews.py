import json
import yaml
import requests


keys = ['food', 'inside', 'outside', 'label', 'caption', 'food_and_caption', 'food_and_no_caption']
dictionary = dict.fromkeys(keys, 0)


with open("photos.json") as myfile:
    curr = [yaml.safe_load(next(myfile)) for x in xrange(196278)]

for curr_string in curr:

    if curr_string.get('caption') != "":
    	dictionary['caption'] += 1


    if curr_string.get('label') == 'food':
    	dictionary['food'] += 1
        dictionary['label'] += 1
    elif curr_string.get('label') == 'inside':
    	dictionary['inside'] += 1
    	dictionary['label'] += 1
    elif curr_string.get('label') == 'outside':
    	dictionary['outside'] += 1
    	dictionary['label'] += 1

        
    if curr_string.get('label') == 'food' and curr_string.get('caption') != "":
        dictionary['food_and_caption']+=1
    elif curr_string.get('label') == 'food' and curr_string.get('caption') == "":
        dictionary['food_and_no_caption']+=1


print "reviews with a label: " + str(dictionary['label'])
print "Label is food: " + str(dictionary['food'])
print "Label is inside: " + str(dictionary['inside'])
print "Label is outside: " + str(dictionary['outside'])
print "reviews with captions: " +  str(dictionary['caption'])
print "food and caption " + str(dictionary['food_and_caption'])
print "food and no caption " + str(dictionary['food_and_no_caption'])
