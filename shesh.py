keywords = {
  "अन्यथा अगर": "elif",
  "अगर": "if",
  "अन्यथा": "else",
  "सत्य": "True",
  "मिथ्या": "False",
  "दिखाएं": "print",
  "और": "and",
  "या": "or",
}

f = open("code.txt", 'r', encoding='utf-8')
out = open("out.py", 'w', encoding='utf-8')

for line in f:
  # if this is a print statement 
  # dont replace keywords except print
  if line.strip().startswith("दिखाएं"):
    line = line.replace("दिखाएं", keywords["दिखाएं"], 1)
  else:
    for key in keywords.keys():
      line = line.replace(key, keywords[key])
  out.write(line)

out.close()
f.close()

import subprocess
subprocess.call(" python out.py 1", shell=True)
