"""
Django views for integrating FastAPI with Django.

This module provides a Django view that maps requests to a FastAPI application
using the FastAPI TestClient.
"""

import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from fastapi.testclient import TestClient
from .fastapi_app import create_fastapi_app


# Create your FastAPI app
fastapi_app = create_fastapi_app()

# Create a TestClient for the FastAPI app
client = TestClient(fastapi_app)


@csrf_exempt
def fastapi_view(request, path):
    """
    Map Django requests to the FastAPI test client requests.

    This view function intercepts Django requests and forwards them to the
    FastAPI application, then returns the FastAPI response back as a Django
    HttpResponse.

    Args:
        request (HttpRequest): The Django request object.
        path (str): The path of the requested URL.

    Returns:
        HttpResponse: The response object created from the FastAPI response.
    """
    if request.method == "GET":
        response = client.get(f"/{path}")
    elif request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        response = client.post(f"/{path}", json=body)
    elif request.method == "PUT":
        body = json.loads(request.body.decode('utf-8'))
        response = client.put(f"/{path}", json=body)
    elif request.method == "DELETE":
        response = client.delete(f"/{path}")
    else:
        return HttpResponse(status=405)  # Method not allowed

    django_response = HttpResponse(
        content=response.content,
        status=response.status_code,
        content_type=response.headers.get('content-type', 'application/json'),
    )
    return django_response
