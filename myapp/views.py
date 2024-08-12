from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from fastapi import FastAPI
from fastapi.testclient import TestClient
from .fastapi_app import create_fastapi_app_with_django_integration
import json

# Create your FastAPI app
fastapi_app = create_fastapi_app_with_django_integration()

# Create a TestClient for the FastAPI app
client = TestClient(fastapi_app)

@csrf_exempt
def fastapi_view(request, path):
    # Map the Django request to the FastAPI test client request
    if request.method == "GET":
        response = client.get(f"/{path}")
    elif request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))  # Parse the request body as JSON
        response = client.post(f"/{path}", json=body)
    elif request.method == "PUT":
        body = json.loads(request.body.decode('utf-8'))  # Parse the request body as JSON
        response = client.put(f"/{path}", json=body)
    elif request.method == "DELETE":
        response = client.delete(f"/{path}")
    else:
        return HttpResponse(status=405)  # Method not allowed

    # Create a Django HttpResponse from the FastAPI response
    django_response = HttpResponse(
        content=response.content,
        status=response.status_code,
        content_type=response.headers.get('content-type', 'application/json'),
    )
    return django_response
