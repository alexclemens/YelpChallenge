import json
import yaml
import requests


food = 0
inside = 0
outside = 0

label = 0
caption = 0
keys = ['food', 'inside', 'outside', 'label', 'caption']
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

#print curr
print "reviews with a label: " + str(dictionary['label'])
print "Label is food: " + str(dictionary['food'])
print "Label is inside: " + str(dictionary['inside'])
print "Label is outside: " + str(dictionary['outside'])
print "reviews with captions: " +  str(dictionary['caption'])