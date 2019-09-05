from pprint import pprint
from characters import characters

#1 How many characters names start with "A"?
for character in characters:
    #if character['name'][0] == 'A':
        #pprint(character['name'])
    if character['name'].startswith('A') == True:
        pprint(character['name'])
#2 How many characters names start with "Z"?
for character in characters:
    if character['name'].startswith('Z') == True:
        pprint(character['name'])
#3 How many characters are dead?
for character in characters:
        if character['died'] != '':
                pprint(character['died'])
#4 Who has the most titles?
for character in characters:
        if len(character['titles']) > 1:
                pprint(character['titles'])
"""        if len(character['titles']) > 0:
                pprint(len(character['titles']))"""

#5 How many are Valyrian?
for character in characters:
        if character['culture'] == 'Valyrian':
                pprint(character['culture'])
#6 What actor plays "Hot Pie" (and don't use IMDB)?
for character in characters:
        if len(character['playedBy']) > 1:
                pprint(character['playedBy'])
        if character['name'] == 'Hot Pie':
                pprint(character['name'])
#7 How many characters are *not* in the tv show?
"""for character in characters:
        if character['playedBy'] > 1:
s#8 Produce a list characters with the last name "Targaryen"

#9 Create a histogram of the houses (it's the "allegiances" key)

# print(len(characters))
"""
"""for a in b:
        if a == True
        x += 1
        print(x)
# # print out the key names individually
# for k in jon_snow:
#    print(k)
"""
# # print out just the values
# for key in jon_snow:
#    print(jon_snow[key])

# # print both the key and the value
# for k in characters.jon_snow:
#    print("%s: %s" % (k, jon_snow[k]))