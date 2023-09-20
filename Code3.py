#!/usr/bin/env python
# coding: utf-8

# In[8]:


# problem
name = input("enter your name: ")
print(f"Hello, {name}! Nice to meet you.")
print("Hello, "+ name +"! Nice to meet you.")



      


# In[12]:


# problem 2
word = input("enter a word: ")
reversed_word = word[::-1]
print(f"Reversed word: {reversed_word}.")


# In[13]:


# problem 3
sentence = input("enter a sentence: ")
char_count = len(sentence)
print(f"this sentence has {char_count} characters.")


# In[14]:


# problem 4
string = input("enter a word or a sentence: ")

string_lower = string.lower()

a_count = string_lower.count("a")
e_count = string_lower.count("e")
i_count = string_lower.count("i")
o_count = string_lower.count("o")
u_count = string_lower.count("u")

vowel_count = a_count + e_count + i_count + o_count + u_count

print(f"number of vowels is {vowel_count}.")


# In[19]:


# problem 5
word_to_check = input("enter a word: ")
word_palindrome = word_to_check.upper()

if word_palindrome == word_palindrome[::-1]:
    print(f"This word is a palindrome.")
else:
    print(f"This word is not a palindrome.")


# In[18]:


# problem 6
secret_message = input("Enter your secret message: ")
encrypted = secret_message.upper().replace(" ", "_")
print(f"encrypted secret message: {encrypted}.")


# In[ ]:




