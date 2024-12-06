from celery import shared_task
from .models import Task
from .ai_utils import predict_priority

@shared_task
def update_priority_scores():
    tasks = Task.objects.all()
    for task in tasks:
        task.priority_score = predict_priority(task.hours_until_deadline, task.description)
        task.save()
    return f"Updated {len(tasks)} tasks' priority scores"