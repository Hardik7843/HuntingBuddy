from apify_client import ApifyClient
import json
import time
import os
from dotenv import load_dotenv

from dotenv import dotenv_values

config = dotenv_values(".env") 
client_id = config['client_token']
task_id = config['indeed_scrapper_task']

# print(type(client_id))
apify_client = ApifyClient(client_id)

task = apify_client.task(task_id)

x = task.call()

last_run  = task.last_run(status='SUCCEEDED' , origin = 'API')

dataset = last_run.dataset()

jobs = dataset.list_items(fields = ['company' , 'description'])

jobs = jobs.items


print(f"Run Executed Please view the log on web")
with open('autorun.json' , 'w') as f:
    json.dump(jobs , f)