import charactermapping
from charactermapping import character_to_english, character_to_arabic

def toFullEnglish(x)->str:
  y = ''
  for i in range(len(x)):
    u = character_to_english.get(x[i], "NotFound")
    y += u if u != "NotFound" else x[i]
  return y

def toFullArabic(x)->str:
  y = ''
  for i in range(len(x)):
    u = character_to_arabic.get(x[i], "NotFound")
    y += u if u != "NotFound" else x[i]
  return y
