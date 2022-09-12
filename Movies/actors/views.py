from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def top_actor(request : HttpRequest):
    top_actor : str = "Tom Cruise"

    return HttpResponse(f"The top actor in the world is {top_actor}")

