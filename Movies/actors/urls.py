from django.urls import path
from . import views

app_name = "actors"

urlpatterns = [
    path("topactor/", views.top_actor, name="top_actor"),
]