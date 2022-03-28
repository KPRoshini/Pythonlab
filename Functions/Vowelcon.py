wd=input("Enter the string:")
def word_count(wd):
  vowel= 0
  ct=0
  for j in wd:
      if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u'or j=='A' or j=='E' or j=='I' or j=='O' or j=='U'):
        vowel=vowel+1
      else:
        ct=ct+1
  print("Number of vowels in the word:",vowel)
  print("Number of consonants in the word:",ct)
word_count(wd)
