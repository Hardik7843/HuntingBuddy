from apify_client import ApifyClient
import json
import time


apify_client = ApifyClient('apify_api_zIrNjSOeE1FO4VtTTFKdQ66uXBebX94DDVFp')

task = apify_client.task("6mE22yvtCbJwJ0j0d")

x = task.call()

last_run  = task.last_run(status='SUCCEEDED' , origin = 'API')

dataset = last_run.dataset()

jobs = dataset.list_items(fields = ['company' , 'description'])

jobs = jobs.items


# time.sleep(10)
print(f"Run Executed Please view the log on web")
with open('autorun.json' , 'w') as f:
    json.dump(jobs , f)

# last_run = actor_indeed_scrapper.last_run(status = 'SUCCEEDED' , origin = 'API')

# time.sleep(120)

# runs = actor_indeed_scrapper.runs()

# last_run = runs.list(limit = 1 , desc = False , status = 'SUCCEEDED')

# last_dataset = last_run.dataset()

# last_dataset_items = last_dataset.list_items(fields = ['descriptions'])





