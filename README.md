![Alt text](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1cccbcdd-92bd-44d6-b5f6-d7959eddf41b/d3jcvxa-c2b65d35-e3fe-46ce-bf06-9a3cf4fa56f4.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvMWNjY2JjZGQtOTJiZC00NGQ2LWI1ZjYtZDc5NTllZGRmNDFiXC9kM2pjdnhhLWMyYjY1ZDM1LWUzZmUtNDZjZS1iZjA2LTlhM2NmNGZhNTZmNC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.O94hGo-lvqhDxD9gL8sEgT_e70LnVEFJA0Ug6Xh0XZY "HP Banner")

# Harry Potter Anagrams


![Alt text](https://smedia2.intoday.in/indiatoday/images/stories/2016May/18_051316044939.jpg "Lord Voldemort")

An anagram is a word formed by rearranging the letters of another word. For example, in the book Harry 
Potter and the Chamber of Secrets, “I am Lord Voldemort” is an anagram of the evil wizard’s real name, 
Tom Marvolo Riddle. “Lord Ear Mold Vomit” is also an anagram of Tom Marvolo Riddle, but that would really make the guy a 
"he who should not be named". 

But enough fan girling, let's get into the code!

First, we want the user to enter a word to see if it has an anagram. This word is checked against an imported dictionary file. 

```
User_word = input('Enter your word to see if it is an Anagram: ') 
```
We then want to have that word formated properly so that it can me checked against our completed lower case dictionary.
```
print('Input name = {}\nUsing name: {}'.format(User_word, User_word.lower()))
```
Finally, in order to see if one word equals the other, we need to sort the letters in the word we have and the word in the dictionary to see if they are an anagram. 
```
sorted_word = sorted(User_word.lower())
```
Great! Our words are properly formated and we are ready to get to work. 
We want to take each word in the dictionary list and so long as it doesn't equal the word (It is the same word and thus not an Anagram) then we continue through the loop.
We will sort each word and compare them.
Then if a sorted word equals the user's input word, the dictionary word is appended to an Anagram list we made. 
```
for word in word_list: 
    if word.lower() != User_word.lower():
        if sorted(word) == sorted_word:
            anagram_list.append(word)
```
We then want to print the list of words for the user. But we don't want it to look like a functional python list so we use the '*' 
function and seperate each word onto a new line with '\n'. We could also have seperated them out by a ',' for a one line list.  
```
print(*anagram_list, sep='\n') 
```
Now, if we run this program and input 'LoW', here is our result!

```
Enter your word to see if it is an Anagram: LoW
Input name = LoW
Using name: low
owl
['l', 'o', 'w']
['l', 'o', 'w']
Sorted low and owl are Anagrams
```
I showed how our program took in the user's word, changed it to lower case, sorted it, and compared the word to sorted dictionary words.
After seeing that the return was 'owl' I input the two words and printed them out sorted so that you can see how this result was given. 
```
x = 'low'
y = 'owl'

sorted_x = sorted(x) 
sorted_y = sorted(y)

if sorted(x) == sorted(y):
    print('Sorted ' + x + ' and ' + y + ' are Anagrams') 
```
We found Hedwig! 

![Alt text](https://th.bing.com/th/id/OIP._VCwlxA3S6z5AvJ1sQN8aQHaFj?pid=ImgDet&rs=1 "Owl Anagram")

