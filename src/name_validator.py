def name_validator(name):
  two_names = (name.split(' '))

  #this line of code validates if the name entered is a string and contains two names
  if type(name) != str and len(two_names) != 2: 
    raise Exception('Name must be a string and must contain two names separated by a single space')
  
  #This line validates that the name conntains just alphabets
  if not(name.replace(" ","")).isalpha(): 
    raise ValueError('Name must contain only alphabets')

  #This line validates the length of both names
  if not((len(two_names[0]) >= 5 and len(two_names[0]) <= 20) and (len(two_names[1]) >= 5 and len(two_names[1]) <= 20)):
    raise Exception('Each name must be have 5 or more characters but not more than 20 characters ')

  return name  
 
  
print(name_validator('Oreoluwa Lanabnfdjhskhfjsdkbcvjcdjdschfdjvhnfdjhvfkdvldfjvhgfjdbhkdvfhjbdkhgjvjbnfjdhvkdvkdskv'))