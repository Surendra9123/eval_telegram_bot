#Install requirements.txt using python..

import os

def install():
 try:
  file = open("requirements.txt","r")
  lines = file.read()
  file.close()
 except:
  print("requirements.txt file not found unable to install requirements!!")
  return
 for module in lines.split("\n"):
   try:
    os.system(f"pip3 install {module}")
   except Exception as e:
    print(e)
    continue
 print("Requirements installed successfully!")

install()
