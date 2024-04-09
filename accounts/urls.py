from django.urls import path
from . import views
urlpatterns = [
    path("login/",views.Login,name='login'),
    path("signup/",views.signup,name='signup'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',views.activate, name='activate'),
    path("logout/",views.custom_logout,name='custom_logout'),
]
