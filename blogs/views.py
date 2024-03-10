from django.shortcuts import render

from .models import Blog, BlogTag


# Create your views here.
def HomePage(request):
    query_params = request.GET
    tag = query_params.get("tag")
    try:
        blogs = Blog.objects.filter(tag__id=tag)
    except:
        blogs = Blog.objects.all()
    tags = BlogTag.objects.all()

    context = {
        "tags": tags,
        "objects": blogs,
        "current_tag": tag,
    }

    return render(request, "home.html", context)
    # return render(request, "home.html")
