# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 23:01:24 2019

Count the number of words in northwind.txt using different methods
For 

@author: Chris Seymour
"""

import collections as coll

file = 'northwind.txt'

with open(file, 'r') as f:
    words = f.read().split()
#    print(words)
    swords = [] #list to store the cleaned-up words
    for word in words:
        strip_word = word.strip(',').strip('.') #remove any punctuation #.strip(':') etc...
#        print(strip_word)
        swords.append( strip_word.lower() ) #convert to lower case letters, and add the word to the new list

#print(swords)
print("\n--== with a list ==--\n")
word_counts = []
#loop through the stripped words and count the number of times each one appears
for word in swords:
    #swords.count('the') will count the number of times 'the' appears in the word list
    word_counts.append( swords.count(word) )
    print('The word "', word,'" appeared ', word_counts[-1],' times' , sep='')
    
print("\n--== with a dictionary ==--\n")
count_dict = {}
for word in swords:
    if word not in count_dict: #if "word" isn't a key in the dictionary yet, add it
        count_dict[word] = 0 #use an int to store the number of counts for this word
    count_dict[word] += 1 #increase the count by 1

for key in count_dict.keys():
#   print(d[key]) #the number of counts is associated with the word itself!
    print('The word "{}" appeared {} times'.format(key, count_dict[key]) )
  
print("\n--== with a collections.Counter() ==--\n")      
counter = coll.Counter()
for word in swords:
    counter[word] += 1
 
  
print(counter, '\n')
print("Counter version is the same as our standard dictionary:")
print( dict( counter ) == count_dict ) 
