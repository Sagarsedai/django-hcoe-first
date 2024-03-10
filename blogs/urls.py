from django.urls import path
from .views import HomePage, BlogDetailPage


urlpatterns = [
    path("", HomePage, name="index"),
    path("blog-detail/<int:pk>/", BlogDetailPage, name="blog_detail"),
]
