[![shesh](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Ananta_Shesha.jpg/220px-Ananta_Shesha.jpg)](https://en.wikipedia.org/wiki/Shesha)


##### अगर आप इस पेज को नहीं पढ़ पा रहे हैं तो [यहां जा सकते हैं](./README.md) <br><br><br>


# Shesh

### A simple non-english programming language

<br>

## The Concept

Python 3 has almost 35 keywords. If we replace those with words in any other language then we could create a pseudo progamming language. This repository is an attempt to do that.

<br>

## How it works
We replace the associated keywords in non-english language to original python keywords and recreate a runnable python script. Then we run that script to get the output.

```python
अगर (सत्य):
    दिखाएं("मैं सत्य हूँ. सत्यमेव जयते!")
अन्यथा:
    दिखाएं("मैं मिथ्या हूँ. अँधेरा कायम रहे!")


a = 50
अगर (a < 40):
    दिखाएं("कम है.")
अन्यथा अगर (a > 40 और a < 70):
    दिखाएं("ठीक है!")
अन्यथा: 
    दिखाएं("अधिक है.")
```

Result:
```python
मैं सत्य हूँ. सत्यमेव जयते!
ठीक है!
```

The original script is converted to following code that makes this result possible:
```python
if (True):
  print("मैं सत्य हूँ. सत्यमेव जयते!")
else:
  print("मैं मिथ्या हूँ. अँधेरा कायम रहे!")


a = 50
if (a < 40):
  print("कम है.")
elif (a > 40 and a < 70):
  print("ठीक है!")
else: 
  print("अधिक है.")

```
<br>

## Keywords added till now
```python
"अन्यथा अगर": "elif",
"अगर": "if",
"अन्यथा": "else",
"सत्य": "True",
"मिथ्या": "False",
"दिखाएं": "print",
"और": "and",
"या": "or",
```
<br>

## Contribution
There will be many edge cases in parsing and converting the code, but we can do it slowly and incrementally.