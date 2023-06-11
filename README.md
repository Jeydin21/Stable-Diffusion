# Stable Diffusion
This is an app I made just to practice my frontend development skills in HTML and CSS

Basically this is a Flask app that takes in a prompt and amount of results from the user, then displays the results on another page. 

I used the [OpenAI Python library](https://platform.openai.com/docs/api-reference/introduction?lang=python) to use stable diffusion to generate the results.

### Create a file named funcitons.py with the following code:
```py
import openai

openai.api_key = "No"

def getImageLinks(data):
  list = []
  for link in data["data"]:
    list.append(link["url"])
  return list

def getData(prompt, amount):
  results = openai.Image.create(prompt = str(prompt), n = int(amount), size="512x512")
  print(getImageLinks(results))
  return getImageLinks(results)
  ```
  And make sure to replace the API key variable with your own OpenAI API Key.
