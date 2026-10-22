from __future__ import annotations

import json
from datetime import date
from pathlib import Path


def load_tasks(file_path: str) -> list[dict]:
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data["tasks"]


def find_overdue_tasks(tasks: list[dict], today: date) -> list[dict]:
    overdue: list[dict] = []
    for task in tasks:
        due = date.fromisoformat(task["due_date"])
        if not task.get("done") and due < today:
            overdue.append(task)
    return overdue


def complete_task(tasks: list[dict], task_id: int) -> bool:
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False


def count_open_by_owner(tasks: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for task in tasks:
        if task.get("done"):
            continue
        owner = task["owner"]
        counts[owner] = counts.get(owner, 0) + 1
    return counts
