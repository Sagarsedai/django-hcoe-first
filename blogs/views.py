from django.shortcuts import render
from .models import Blog


# Create your views here.
def HomePage(request):

    blogs = Blog.objects.all()
    context = {
        "objects": blogs,
    }
    return render(request, "home.html", context)
