from django.urls import path
from . import views

urlpatterns = [
    path("",views.friend,name="friendo"),
    path("view_requests",views.view_request,name="viewrequest"),
    
    path("request_send/<str:username>",views.request_send,name="request_send")
]
