from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ai_utils import predict_priority

@api_view(["POST"])
def predict_priority_view(request):
  data = request.data
  hours_until_deadline = data.get("hours_until_deadline")
  description = data.get("description")

  if hours_until_deadline is None or description is None:
    return Response({"error": "Invalid input data"}, status=400)
  
  priority = predict_priority(hours_until_deadline, description)
  return Response({"priority_score": priority})