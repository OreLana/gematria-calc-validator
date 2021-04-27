from helper import dict_word
import string

DICT_WORD = dict_word()
#This function takes in a word returns the gematria of that word 
def calc_gematria(word):
  lowercase_letters = string.ascii_lowercase
  letters_dict = {letter: i for i, letter in enumerate(lowercase_letters,1)}
  gematria_value = 0
  for i in word:
    if i.isupper():
      gematria_value += 0
    else:
      gematria_value += letters_dict[i]
  return gematria_value

#This function loops through the dictionary and returns an array of any word in the dictionary that has the samme gematria as the word passed into it
def gematria(word): 
  gematria_dict = [i for i in DICT_WORD if calc_gematria(i) == calc_gematria(word)]
  return gematria_dict

print(gematria('cat'))