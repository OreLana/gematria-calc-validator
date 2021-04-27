## Gematria
When you were little, you might have created or used a “secret” code in which a was 1, b was 2, c was 3, and so forth, until z (which was 26). This type of code happens to be quite ancient and was used by a number of different groups more than 2,000 years ago which was named Gematria in Hebrew.

[Gematria - Wikipedia](https://en.wikipedia.org/wiki/Gematria) is an alphanumeric code of assigning a numerical value to a name, word or phrase based on its letters.

Gematria is a python module that consists of a gematria function that takes in a word as a parameter, calculates the gematria value of that word and returns a list of strings of all who have the same gematria value from an English dictionary list of words in the file 'gematria-calc-validator/assets/words.txt'.


For example:

```python

gematria('cat')

['Aani', 'abu', 'Acaena', 'acara', 'Acrab', 'act', 'aer', 'aho', 'Akal', 'alef', 'alk', 'ani', 'araca', 'arad', 'are', 'ava', 'aw', 'babble', 'Bahama', 'bail', 'bali', 'bang', 'Baraca', 'Bare', 'beback', 'bedded', 'beice', 'benab', 'blade', 'blee', 'bocca', 'bog', 'Cacara', 'Caddo', 'Cain', 'canada', 'cat', 'cep', 'chaff', 'Chagga', 'chaka', 'chal', 'chid', 'cled', 'crab', 'Cuba', 'dado', 'Damia', 'danda', 'Dani', 'das', 'dean', 'Dedan', 'deface', 'Dene', 'dhak', 'Dian', 'dich', 'Dode', 'doe']


```

 
## Simple Interactive Calculator

Simple Interactive Calculator is a command-line interactive calculator built based on the assumption that User input is a formula that consists of a number, an operator (at least +, -, *, / ), and another number, separated by white space (e.g. 1 + 1).  

For example:

```python

>>> 1 + 1
2.0
>>> 3.2 - 1.5
1.7000000000000002
>>> quit

```

## Name Validator

Name validator is a python module that consists of a fucntion that takes in a name as an argument and validates the name using the following constraints:

- Must be a string which is a combination of two substrings, each representing first name and last name respectively, Ex. "John Doe"
- Must only contain alphabets and a single space character that separates the first and last name substrings
- The length of the first and last name substrings each must be >= 5 characters and <= 20 characters

An exception with a meaningful error message is raised when the constraint is violated.
