# Import the required module for text  
# to speech conversion 
#Resource: https://www.geeksforgeeks.org/convert-text-speech-python/
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 
  
# The text that you want to convert to audio 
mytext = 'Welcome to my GitHub please also check out my YouTube channels, for programming https://www.youtube.com/channel/UCbmb5IoBtHZTpYZCDBOC1CA and for computer science, https://www.youtube.com/user/randerson112358 !'
  
# Language in which you want to convert 
#language = 'pt-br' #Portuguese (Brazil)
language = 'en' #English
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 
  
# Playing the converted file 
os.system("start welcome.mp3")  #This command is for windows only for either operating systems download mpg321 and use os.system("mpg321 welcome.mp3") 
