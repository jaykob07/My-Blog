from django.urls import path
from .views import render_post, post_details

app_name = "blog"

urlpatterns = [
    path('', render_post, name='posts'),
    path('<int:post_id>', post_details, name="post_details"),    # numero entero int post es el / y id el numero id
]
