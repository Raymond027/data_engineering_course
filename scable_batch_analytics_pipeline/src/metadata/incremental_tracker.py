import json
import os


CHECKPOINT_FILE = "metadata/checkpoint.json"


def get_last_processed_date():

    if not os.path.exists(CHECKPOINT_FILE):
        return None

    with open(CHECKPOINT_FILE) as f:
        return json.load(f)["last_date"]


def update_checkpoint(date):

    with open(CHECKPOINT_FILE, "w") as f:
        json.dump({"last_date": date}, f)