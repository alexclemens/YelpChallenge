import json
import yaml
import requests


food = 0
inside = 0
outside = 0

label = 0
caption = 0


with open("photos.json") as myfile:
    curr = [yaml.safe_load(next(myfile)) for x in xrange(196278)]

for curr_string in curr:

    if curr_string.get('caption') != "":
    	caption += 1
    if curr_string.get('label') == 'food':
    	food+=1
    	label+=1
    elif curr_string.get('label') == 'inside':
    	inside+=1
    	label+=1
    elif curr_string.get('label') == 'outside':
    	outside+=1
    	label+=1

#print curr
print "reviews with a label: " + str(label)
print "Label is food: " + str(food)
print "Label is inside: " + str(inside)
print "Label is outside: " + str(outside)
print "reviews with captions: " +  str(caption)