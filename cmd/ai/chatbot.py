import openai
def x(prompt, limit, key):
  openai.api_key = key
  response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=limit)
  responseTrimmed = response["choices"][0]["text"].strip()
  return responseTrimmed
