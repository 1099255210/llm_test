import warnings
warnings.filterwarnings("ignore")

from revChatGPT.V1 import Chatbot
import rev.config as cfg

with open(cfg.promptPath, encoding='utf-8') as f:
  base_prompt = f.read().strip()

query = "find the basket that contains most fishes."
base_prompt = base_prompt.replace("INSERT_QUERY_HERE", query)

print(base_prompt.split('\n')[-1])

chatbot = Chatbot(config={
  "access_token": cfg.accessToken,
})
# }, conversation_id=cfg.conversationId)

response = ""
con_id = ""

for data in chatbot.ask(
  base_prompt
):
  response = data["message"]
  if not con_id:
    con_id = data["conversation_id"]

chatbot.delete_conversation(con_id)
print(response)