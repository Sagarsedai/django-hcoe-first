from django.shortcuts import render

from .models import Blog, BlogTag


# Create your views here.
def HomePage(request):
    query_params = request.GET
    tag = query_params.get("tag")
    try:
        # raise Exception
        tv = BlogTag.objects.get(pk=tag)
        blogs = Blog.objects.filter(tag=tv)
    except:
        blogs = Blog.objects.all()

    tags = BlogTag.objects.all()

    context = {
        "tags": tags,
        "objects": blogs,
        "current_tag": tag,
    }

    return render(request, "home.html", context)


def BlogDetailPage(request, pk):
    blog_object = Blog.objects.get(pk=pk)
    context = {
        "object": blog_object,
    }
    return render(request, "blog-detail.html", context)
