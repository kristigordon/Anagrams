# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import Load_dictionary

word_list = Load_dictionary.load('2of4brif.txt') 

anagram_list = []

User_word = input('Enter your word to see if it is an Anagram: ') 
# Lower_word = User_word.lower() (Another way of getting a lower word as a new variable)
print('Input name = {}\nUsing name: {}'.format(User_word, User_word.lower()))

# Could also do sorted_word = sorted(Lower_word)
sorted_word = sorted(User_word.lower())


for word in word_list: 
    if word.lower() != User_word.lower():
        if sorted(word) == sorted_word:
            anagram_list.append(word)
# * allows the list to be formated so it doesn't look like a list, instead a series of words without punctuation
print(*anagram_list, sep='\n') 

x = 'silent'
y = 'listen'

print(list(x))
print(list(y))

sorted_x = sorted(x) 
sorted_y = sorted(y)

print(list(x))
print(list(y))

print(sorted_x)
print(sorted_y)

if sorted_x == sorted_y:
    print('x and y are Anagrams')

if sorted(x) == sorted(y):
    print('Sorted ' + x + ' and ' + y + ' are Anagrams') 