from django.urls import path
from blog.views import post_view

urlpatterns = [
    path('', post_view.postView.as_view(), name='home')
]