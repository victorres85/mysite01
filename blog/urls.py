from django.urls import path
from blog.views import post_view

urlpatterns = [
    path('', post_view.postView.as_view(), name='home'),
    path('<slug:slug>/', post_view.postDetail.as_view(), name='post_detail')
]