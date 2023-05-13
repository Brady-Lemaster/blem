import openai
def x(prompt, profile):
  openai.api_key = profile[3]
  response = openai.Completion.create(model=profile[0], prompt=prompt, temperature=profile[1], max_tokens=profile[2])
  responseTrimmed = response["choices"][0]["text"].strip()
  return responseTrimmed
