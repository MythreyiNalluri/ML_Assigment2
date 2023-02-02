Str='The quick Brow Fox'
lower=0
upper=0
for i in Str:
      if(i.isupper()):
            upper+=1
      elif(i.islower()):
            lower+=1
print("The number of Uppercase characters is:",upper)
print("The number of lowercase characters is:",lower)