from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .ai_utils import predict_priority
from .models import Task
from .serializer import TaskSerilizer

@api_view(["GET", "POST"])  # Allow both GET and POST methods
def predict_priority_view(request):
    if request.method == "POST":
        # Handle POST request (create or update a task)
        data = request.data
        task_id = data.get("task_id")
        hours_until_deadline = data.get("hours_until_deadline")
        description = data.get("description")

        if hours_until_deadline is None or description is None:
            return Response({"error": "Invalid input data"}, status=400)

        priority_score = predict_priority(hours_until_deadline, description)

        if task_id:
            task = Task.objects.get(id=task_id)
            task.hours_until_deadline = hours_until_deadline
            task.description = description
            task.priority_score = priority_score
            task.save()
        else:
            task = Task.objects.create(
                description=description,
                hours_until_deadline=hours_until_deadline,
                priority_score=priority_score
            )

        return Response({
            "task_id": task.id,
            "description": task.description,
            "hours_until_deadline": task.hours_until_deadline,
            "priority_score": task.priority_score,
        })

    elif request.method == "GET":
        # Handle GET request (retrieve all tasks)
        tasks = Task.objects.all()
        serializer = TaskSerilizer(tasks, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail_view(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # GET request: Retrieve a single task
        serializer = TaskSerilizer(task)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # PUT request: Update a task
        serializer = TaskSerilizer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # DELETE request: Delete a task
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    