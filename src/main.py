import json
import os
import requests
import random
import sys

def main():
  USER_TOKEN = os.environ.get("INPUT_USER_TOKEN")
  MESSAGE = os.environ.get("INPUT_MESSAGE")
  WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

  if USER_TOKEN == None:
    return -1
  
  headers = {'Content-Type': 'application/json; charset=utf-8'}
  data = {
    'user_token': USER_TOKEN,
    'message': MESSAGE
  }

  requests.post(WEBHOOK_URL, headers=headers, data=json.dumps(data))

if __name__ == "__main__":
  main()
