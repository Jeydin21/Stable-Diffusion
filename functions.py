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