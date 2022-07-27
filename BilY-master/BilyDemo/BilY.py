from msilib.schema import Shortcut
from click import format_filename
from pyparsing import Regex
from textBased import toFullEnglish, toFullArabic
from english_words import english_words_set
from ar_corrector.corrector import Corrector
from textblob import Word
from gingerit.gingerit import GingerIt
 
def isEnglish(s):
  return s.isascii()

def correct_english_word_spelling(word)->str:
  word = Word(word)
  result = word.correct()
  return result
    
def quickFix(s):
  with open("dataBase.txt") as f:
    wordlist = []
    for line in f:
      wordlist.append(line.strip())
  
  a = s.split()
  b = []
  for i in a:
    j = toFullEnglish(i)
    if j in english_words_set or j in wordlist:
      b.append(toFullEnglish(i))
    else:
      b.append(toFullArabic(i))
  
  return ''.join([x+' ' for x in b])

def spellingFix(s)->str:
  corr = Corrector()
  a = s.split()
  b = []
  isItAllArabic = True
  for i in a:
    if isEnglish(i):
      isItAllArabic = False
  if isItAllArabic:
    return corr.contextual_correct(s)

  for i in a:
    if isEnglish(i):
      b.append(correct_english_word_spelling(i))
    else:
      x = corr.spell_correct(i, 1)
      if x:
        b.append(i)
      else:
        b.append(x[0][0])  
  return ''.join([x+' ' for x in b])

def grammerFix(s)->str:
  corr = Corrector()
  a = s.split()
  b = []
  isItAllArabic = True
  for i in a:
    if isEnglish(i):
      isItAllArabic = False
  if isItAllArabic:
    return corr.contextual_correct(s)
  # otherwise we use english grammer
  parser = GingerIt()
  return parser.parse(s)['result']

def addSlang(s)->str:
  with open("dataBase.txt") as f:
    wordlist = []
    for line in f:
      wordlist.append(line.strip())
  a = s.split()
  if len(a) == 0:
    return "the sky is the limit here.(don’t forget to be creative :D"
  if a[0] in wordlist or a[0] in english_words_set:
    return "the word is already in the library"
  else:
    with open("dataBase.txt", "a") as f:
      f.write('\n')
      f.write(a[0])
    return "the words has been successfully added to the library"
  
def addShortcut(s, x):
  with open("dataBase.txt") as f:
    wordlist = []
    for line in f:
      wordlist.append(line.strip().split(','))
    if s in wordlist:
      return False
  with open("shortCut.txt", "a") as f:
    f.write('\n')
    f.write(s + ','+ x)
    return True
  return False