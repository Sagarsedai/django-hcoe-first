from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("blogs.urls")),
    path("admin/", admin.site.urls),
]

from demoproject import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
