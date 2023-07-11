import json

email = ''
password = ''
accessToken = ''
promptPath = ''
conversationId = ''

with open('cfg.json') as f:
  res = json.load(f)
  email = res['email']
  password = res['password']
  accessToken = res['accessToken']
  promptPath = res['promptPath']
  conversationId = res['conversationId']