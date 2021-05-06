# -*- coding: utf-8 -*-
"""
Created on Wed May  5 05:38:00 2021

@author: v-kgordon
"""

"""
Load a dictionary file
Accept a name from user
Set limit = length of name
Start empty list to hold anagram phrase
While length of phrase < limit:
    Generate list of dictionary words that fit in name
Present words to user
Present remaining letters to user
Present current phrase to user
Ask user to input word or start over
If user input can be made from remaining letters:
Accept choice of new word or words from user
Remove letters in choice from letters in name
Return choice and remaining letters in name
If choice is not a valid selection:
Ask user for new choice or let user start over
Add choice to phrase and show to user
Generate new list of words and repeat process
When phrase length equals limit value:
Display final phrase
Ask user to start over or to exit
"""

test = 'I am Lord Voldemort'
test_1 = 'Tom Marvolo Riddle'
#Since there are 3 spaces in test and only 2 in test_1, we need to replace the spaces with nothing. 
test = test.replace(' ', '')
test_1 = test_1.replace(' ', '')

# Building test 1

# For each word in the words list 
# Aah 
# Could we take Aah out of test? 
# No. Because Aah has 2 A's and an H, and I am Voldemort only have a single A.
# Lot
# Could we take Lot out of test?
# Yes. The letters in lot also appear in Voldemort

# import collections (Instead of importing the whole library, make the program run more effieciently by only importing the part we need)
from collections import Counter 

test = Counter(test.lower())
print(test)
#Result - Counter({'o': 3, 'm': 2, 'l': 2, 'r': 2, 'd': 2, 'i': 1, 'a': 1, 'v': 1, 'e': 1, 't': 1})


test_1 = Counter(test_1.lower())
print(test_1)
#Result - Counter({'o': 3, 'm': 2, 'r': 2, 'l': 2, 'd': 2, 't': 1, 'a': 1, 'v': 1, 'i': 1, 'e': 1})

if test == test_1:
    print('This is an Anagram phrase')  
    
# See if test_word can come out of test
test_word = 'mold'
test_word_map = Counter(test_word)
for i in test_word:
    print(i) 
    print(test_word_map[i])
    '''
m
1
o
1
l
1
d
1
'''
    print(test[i])
'''
When compared to test_word_map first number is from mold, second from test. 
m
1
2
o
1
3
l
1
2
d
1
2
'''
print(test_word)
print(test)
#test word - mold = Counter({'m': 1, 'o': 1, 'l': 1, 'd': 1})
#test - Counter({'o': 3, 'm': 2, 'l': 2, 'r': 2, 'd': 2, 'i': 1, 'a': 1, 'v': 1, 'e': 1, 't': 1})

for i in test_word:
    print('for letter ' + i)
    print('in mold, there is ' + str(test_word_map[i]) + ' ' + i)
    print('in I am Lord Voldemort, there is ' + str(test[i]) + ' ' + i)
    print()
''' 
for letter m
in mold, there is 1 m
in I am Lord Voldemort, there is 2 m

for letter o
in mold, there is 1 o
in I am Lord Voldemort, there is 3 o

for letter l
in mold, there is 1 l
in I am Lord Voldemort, there is 2 l

for letter d
in mold, there is 1 d
in I am Lord Voldemort, there is 2 d
'''
anagram = ''

for i in test_word:
    if test_word_map[i] <= test[i]:
        print('Adding ' + i + ' to Anagram')
        anagram = anagram + i 
        print('Current Anagram: ' + anagram)
        print()
'''
Adding m to Anagram
Current Anagram: m

Adding o to Anagram
Current Anagram: mo

Adding l to Anagram
Current Anagram: mol

Adding d to Anagram
Current Anagram: mold
'''

test_word_2 = 'demolish'
test_word_2_map = Counter(test_word_2)

for i in test_word_2:
    print('for letter ' + i)
    print('in demolish, there is ' + str(test_word_2_map[i]) + ' ' + i)
    print('in I am Lord Voldemort, there is ' + str(test[i]) + ' ' + i)
    print()
'''
for letter d
in demolish, there is 1 d
in I am Lord Voldemort, there is 2 d

for letter e
in demolish, there is 1 e
in I am Lord Voldemort, there is 1 e

for letter m
in demolish, there is 1 m
in I am Lord Voldemort, there is 2 m

for letter o
in demolish, there is 1 o
in I am Lord Voldemort, there is 3 o

for letter l
in demolish, there is 1 l
in I am Lord Voldemort, there is 2 l

for letter i
in demolish, there is 1 i
in I am Lord Voldemort, there is 1 i

for letter s
in demolish, there is 1 s
in I am Lord Voldemort, there is 0 s

for letter h
in demolish, there is 1 h
in I am Lord Voldemort, there is 0 h
'''

anagram = ''

for i in test_word_2:
    if test_word_2_map[i] <= test[i]:
        print('Adding ' + i + ' to Anagram')
        anagram = anagram + i 
        print('Current Anagram: ' + anagram)
        print()
'''
Adding d to Anagram
Current Anagram: d

Adding e to Anagram
Current Anagram: de

Adding m to Anagram
Current Anagram: dem

Adding o to Anagram
Current Anagram: demo

Adding l to Anagram
Current Anagram: demol

Adding i to Anagram
Current Anagram: demoli
'''