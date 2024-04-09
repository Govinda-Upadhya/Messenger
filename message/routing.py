from django.urls import path
from .consumer import MySyncConsumer
ws_urlpattern=[
    path("ws/sc/<str:groupkanam>",MySyncConsumer.as_asgi())
]