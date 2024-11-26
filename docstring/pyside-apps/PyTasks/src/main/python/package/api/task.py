import sys
from pathlib import Path
import logging
import json

from shiboken2 import delete

logging.basicConfig(level=logging.DEBUG)

TASKS_DIR = Path.home() / '.todo'
TASKS_FILEPATH = TASKS_DIR / 'tasks.json'

def get_tasks():
    if TASKS_FILEPATH.exists():
        with open(TASKS_FILEPATH, "r") as f:
            return json.load(f)
    return {}

def add_task(name):
    tasks = get_tasks()
    if name in tasks.keys():
        logging.error(f"Task '{name}' already exists")
        return False

    tasks[name] = False
    logging.info(f"Added task '{name}'")
    _save_tasks(tasks=tasks)
    return True

def remove_task(name):
    tasks = get_tasks()
    if name not in tasks.keys():
        logging.error(f"Task '{name}' does not exist")
        return False

    del tasks[name]
    logging.info(f"Task '{name}' removed")
    _save_tasks(tasks=tasks)
    return True

def set_task_status(name, done=True):
    tasks = get_tasks()
    if name not in tasks.keys():
        logging.error(f"Task '{name}' does not exist")
        return False
    tasks[name] = done
    logging.info(f"Task '{name}' set to {done}")
    _save_tasks(tasks=tasks)
    return True


def _save_tasks(tasks):
    Path.mkdir(TASKS_DIR, parents=True, exist_ok=True)
    with open(TASKS_FILEPATH, "w") as f:
        json.dump(tasks, f, indent=4)
    logging.debug(f"Saved tasks to {TASKS_FILEPATH}")


if __name__ == '__main__':
    add_task('Apprendre Python')
    add_task('Refaire un exercice')
    set_task_status('Refaire un exercice')
    remove_task("Apprendre Python")