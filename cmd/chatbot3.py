def x(prompt, chatHistory, key):
  openai.api_key = key
  chatHistory.append({"role": "user", "content": prompt})
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=chatHistory
  )['choices'][0]['message']['content']
  chatHistory.append({"role": "assistant", "content": response})
  return response, chatHistory
