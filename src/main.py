import json
import os
import requests
import random
import sys

def main():
  APP_TOKEN = os.environ.get("INPUT_APP_TOKEN")
  WEBHOOK_URL = ""
#   WEBHOOKS_URL = os.environ.get("INPUT_WEBHOOKS_URL")
#   MESSAGE = os.environ.get("INPUT_MESSAGE")

#  if WEBHOOKS_URL == None or MESSAGE == None:
  if APP_TOKEN == None:
    return -1
  
  headers = {'Content-Type': 'application/json; charset=utf-8'}
  data = {
    'app_token': APP_TOKEN
  }

  requests.post(WEBHOOK_URL, headers=headers, data=json.dumps(data))

if __name__ == "__main__":
  main()
