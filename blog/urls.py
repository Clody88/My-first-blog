from django.urls import path
from . import views

# we are adding our first URL pattern
urlpatterns = [
    path('', views.post_list, name='post_list'),
]