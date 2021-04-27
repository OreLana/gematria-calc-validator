def dict_word():
  with open('../assets/words.txt') as fd:
    return fd.read().splitlines()

